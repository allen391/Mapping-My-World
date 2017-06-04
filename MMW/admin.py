from django.contrib import admin
from . import models

# Register your models here.


class UserInfoAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email']


class ContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email')
    search_fields = ('name', 'email')


class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')


class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'time')

admin.site.register(models.UserInfo, ContactAdmin)
admin.site.register(models.WhoIAm, ContentAdmin)
admin.site.register(models.Communication, ContentAdmin)
admin.site.register(models.WhoIAmHistory, HistoryAdmin)
admin.site.register(models.CommunicationHistory, HistoryAdmin)
admin.site.register(models.Program)
admin.site.register(models.WeeklySupport)
admin.site.register(models.Health)
admin.site.register(models.Activity)
admin.site.register(models.Short_term)
admin.site.register(models.Importance)
admin.site.register(models.Equipment)
admin.site.register(models.Wish)
admin.site.register(models.Long_term)
admin.site.register(models.Bulk_list)


admin.site.register(models.MyHome, ContentAdmin)


