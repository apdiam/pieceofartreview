from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name="home"),  # Apostolis: home function will be called
    path('details/<int:id>/', views.details, name="details"), # Apostolis: details function for each Piece of Art
    path('addpiece/', views.add_pieces, name="add_pieces"),  # Apostolis: function to add a Piece of Art
    path('editpiece/<int:id>/', views.edit_pieces, name="edit_pieces"), # Apostolis: Take care with the '/' characters!
    path('deletepiece/<int:id>/', views.delete_pieces, name="delete_pieces"),
    path('addreview/<int:id>/', views.add_review, name="add_review"),
    path('editreview/<int:piece_id>/<int:review_id>/', views.edit_review, name="edit_review"),
    path('deletereview/<int:piece_id>/<int:review_id>/', views.delete_review, name="delete_review"),
]

