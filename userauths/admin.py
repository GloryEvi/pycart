from django.contrib import admin
from userauths import models

admin.site.register(models.User)
admin.site.register(models.Profile)

# Register your models here.
