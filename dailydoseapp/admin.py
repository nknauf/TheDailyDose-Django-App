from django.contrib import admin


class MuscleGroupAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    filter_horizontal = ['muscle_groups', 'equipment']


def register_models():
    from .models import MuscleGroup, Exercise, Equipment
    admin.site.register(MuscleGroup, MuscleGroupAdmin)
    admin.site.register(Equipment, EquipmentAdmin)
    admin.site.register(Exercise, ExerciseAdmin)


register_models()
