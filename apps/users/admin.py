from django.contrib import admin
from apps.users.models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('password',)


admin.site.register(User, UserAdmin)
