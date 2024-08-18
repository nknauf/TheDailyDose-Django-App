from django import forms
from .models import MuscleGroup, Equipment, Exercise


class MuscleGroupForm(forms.Form):
    muscle_groups = forms.ModelMultipleChoiceField(
        queryset=MuscleGroup.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Select Muscle Groups"
    )


class EquipmentForm(forms.Form):
    equipment = forms.ModelMultipleChoiceField(
        queryset=Equipment.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Select Equipment"
    )


class ExerciseForm(forms.Form):
    name = forms.ModelMultipleChoiceField(
        queryset=Exercise.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        label="Select Exercises"
    )

    def __init__(self, *args, **kwargs):
        muscle_groups = kwargs.pop('muscle_groups', None)
        equipment = kwargs.pop('equipment', None)
        super(ExerciseForm, self).__init__(*args, **kwargs)
        if muscle_groups and equipment:
            self.fields['name'].queryset = (Exercise.objects.filter(muscle_groups__in=muscle_groups,
                                                                    equipment__in=equipment).distinct())
