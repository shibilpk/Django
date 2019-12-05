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

    path('',general_views.app,name='app'),
    path('app/',general_views.app,name='app'),
    
    path('notification/read/<int:pk>', views.read_notification, name='read_notification'),

    path('app/college/', include('college.urls', namespace="college"))

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
