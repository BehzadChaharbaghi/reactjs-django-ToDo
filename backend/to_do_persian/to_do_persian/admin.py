from django.contrib import admin
from .models import Todo
# Register your models here.


class Todoadmin(admin.ModelAdmin):
    list_display = ('title', 'descreption', 'completed')


admin.site.register(Todo, Todoadmin)