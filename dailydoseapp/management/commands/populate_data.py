from django.core.management.base import BaseCommand
from dailydoseapp.models import MuscleGroup, Equipment, Exercise


class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **kwargs):

        # Muscle Groups
        # Chest
        chest, created = MuscleGroup.objects.get_or_create(name='Chest')
        upper_chest, created = MuscleGroup.objects.get_or_create(name='Upper Chest')
        mid_chest, created = MuscleGroup.objects.get_or_create(name='Mid Chest')
        lower_chest, created = MuscleGroup.objects.get_or_create(name='Lower Chest')
        # Back
        back, created = MuscleGroup.objects.get_or_create(name='Back')
        upper_back, created = MuscleGroup.objects.get_or_create(name='Upper Back / Traps')
        lats, created = MuscleGroup.objects.get_or_create(name='Lats')
        lower_back, created = MuscleGroup.objects.get_or_create(name='Lower Back')
        # Shoulders
        shoulders, created = MuscleGroup.objects.get_or_create(name='Shoulders')
        front_delt = MuscleGroup.objects.get_or_create(name='Front Delt')
        side_delt, created = MuscleGroup.objects.get_or_create(name='Side Delt')
        rear_delt, created = MuscleGroup.objects.get_or_create(name='Rear Delt')
        # Legs
        legs, created = MuscleGroup.objects.get_or_create(name='Legs')
        quads, created = MuscleGroup.objects.get_or_create(name='Quads')
        hamstrings, created = MuscleGroup.objects.get_or_create(name='Hamstrings')
        glutes, created = MuscleGroup.objects.get_or_create(name='Glutes')
        calves, created = MuscleGroup.objects.get_or_create(name='Calves')
        # Arms
        arms, created = MuscleGroup.objects.get_or_create(name='Arms')
        biceps, created = MuscleGroup.objects.get_or_create(name='Biceps')
        triceps, created = MuscleGroup.objects.get_or_create(name='Triceps')
        forearms, created = MuscleGroup.objects.get_or_create(name='Forearms')
        # Core
        core, created = MuscleGroup.objects.get_or_create(name='Core')

        # Equipment
        gym, created = Equipment.objects.get_or_create(name='In Gym / All')
        dumbbells, created = Equipment.objects.get_or_create(name='Dumbbells')
        bench, created = Equipment.objects.get_or_create(name='Bench')
        barbell, created = Equipment.objects.get_or_create(name='Barbell')
        kettlebell, created = Equipment.objects.get_or_create(name='Kettlebell')
        squat_rack, created = Equipment.objects.get_or_create(name='Squat Rack')
        ez_bar, created = Equipment.objects.get_or_create(name='Ez Bar')
        cable, created = Equipment.objects.get_or_create(name='Cable')
        smith_machine, created = Equipment.objects.get_or_create(name='Smith Machine')
        other_machine, created = Equipment.objects.get_or_create(name='Other Machines')

        # Exercises
        dumbbell_bench_press, created = Exercise.objects.get_or_create(name='Dumbbell Bench Press')
        dumbbell_bench_press.muscle_groups.set([mid_chest])
        dumbbell_bench_press.equipment.set([bench, barbell])
        dumbbell_incline_bench_press, created = Exercise.objects.get_or_create(name='Incline Dumbbell Bench Press')
        dumbbell_incline_bench_press.muscle_groups.set([upper_chest])
        dumbbell_incline_bench_press.equipment.set([bench, barbell])
        dumbbell_decline_bench_press, created = Exercise.objects.get_or_create(name='Decline Dumbbell Bench Press')
        dumbbell_decline_bench_press.muscle_groups.set([lower_chest])
        dumbbell_decline_bench_press.equipment.set([bench, barbell])
        dumbbell_chest_fly, created = Exercise.objects.get_or_create(name='Chest Fly')
        dumbbell_chest_fly.muscle_groups.set([mid_chest])
        dumbbell_chest_fly.equipment.set([cable])

        self.stdout.write(self.style.SUCCESS('Database populated successfully'))
