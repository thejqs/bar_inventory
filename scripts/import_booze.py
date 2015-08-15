# -------------- DJANGO IMPORTS
import csv
import os
import sys
import re
from django.contrib.auth.models import User

# --------------  APP IMPORTS
from main.models import BoozeType, Booze, BoozeDistillate

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bar_inventory.settings")

sys.path.append('..')

bar_inventory_csv = os.path.join(os.path.dirname(os.path.abspath('__file__')), "bar_inventory.csv")

csv_file = open(bar_inventory_csv, 'r')

reader = csv.DictReader(csv_file)

# BoozeType.objects.all().delete()
# Booze.objects.all().delete()
# BoozeDistillate.objects.all().delete()

user, created = User.objects.get_or_create(username='thejqs', password='thejqs')
for row in reader:
    new_booze_type, created = BoozeType.objects.get_or_create(name=row['type'])
    new_distillate, created = BoozeDistillate.objects.get_or_create(distillate=row['main_distillate'])
    new_booze, created = Booze.objects.get_or_create(
        user=user,
        style=row['style'],
        maker=row['maker'],
        bottle_label=row['bottle_label'],
        proof=None if not row['proof'] else int(row['proof']),
        easily_replaceable=False if row['easily_replaceable'] is 'N' else True,
        country_of_origin=row['country_of_origin'],
        booze_type=new_booze_type
    )
    Bottle.objects.create(booze=booze, was_gift=False)

csv_file.close()
