from django.contrib import admin
from .models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
  list_display = ['name','id','roll','city','passby']

admin.site.register(Student,StudentAdmin)
