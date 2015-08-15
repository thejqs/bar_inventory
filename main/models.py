from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Booze(models.Model):
    user = models.ForeignKey(User)
    style = models.CharField(max_length=255)
    maker = models.CharField(max_length=100, blank=True, null=True)
    country_of_origin = models.CharField(max_length=80, blank=True, null=True)
    proof = models.IntegerField(blank=True, null=True)
    tasting_notes = models.TextField(blank=True, null=True)
    bottle_label = models.CharField(max_length=255, blank=True, null=True)
    easily_replaceable = models.BooleanField()
    booze_type = models.ForeignKey('BoozeType')
    favorites = models.ManyToManyField(User, related_name='favorites', blank=True)

    @property
    def total_bottles(self):
        return self.bottle_set.count()

    def __unicode__(self):
        return self.style


class Bottle(models.Model):
    MILLILITER_CHOICE = 2
    SIZE_CHOICES = (
            (0, 'ounces'),
            (1, 'liters'),
            (MILLILITER_CHOICE, 'milliliters')
        )

    location = models.ForeignKey('Location', blank=True, null=True)
    release_year = models.DateTimeField(blank=True, null=True)
    was_gift = models.BooleanField()
    date_acquired = models.DateTimeField(blank=True, null=True)
    date_finished = models.DateTimeField(blank=True, null=True)
    bottle_size = models.FloatField(blank=True, null=True)
    size_unit = models.IntegerField(default=MILLILITER_CHOICE, choices=SIZE_CHOICES, blank=True, null=True)
    booze = models.ForeignKey('Booze')
    image = models.ImageField(upload_to='booze_images', blank=True, null=True)

    def __unicode__(self):
        # storage_type = self.location.storage_type
        # size_unit_string = SIZE_CHOICES[self.size_unit][1]
        booze_name = self.booze.booze_type.name

        return "bottle of %s" % (
            # self.bottle_size, 
            # size_unit_string, 
            booze_name, 
            # storage_type,
        )


class BoozeType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class BoozeDistillate(models.Model):
    distillate = models.CharField(max_length=40, blank=True, null=True)

    def __unicode__(self):
        return self.distillate


# class BoozeShopping(models.Model)
    # shopping_list = models.ForeignKey('Bottle')
    # replacement_bottle = models.ForeignKey()
    # new_bottle = models.CharField()
    # price_change = models.FloatField()
    # date_added = models.DateTimeField()
    # date_modified = models.DateTimefield()
    # notes = models.TextField()


class Location(models.Model):
    floor = models.CharField(max_length=12, unique=True)
    storage_type = models.CharField(max_length=40, blank=True, null=True)
    shelf = models.CharField(max_length=20, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.storage_type
