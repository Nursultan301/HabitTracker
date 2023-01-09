from django.db import models


class HabitDay(models.Model):
    days = models.TextField()

    def __str__(self):
        return self.days


class Habit(models.Model):
    """Привычка"""
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)
    target = models.PositiveSmallIntegerField()
    days = models.ManyToManyField(HabitDay, related_name='days_set')

    def __str__(self):
        return self.title
