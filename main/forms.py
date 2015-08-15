# -------------- DJANGO IMPORTS
from django import forms
from django.forms import ModelForm

# -------------- APP IMPORTS
from main.models import BoozeType, Booze, BoozeDistillate, Bottle, Location


class AddBoozeForm(forms.Form):
    booze_type = forms.ModelChoiceField(required=True,
                                        queryset=BoozeType.objects.all(),
                                        widget=forms.Select,
                                        )

    style = forms.CharField(required=False, label="Style (examples: Rye, London Dry)")

    maker = forms.CharField(required=False, label="Maker (examples: Laphroaig, Maggie's Farm)",
                            widget=forms.TextInput,
                            )

    bottle_label = forms.CharField(required=False,
                                        max_length=255,
                                        widget=forms.TextInput,
                                        )

    country_of_origin = forms.CharField(required=False,
                                        widget=forms.TextInput,
                                        )

    proof = forms.IntegerField(required=False,
                            widget=forms.NumberInput,
                            )

    # tasting_notes = forms.CharField(required=False,
    #                                 widget=forms.Textarea,
    #                                 )

    easily_replaceable = forms.NullBooleanField(required=False,
                                            widget=forms.NullBooleanSelect,
                                            )


class AddBottleForm(forms.Form):
    location = forms.CharField
    release year = forms.IntegerField
    was_gift = forms.NullBooleanField
    date_acquired = forms.DateTimeField
    date_finished = forms.DateTimeField
    bottle_size = forms.FloatField
    size_unit = forms.ChoiceField




    # mark_as_favorite = forms.


# class NewBoozeTypeForm(forms.Form):
#     name = forms.CharField(required=True,
#                             widget=forms.TextInput,
#                             )
#     main_distillate = forms.CharField(required=False,
#                                         widget=forms.TextInput,
#                                         )
#     description = forms.CharField(required=False,
#                                         widget=forms.Textarea)
