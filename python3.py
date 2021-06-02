#setting up virtual environment (python 3) // CHANGES
    virtualenv venv -p python3
    cd src && pip install django && pip install pillow
    django-admin.py startproject project
    pip install psycopg2-binary

#MAIN urls.py
from django.urls import include, path, re_path
from django.contrib import admin
from main import views as general_views
from django.conf import settings
from registration.backends.default.views import RegistrationView
from users.forms import RegForm
from users.backend import user_created
from django.views.static import serve
from django.conf.urls.static import static


app_name='college_union'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('notification/read/<int:pk>', views.read_notification, name='read_notification'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
