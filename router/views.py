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
    template_name = 'router/base_react.html'
    react_props = {}


class ComponentListSimpleView(ListView):
    model = Component
    template_name = 'router/base_react.html'
    
    def get_context_data(self, **kwargs):
        """
        We want to render our JSON to out template
        """
        context = super(ComponentListSimpleView, self).get_context_data(**kwargs)

        props = serializers.serialize('json', self.object_list)

        context.update({
            'var': '',
            'props': props,
        })
        
        return context