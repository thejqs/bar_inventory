# -------------- DJANGO IMPORTS
from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

import django.contrib.auth.views

from main.views import BoozeDetailView, AddBoozeForm

urlpatterns = [
    # url(r'^$', 'main.views.initial', name='initial'),
    # url(r'^login/$', 'main.views.login', name='login'),
    # url(r'^logout/$', 'main.views.logout', name='logout'),
    url(r'^add-booze/$', 'main.views.add_booze', name='add_booze'),
    # url(r'^booze/$', 'main.views.booze', name='booze'),
    url(r'^booze-search/$', 'main.views.search_booze', name='search_booze'),
    url(r'^booze/(?P<pk>[0-9]+)/$', BoozeDetailView.as_view(), name='booze_detail'),

]
