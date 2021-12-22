from django.contrib import admin

from .models import User, Company, Address, Geo, Task

admin.site.register(User)
admin.site.register(Company)
admin.site.register(Address)
admin.site.register(Geo)
admin.site.register(Task)
# Register your models here.
