from django.contrib import admin

from tracker.models import Habit, HabitDay


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    pass


@admin.register(HabitDay)
class HabitDayAdmin(admin.ModelAdmin):
    pass

