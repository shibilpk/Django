 # Django

## Create a new project
### Create <project folder> and enter the folder
```
mkdir <project_name>
cd <project_name>
```

### Virtual environment

```
virtualenv venv
virtualenv venv -p python3
```

### Activate
```
source venv/bin/activate
```
### Make directory src then enter to  src

```
mkdir src
cd src
```
### Install django and create project

```
pip install django
pip install pillow psycopg2    (  psycopg2-binary  )
django-admin.py startproject  <project folder name>
```

### Change dir to  <project folder name>

```
cd <project folder name>
mkdir static media templates
python manage.py runserver
```



## Some initial configuration
### To activate virtualenv
```
source ../../venv/bin/activate
```
### To open python shell
```
python manage.py shell
```
### Create a new App
```
python manage.py startapp <app name>
```

### Start a new app
```
python manage.py startapp web
```

### Register in INSTALLED APPS

```
'web'
```

### Define template directory in TEMPLATES

```
'templates'
```

## Postgres database creation
### Create database and user in phppgadmin

```
sudo su postgres
createdb <dbname>
createuser shibil -P  (create only once next time grant privileges)
    eg:(femmepk -> shibil -> 12345)
psql
grant all privileges on database femmepk to shibil;
\q
exit
```


### in (setting.py)
```
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbname',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST':'localhost',
        'PORT': '',
    }
}

# Django latest
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
STATIC_URL = '/static/'
STATIC_FILE_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = (BASE_DIR / 'static',)
STATIC_ROOT = (BASE_DIR / 'static'/'static_files')
 ```

### Create super user
```
python manage.py createsuperuser
    (shibil -> shibil789)

```
### Migration comments
```
python manage.py makemigrations && python manage.py migrate
```
python manage.py loaddata initial_data user_groups permissions notification

### Delete migration
```
find . -path "*/migrations/*.py" -not -path "*/venv/*" -not -name "__init__.py" -delete && find . -path "*/migrations/*.pyc" -not -path "*/venv/*"  -delete
```

### Read and write from file
```
pip freeze > r.txt
pip install -r r.txt
```
### Database export and import
```
python manage.py dumpdata > database.json
python manage.py loaddata database.json
python manage.py dumpdata --exclude auth.permission --exclude contenttypes.contenttype --exclude sessions.session --exclude admin.logentry --indent 4 > data_base.json
```

