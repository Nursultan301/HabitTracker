from rest_framework import serializers

from .models import Habit, HabitDay


class HabitListSerializer(serializers.ModelSerializer):
    """ Список привычки """

    class Meta:
        model = Habit
        fields = ('id', 'icon', 'title', 'target')


class HabitDaySerializer(serializers.ModelSerializer):
    """ Список привычки """
    days = serializers.SlugRelatedField(slug_field="days", read_only=True, many=True)

    class Meta:
        model = Habit
        fields = ('id', 'icon', 'title', 'target', 'days')


class HabitSerializer(serializers.ModelSerializer):
    """ Добавление привычки """

    class Meta:
        model = Habit
        fields = ("title", "target", "icon")
