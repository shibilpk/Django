# To remane project
python manage.py rename demo new djecommerce

#to dumbdata with django default datas
python manage.py dumpdata --exclude auth.permission --exclude users.permission --exclude auth.user --exclude auth.group --exclude users.notificationsubject --exclude main.mode --exclude sessions.session --exclude contenttypes.contenttype --indent 2 > data.json
