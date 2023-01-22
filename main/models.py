from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Apostolis: A Database has Tables.
#            Each Table has fields.
#            Therefore, each table with fields will be represented in the database as a model, from here.
#            Then, register each model in admin.py
#            After each in the Database, run python 'manage.py makemigrations' & 'python manage.py migrate' again.


class PieceOfArt(models.Model):
    name = models.CharField(max_length=300)
    creator = models.CharField(max_length=300)
    description = models.TextField(max_length=2000)
    creation_year = models.DateField()
    averageRating = models.FloatField(default=0)
    image = models.URLField(default=None, null=True)  # Apostolis: field which includes a url to an image of the painting

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Review(models.Model):
    piece = models.ForeignKey(PieceOfArt, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.user.username

