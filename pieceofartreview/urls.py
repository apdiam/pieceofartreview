"""
URL configuration for pieceofartreview project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Apostolis: Create a url for each application/component of the website/project.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Apostolis: include() the path to main.urls.py, namely our application
    path('accounts/', include('accounts.urls')),  # Apostolis: 2nd application for our project/website
]
