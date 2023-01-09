from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .views import HabitViewSet

urlpatterns = format_suffix_patterns([
    path('tracker/', HabitViewSet.as_view({'get': 'list'})),
    path('tracker/<int:pk>/', HabitViewSet.as_view({'get': 'retrieve'})),
    path("tracker/add/", views.HabitCreateViewSet.as_view({'post': 'create'})),
])