
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

#Pagination
def get_paginated_url(request,kwargs):
    query = request.GET.copy()
    for key in kwargs:
        query[key] = kwargs[key]
    return f"{request.build_absolute_uri(request.path)}?{query.urlencode()}"

get_paginated_url(request,{'page':instances.previous_page_number()})
