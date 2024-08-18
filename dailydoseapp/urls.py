from django.urls import path
from . import views
from .views import SelectMuscleGroupView, SelectEquipmentView, SelectExercisesView, DisplayExercisesView

urlpatterns = [
    path('', views.home, name='home'),
    path('select-muscle-groups/', SelectMuscleGroupView.as_view(), name='select_muscle_groups'),
    path('select-equipment/', SelectEquipmentView.as_view(), name='select_equipment'),
    path('select-exercises/', SelectExercisesView.as_view(), name='select_exercises'),
    path('display-exercises/', DisplayExercisesView.as_view(), name='display_exercises'),
]
