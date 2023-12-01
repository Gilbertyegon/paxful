from django.contrib import admin

from .models import Logins

# Register your models here.
class LoginsAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'ip', 'codes')

admin.site.register(Logins, LoginsAdmin)