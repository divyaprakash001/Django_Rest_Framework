from django.contrib import admin
from .models import Singer,Song


# Register your models here.
class SingerAdmin(admin.ModelAdmin):
  list_display = ['name','id','gender']

class SongAdmin(admin.ModelAdmin):
  list_display = ['title','duration','singer__name']

admin.site.register(Singer,SingerAdmin)
admin.site.register(Song,SongAdmin)
