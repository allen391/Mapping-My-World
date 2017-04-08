from django.contrib import admin
from . import models

# Register your models here.


# class UserInfoAdmin(admin.ModelAdmin):
#     search_fields = ['name', 'email']

class ContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email')
    search_fields = ('name', 'email')

admin.site.register(models.UserInfo, ContactAdmin)
admin.site.register(models.WhoIAm)
admin.site.register(models.Communication)


