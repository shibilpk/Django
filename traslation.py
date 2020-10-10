Translation 
1 load {% load i18n %} in every template for Translation
2 {% trans 'Lets translate this' %}

3 set a location to store:
    USE_I18N = True
    LOCALE_PATHS = (
        os.path.join(BASE_DIR, 'locale'),
    )

    then create this folder
4 run comment 
    django-admin makemessages -l ml

    this generate a file.

    then run
    django-admin compilemessages

5 then add ml in setings 

6 middleware
    ...
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', 
    'django.middleware.common.CommonMiddleware',
    ...

7 in main url 
    from django.conf.urls.i18n import i18n_patterns

    urlpatterns = [

         url(r'^admin/', admin.site.urls),   
            url(r'^i18n/', include('django.conf.urls.i18n')),
    ]


    urlpatterns += i18n_patterns(
        
            url(r'^app/web/', include('web.urls', namespace="web")),

            prefix_default_language=False

    )


    seperate all url that we need to translate in pages no need admin url


8   set lang list

    from django.utils.translation import ugettext_lazy as _
    LANGUAGES = (
        ('en', _('English')),
        ('ml', _('Malayalam')),
    )



 <a href="{% url 'switch_language' %}?lang=en" title="English">
            <button type="submit" class="btn btn-primary">English</button>
        </a>

url(r'^switch-language/$', general_views.switch_language, name='switch_language'),
from django.utils.translation import activate

def switch_language(request):
    lang = request.GET.get('lang')
    if lang == "en":
        activate('en')
    elif lang == "ml":
        activate('ml')
    
    return HttpResponseRedirect(reverse('dashboard'))