 Django

    1. Create <project folder> and enter the folder
    2. Virtual environment
        a. virtualenv venv
        b. virtualenv venv -p python3
    3. Activate
        a. source venv/bin/activate
    4. Make directory src then enter to  src
        a. mkdir src
        b. cd src
    5. Install django and create project
        a. pip install django==1.11.15
        b. pip install pillow psycopg2    (  psycopg2-binary  )
        c. django-admin.py startproject  <project folder name>
    6. Change dir to  <project folder name>
        a. cd <project folder name>
        b. mkdir static media templates
        c. python manage.py runserver




    1. To activate virtualenv
        a. source ../../venv/bin/activate
    2. To open python shell
        a. python manage.py shell
    3. Create a new App
        a. python manage.py startapp <app name>



    1. Create database and user in phppgadmin
        a. sudo su postgres
        b. createdb <dbname>
        c. createuser shibil -P  (create only once next time grant privileges)
            i.  femmepk -> shibil -> 12345
        d. psql
        e. grant all privileges on database femmepk to shibil;
        f. \q
        g. exit
    2. Create super user
        a. python manage.py createsuperuser
            i. shibil -> shibil789
    3. Migration comments
        a. python manage.py makemigrations && python manage.py migrate
        c. python manage.py loaddata initial_data user_groups permissions notification
    4. Delete migration
        a. find . -path "*/migrations/*.py" -not -name "__init__.py" -delete && find . -path "*/migrations/*.pyc"  -delete
    5. Read and write from file
        a. pip freeze > r.txt
        b. pip install -r r.txt
        c. python manage.py loaddata initial_data user_groups permissions notification

    6. database export and import
        a. python manage.py dumpdata > database.json
        b. python manage.py loaddata database.json







Django documentation notes

    1. Models objects return functions
        a. all()
        b. filter()
            i. filter value ( instance= , )
        c. exclude()
            i. To avoid some fields
        d. get()
            i. for one value
    2. Models objects create functions
        a. create()
    3. Forms for single line
        a. for field in form:
field.id_for_label   ||  field.label  ||  field
endfor
        b. form.as_p
    4. Form validation views.py(function)
    a. if request.method=="POST":
    	name = request.POST.get('name')
    	email = request.POST.get('email')

    	FormClassName.objects.create(
        	name = name,
        	email = email,
    	)
    	return HttpResponse('Form Submitted')
	else:
    		return HttpResponse('Invalid Request')
