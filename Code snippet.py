
# For Filter with Custom name ,in admin.py 
def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
	def __new__(cls, *args, **kwargs):
	    instance = admin.FieldListFilter.create(*args, **kwargs)
	    instance.title = title
	    return instance
    return Wrapper

class RegistrationAdmin(admin.ModelAdmin):
	list_display = ('id','name','email','phone','dob','message')
	ordering = ('name',)

	list_filter = (
    ('name', custom_titled_filter('Name')),
    'email',
	)

admin.site.register(Registration,RegistrationAdmin)


# Add/change admin logo
@ venv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/base_site.html
<h1 id="site-name">
    <a href="{% url 'admin:index' %}">
        <img src="{% static 'umsra_logo.png' %}" height="40px" />
    </a>
</h1>