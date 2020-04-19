from django.db import models
from auth_.models import CustomUser
import datetime
# Create your models here.

class ToDoListManager(models.Manager):

    def for_user(self, user):
        return self.filter(owner=user)

class ToDoList(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    objects = ToDoListManager()

    class Meta:
        verbose_name = 'Лист заданий'
        verbose_name_plural = 'Листы заданий'

    def __str__(self):
        return self.name

class ToDo(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    due_on = models.DateTimeField(null=True, default=None)
    is_done = models.BooleanField(default=False)
    list = models.ForeignKey(ToDoList, on_delete=models.CASCADE, related_name='tasks')
    notes = models.CharField(max_length=255, default='', blank=True)

    objects = ToDoListManager()

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.name
