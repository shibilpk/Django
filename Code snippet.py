
#FOr Filter with Custom name ,in admin.py 
{{{{
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
}}}}
