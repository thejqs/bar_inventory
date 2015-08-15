# -------------- DJANGO IMPORTS
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.views.generic import View
from django.db.models import Sum

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView

from collections import OrderedDict

# -------------- APP IMPORTS
from main.models import Booze, BoozeType, BoozeDistillate, Bottle
from main.forms import AddBoozeForm #, NewBoozeTypeForm

# Create your views here.

# def initial():


# def login():


# def logout():


# def add_booze():


# def add_booze_type():


def add_booze(request):
    context = {}
    booze_dict = OrderedDict()
    # import ipdb; ipdb.set_trace()

    form = AddBoozeForm()
    context['form'] = form

    if request.method == 'POST':
        booze_type = form.cleaned_data['booze_type']
        style = form.cleaned_data['style']
        maker = form.cleaned_data['maker']
        country_of_origin = form.cleaned_data['country_of_origin']
        proof = form.cleaned_data['proof']
        tasting_notes = form.cleaned_data['tasting_notes']
        bottle_label = form.cleaned_data['bottle_label']
        easily_replaceable = form.cleaned_data['easily_replaceable']
        context['boozes'] = Booze.objects.filter(booze__booze_type=booze_type,
                                                    style=style,
                                                    maker=maker,
                                                    country_of_origin=country_of_origin,
                                                    proof=proof,
                                                    tasting_notes=tasting_notes,
                                                    bottle_label=bottle_label,
                                                    easily_replaceable=easily_replaceable
                                                )

    booze_types = BoozeType.objects.all()

    for booze in booze_types:
        all_booze = booze.booze_set.all()
        bottle_sum = Booze.total_bottles
        booze_dict[booze.name] = {'boozes': all_booze,
                                                    'bottles': bottle_sum,
                                                }

    context['booze_types'] = booze_dict

    context['all_booze'] = booze_types

    return render(request, 'add_booze.html', context)


class BoozeDetailView(DetailView):
    '''extending the boose search to return booze details'''
    model = Booze
    template_name = 'booze_detail.html'
    context_object_name = 'booze'

    # def get_booze_data():
    #     context = super(BoozeDetailView, self).get_booze_data(**kwargs)
    #     import ipdb; ipdb.set_trace()
    #     context['booze_types'] = BoozeTypes.objects.all()
    #     return context


def search_booze(request):
    context = {}
    request_context = RequestContext(request)

    if request.method == 'POST':
        form = AddBoozeForm(request.POST)
        context['form'] = form
        if form.is_valid():
            # booze_type = form.cleaned_data['booze_type']
            # style = form.cleaned_data['style']
            # maker = form.cleaned_data['maker']
            # country_of_origin = form.cleaned_data['country_of_origin']
            # easily_replaceable = form.cleaned_data['easily_replaceable']
            # # import ipdb; ipdb.set_trace()
            # proof = form.cleaned_data['proof']
            # bottle_label = form.cleaned_data['bottle_label']
            total_bottles = Booze.total_bottles

            # import ipdb; ipdb.set_trace()
            form.cleaned_data['booze_type__name'] = form.cleaned_data.pop('booze_type')

            non_empty_data = {key: value for key, value in form.cleaned_data.items() if value != None and value != ''}

            context['boozes'] = Booze.objects.filter(**non_empty_data)

            # Booze.objects.filter(booze_type__name=booze_type,
            #                                         style=style,
            #                                         maker=maker,
            #                                         country_of_origin=country_of_origin,
            #                                         proof=proof,
            #                                         # tasting_notes=tasting_notes,
            #                                         bottle_label=bottle_label,
            #                                         easily_replaceable=easily_replaceable
            #                                     )
            context['valid'] = "Here's that booze you wanted."

            return render_to_response('booze_search.html', context, context_instance=request_context)

        else:
            context['valid'] = form.errors

    else:
        form = AddBoozeForm()
        context['form'] = form

    return render_to_response('booze_search.html', context, context_instance=request_context)
