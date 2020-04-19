from django.db import models
import datetime
# Create your models here.

class BookJournalBase(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    description = models.TextField()
    created_at = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

# class BookManager(models.Manager):


class Book(BookJournalBase):
    numpages = models.FloatField()
    genre = models.CharField(max_length=30)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class Journal(BookJournalBase):
    BULLET = 1
    FOOD = 2
    TRAVEL = 3
    SPORT = 4
    TYPES = (
        (BULLET, 'bullet'),
        (FOOD, 'food'),
        (TRAVEL, 'travel'),
        (SPORT, 'sport'),
    )
    type = models.PositiveSmallIntegerField(choices=TYPES, default=BULLET)
    publisher = models.CharField(max_length=30)


    objects = models.Manager()

    class Meta:
        verbose_name = 'Journal'
        verbose_name_plural = 'Journals'

