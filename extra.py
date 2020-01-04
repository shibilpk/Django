#add/change admin logo
    @ venv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/base_site.html
    <h1 id="site-name">
        <a href="{% url 'admin:index' %}">
            <img src="{% static 'umsra_logo.png' %}" height="40px" />
        </a>
    </h1>

# To remane project
    python manage.py rename demo new djecommerce

#to dumbdata with django default datas
    python manage.py dumpdata --exclude auth.permission --exclude users.permission --exclude auth.user --exclude auth.group --exclude users.notificationsubject --exclude main.mode --exclude sessions.session --exclude contenttypes.contenttype --indent 2 > data.json
