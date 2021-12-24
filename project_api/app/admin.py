from django.contrib import admin

from .models import User, Address, Task

admin.site.register(User)
admin.site.register(Address)
admin.site.register(Task)
# Register your models here.
