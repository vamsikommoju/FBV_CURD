from django.contrib import admin
from app1.models import *
# Register your models here.


@admin.register(Persons)
class Personsadmin(admin.ModelAdmin):
    list_display=['name','age','gender','phno']


