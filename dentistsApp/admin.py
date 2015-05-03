from django.contrib import admin

from .models import User
admin.site.register(User)

from .models import Dentist, User

class UserInline(admin.TabularInline):
    model = User
    extra = 5

class DentistAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'email', 'license_number']
    inlines = [UserInline]
    list_display = ('last_name', 'first_name', 'email', 'license_number')
    search_fields = ['last_name']

admin.site.register(Dentist, DentistAdmin)
