import json
import requests

from django.core import serializers
from django.http import HttpResponse
from django.views.generic import ListView
from requests.exceptions import ConnectionError

from .settings import NODE_URL
from .models import Component
from .mixins import ReactServerMixin


class ComponentListView(ReactServerMixin, ListView):
    model = Component
    react_component = 'component_list.jsx'
    react_props = {}


class ComponentListSimpleView(ListView):
    model = Component
    template_name = 'component/base_react.html'

    def get_context_data(self, **kwargs):
        context = super(ComponentListSimpleView, self).get_context_data(**kwargs)
        context.update({
            'var': '',
            'props': serializers.serialize('json', self.object_list),
        })
        
        return context