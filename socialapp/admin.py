from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User, Group

class UserAdmin(admin.ModelAdmin):
    model = User
    # Only display the "username" field
    fields = ["username"]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
