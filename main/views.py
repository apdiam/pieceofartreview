from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Avg
# Apostolis: Main logic of our application happens here.


# Create your views here.

# Apostolis: Homepage
def home(request):
    query = request.GET.get("title")
    if query:
        allPiecesOfArt = PieceOfArt.objects.filter(name__icontains=query)
    else:
        allPiecesOfArt = PieceOfArt.objects.all()
    # allPiecesOfArt = PieceOfArt.objects.all() # Apostolis: Select * pieces of art

    context = {
        "piecesofart": allPiecesOfArt,
    }

    return render(request, 'main/index.html', context)

# Apostolis: details for each piece of art. We find it by search its 'id'. That's why we pass it as argument.


def details(request, id):
    pieceofart = PieceOfArt.objects.get(id=id)
    reviews = Review.objects.filter(piece=id).order_by("-comment")

    average = reviews.aggregate(Avg("rating"))["rating__avg"]
    if average == None:
        average = 0
    average = round(average, 2)

    context = {
        "pieceofart": pieceofart,
        "reviews": reviews,
        "average": average,
    }

    return render(request, 'main/details.html', context)


def add_pieces(request):
    if request.method == "POST":
        form = PieceForm(request.POST or None)  # Apostolis: Use the Form created to add pieces from addpiece.html

        # Apostolis: check if the form is ok/right
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("main:home")
    else:
        form = PieceForm()
    return render(request, 'main/addpiece.html', {"form": form, "controller": "Add Pieces"})


def edit_pieces(request, id):
    piece = PieceOfArt.objects.get(id=id)

    if request.method == "POST":
        form = PieceForm(request.POST or None, instance=piece)

        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("main:details", id)
    else:
        form = PieceForm(instance=piece)
    return render(request, 'main/addpiece.html', {"form": form, "controller": "Edit Pieces"})


def delete_pieces(request, id):
    piece = PieceOfArt.objects.get(id=id)

    piece.delete()
    return redirect("main:home")


def add_review(request, id):
    if request.user.is_authenticated:
        piece = PieceOfArt.objects.get(id=id)
        if request.method == "POST":
            form = ReviewForm(request.POST or None)
            if form.is_valid():
                data = form.save(commit=False)
                data.comment = request.POST["comment"]
                data.rating = request.POST["rating"]
                data.user = request.user
                data.piece = piece
                data.save()
                return redirect("main:details", id)
        else:
            form = ReviewForm()
        return render(request, 'main/details.html', {"form": form})
    else:
        return redirect("accounts:login")


def edit_review(request, piece_id, review_id):
    if request.user.is_authenticated:
        piece = PieceOfArt.objects.get(id=piece_id)

        review = Review.objects.get(piece=piece, id=review_id)

        if request.user == review.user:
            if request.method == "POST":
                form = ReviewForm(request.POST, instance=review)
                if form.is_valid():
                    data = form.save(commit=False)
                    if (data.rating > 10) or (data.rating < 0):
                        error = "Out of range. Please select rating from 0 to 10."
                        return render(request, 'main/editreview.html', {"error": error, "form": form})
                    else:
                        data.save()
                        return redirect("main:details", piece_id)
            else:
                form = ReviewForm(instance=review)
            return render(request, 'main/editreview.html', {"form": form})
        else:
            return redirect("main:details", piece_id)
    else:
        return redirect("accounts:login")


def delete_review(request, piece_id, review_id):
    if request.user.is_authenticated:
        piece = PieceOfArt.objects.get(id=piece_id)

        review = Review.objects.get(piece=piece, id=review_id)

        if request.user == review.user:
            review.delete()
        return redirect("main:details", piece_id)

    else:
        return redirect("accounts:login")