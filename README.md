 ## Django

    1. Create <project folder> and enter the folder
    2. Virtual environment
            virtualenv venv
            virtualenv venv -p python3
    3. Activate
            source venv/bin/activate
    4. Make directory src then enter to  src
            mkdir src
            cd src
    5. Install django and create project
            pip install django==1.11.15
            pip install pillow psycopg2    (  psycopg2-binary  )
            django-admin.py startproject  <project folder name>
    6. Change dir to  <project folder name>
            cd <project folder name>
            mkdir static media templates
            python manage.py runserver




    1. To activate virtualenv
            source ../../venv/bin/activate
    2. To open python shell
            python manage.py shell
    3. Create a new App
            python manage.py startapp <app name>

    1. start a new app
            python manage.py startapp web

    2. register in INSTALLED APPS
            'web'

    3. define template directory in TEMPLATES
            'templates'


    1. Create database and user in phppgadmin
            sudo su postgres
            createdb <dbname>
            createuser shibil -P  (create only once next time grant privileges)
                (femmepk -> shibil -> 12345)
            psql
            grant all privileges on database femmepk to shibil;
            \q
            exit
    2. Create super user
            python manage.py createsuperuser
                (shibil -> shibil789)
    3. Migration comments
            python manage.py makemigrations && python manage.py migrate
            python manage.py loaddata initial_data user_groups permissions notification
    4. Delete migration
            find . -path "*/migrations/*.py" -not -name "__init__.py" -delete && find . -path "*/migrations/*.pyc"  -delete
    5. Read and write from file
            pip freeze > r.txt
            pip install -r r.txt
            python manage.py loaddata initial_data user_groups permissions notification

    6. database export and import
            python manage.py dumpdata > database.json
            python manage.py loaddata database.json
