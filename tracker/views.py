from rest_framework import viewsets

from tracker.models import Habit
from tracker.serializer import HabitListSerializer, HabitDaySerializer, HabitSerializer


class HabitViewSet(viewsets.ReadOnlyModelViewSet):
    """ Вывод списки привычки  """

    def get_queryset(self):
        habit = Habit.objects.all()
        return habit

    def get_serializer_class(self):
        if self.action == 'list':
            return HabitListSerializer
        elif self.action == 'retrieve':
            return HabitDaySerializer


class HabitCreateViewSet(viewsets.ModelViewSet):
    """Добавление привычки"""
    serializer_class = HabitSerializer
