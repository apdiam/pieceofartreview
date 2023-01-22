from django.contrib import admin
from .models import *
# Register your models here

# Apostolis: superuser: admin
#            password : admin

admin.site.register(PieceOfArt)
admin.site.register(Review)

