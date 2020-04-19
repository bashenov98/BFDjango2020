from django.contrib import admin
from core.models import ToDoList, ToDo
# Register your models here.

@admin.register(ToDoList)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('name',  )


@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
