from django.contrib import admin
from .models import tweet
from django.contrib.auth.models import Group,User



admin.site.unregister(Group)
# Register your models here.
admin.site.register(tweet)




class UserAdmin(admin.ModelAdmin):
    model=User
    fields=["username"]



admin.site.unregister(User)

admin.site.register(User,UserAdmin)
