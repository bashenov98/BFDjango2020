from django.contrib import admin
from core.models import ToDoList, ToDo, ToDoCategory, WorkToDo, StudyToDo
# Register your models here.

@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('name',  )


@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )

@admin.register(ToDo)
class ToDoCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )

@admin.register(ToDo)
class WorkToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )

@admin.register(ToDo)
class StudyToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
