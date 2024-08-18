from django.shortcuts import render, redirect
from django.views import View
from .forms import MuscleGroupForm, EquipmentForm, ExerciseForm
from .models import MuscleGroup, Equipment, Exercise


def home(request):
    return render(request, 'dailydoseapp/templates/home.html')


class SelectMuscleGroupView(View):
    def get(self, request):
        form = MuscleGroupForm()
        return render(request, 'select_muscle_groups.html', {'form': form})

    def post(self, request):
        form = MuscleGroupForm(request.POST)
        if form.is_valid():
            muscle_groups = form.cleaned_data['muscle_groups']
            request.session['muscle_groups'] = [mg.id for mg in muscle_groups]
            return redirect('select_equipment')
        return render(request, 'select_muscle_groups.html')


class SelectEquipmentView(View):
    def get(self, request):
        form = EquipmentForm()
        return render(request, 'select_equipment.html', {'form': form})

    def post(self, request):
        form = EquipmentForm(request.POST)
        if form.is_valid():
            equipment = form.cleaned_data['equipment']
            request.session['equipment'] = [eq.id for eq in equipment]
            return redirect('select_exercises')
        return render(request, 'select_equipment.html')


class SelectExercisesView(View):
    def get(self, request):
        muscle_group_ids = request.session.get('muscle_groups', [])
        equipment_ids = request.session.get('equipment', [])
        form = ExerciseForm(
            muscle_groups=MuscleGroup.objects.filter(id__in=muscle_group_ids),
            equipment=Equipment.objects.filter(id__in=equipment_ids)
        )
        return render(request, 'select_exercises.html', {'form': form})

    def post(self, request):
        muscle_group_ids = request.session.get('muscle_groups', [])
        equipment_ids = request.session.get('equipment', [])
        form = ExerciseForm(request.POST,
                            muscle_groups=MuscleGroup.objects.filter(id__in=muscle_group_ids),
                            equipment=Equipment.objects.filter(id__in=equipment_ids)
                            )
        if form.is_valid():
            selected_exercises = form.cleaned_data['name']
            request.session['selected_exercises'] = [ex.id for ex in selected_exercises]
            return redirect('display_exercises')
        return render(request, 'select_exercises.html', {'form': form})


class DisplayExercisesView(View):
    def get(self, request):
        selected_exercises_ids = request.session.get('selected_exercises', [])
        exercises = Exercise.objects.filter(id__in=selected_exercises_ids)
        return render(request, 'display_exercises.html', {'exercises': exercises})
