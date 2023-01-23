django-admin startproject <project_name>
python manage.py startapp <app_name>
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
python manage.py changepassword <username>
python manage.py runserver

Sources:
https://docs.djangoproject.com/en/4.1/
https://stackoverflow.com/
https://stackexchange.com/
https://www.youtube.com/
https://getbootstrap.com/docs/4.0/getting-started/introduction/


Description:
The main application of our project is main. Accounts application is supposed to be for the user management, but it is a feature for the future. 

views.py: Implements the Logic of our project. Whatever action/behaviour takes part on our website, it is defined in views.py

models.py: Describes the structure of our Database. Specifically, the Pieces of Art and Reviews.

forms.py: Describes a few forms we use on our website, like the one to add new pieces of art.

urls.py: The urls used on our website, in collaboration with the logic of views.

templates/main: Includes all the .html files, namely the pages. Upon them are depicted and run the logic from views.py, which uses our DB(models).