Django


1. Create <project folder> and enter the folder
2. Virtual environment
   1. virtualenv venv
   2. virtualenv venv -p python3
3. Activate
   1. source venv/bin/activate
4. Make directory src then enter to  src 
   1. mkdir src 
   2. cd src
5. Install django and create project
   1. pip install django==1.11.15
   2. pip install pillow psycopg2    (  psycopg2-binary  )
   3. django-admin.py startproject  <project folder name>
6. Change dir to  <project folder name>
   1. cd <project folder name>
   2. mkdir static media templates
   3. python manage.py runserver








1. To activate virtualenv
   1. source ../../venv/bin/activate
2. To open python shell
   1. python manage.py shell
3. Create a new App
   1. python manage.py startapp <app name>






1. Create database and user in phppgadmin
   1. sudo su postgres
   2. createdb <dbname>  
   3. createuser shibil -P
      1.  femmepk -> shibil -> 12345
   4. psql
   5. grant all privileges on database femmepk to shibil;
   6. \q
   7. exit
2. Create super user
   1. python manage.py createsuperuser
      1. shibil -> shibil789
3. Migration comments
   1. python manage.py makemigrations
   2. python manage.py migrate
   3. python manage.py loaddata initial_data user_groups permissions notification
4. Delete migration
   1. find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
   2. find . -path "*/migrations/*.pyc"  -delete
5. Read and write from file
   1. pip freeze > r.txt
   2. pip install -r r.txt
   3. python manage.py loaddata initial_data user_groups permissions notification














Django documentation notes




1. Models objects return functions
   1. all()
   2. filter()         
      1. filter value ( instance= , )
   3. exclude()
      1. To avoid some fields
   4. get() 
      1. for one value 
2. Models objects create functions
   1. create()
3. Forms for single line
   1. for field in form:
field.id_for_label   ||  field.label  ||  field
endfor
   2. form.as_p
4. Form validation views.py(function)
1. if request.method=="POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            
            FormClassName.objects.create(
                name = name,
                email = email,
            )
            return HttpResponse('Form Submitted')
        else:
                    return HttpResponse('Invalid Request')






Django Pagination
1. pip install django-el-pagination
2. Register at INSTALLED_APP in setting -
   1. ‘el_pagination ’
3.  In template
   1. {% load el_pagination_tags %}
   2.  {% paginate 21 instances %}
   3. set loader temp


Auto Complete
1. From App
   1. urls.py        
      1. from whichapp.views import NameAutocomplete
      2. urlpatterns = [        url(r'^anyname-autocomplete/$',NameAutocomplete.as_view(),name='urlname_autocomplete',),
   2. views.py
      1. from dal import autocomplete
      2. class NameAutocomplete(autocomplete.Select2QuerySetView):
        def get_queryset(self):
            if not self.request.user.is_authenticated():
                return whichapp.objects.none()


            items = whichapp.objects.filter(is_deleted=False)


            if self.q:
                query = self.q
                items = items.filter(Q(name__icontains=query) | Q(phone__icontains=query) | Q(email__icontains=query) | Q(address__icontains=query)
)


            return items
2. To App
   1. forms.py
      1.                 'fieldname' : autocomplete.ModelSelect2(url='mainappulrname:urlname_autocomplete ',attrs={'data-placeholder': 'Product','data-minimum-input-length': 0},),


3. {{ formname.media }}




User Authentication
1. pip install django-registration-redux
2. In main setting
   1. register app -  ‘registration’,
   2. LOGIN_URL = '/seturl/url/'
LOGOUT_URL = '/seturl/url/'
LOGIN_REDIRECT_URL = '/'
3. main url.py
   1.         url(r'^app/accounts/', include('registration.backends.default.urls')),
4.