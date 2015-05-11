from django.contrib import admin
from iq_app.models import Solution, Registration

# Register your models here.

class RegistrationAdmin(admin.ModelAdmin):
	list_display = ('user','age')
	# list_display = ('firstname', 'username', 'email', 'password', 'age')


class SolutionAdmin(admin.ModelAdmin):
	list_display = ('serial_num', 'question', 'option1', 'option2', 'option3', 'option4', 'answer', 'uuid')


admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Solution, SolutionAdmin)
