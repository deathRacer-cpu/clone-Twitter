from django.contrib import admin
from django.contrib.auth.models import Group,User
from .models import Profile



# Register your models here.
admin.site.register(profile)

class UserAdmin(admin.ModelAdmin):
    model=User
    fields=["username"]



admin.site.unregister(User)

admin.site.register(User,UserAdmin)
admin.site.register(User, UserAdmin)


