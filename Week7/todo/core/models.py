from django.db import models

# Create your models here.

from utils.constants import (TODO_STATUSES,
                             TODO_DONE,
                             TODO_IN_PROGRESS,
                             TODO_CURRENT,
                             TODO_NEW)

class ToDoList(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(default="")
    created_at = models.DateTimeField(auto_now=True)
    favorite = models.BooleanField(default=False)

    class Meta:
        verbose_name = "To do List"
        verbose_name_plural = "To do Lists"

    def __str__(self):
        return self.name

    @classmethod
    def show_favorites(cls):
        return ToDoList.objects.filter(favorite=True)


class ToDo(models.Model):
    name = models.CharField(max_length=150)
    list = models.ForeignKey(ToDoList, on_delete=models.CASCADE, related_name='tasks')
    status = models.PositiveSmallIntegerField(choices=TODO_STATUSES,
                                              default=TODO_NEW)

    class Meta:
        verbose_name = "todo"
        verbose_name_plural = "todos"

    def __str__(self):
        return self.name


class ToDoCategory(models.Model):
    name = models.CharField(max_length=100)
    todo = models.OneToOneField(ToDo, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class WorkToDo(ToDoCategory):
    pass

    class Meta:
        verbose_name = "Work to do"
        verbose_name_plural = "List of work to do"


class StudyToDo(ToDoCategory):
    pass

    class Meta:
        verbose_name = "Work to learn"
        verbose_name_plural = "List of work to learn"


# managers

class ToDoNewManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=TODO_NEW)

    def filter_by_status(self, status):
        return self.filter(status=status)

class ToDoDoneManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=TODO_DONE)

    def filter_by_status(self, status):
        return self.filter(status=status)



