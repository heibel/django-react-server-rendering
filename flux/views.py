import json
import hashlib
import execjs

from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import ListView, CreateView, UpdateView

from .models import Component


class DjangoReact(object):
    """
    Expose bundled js-file to runtime
    """
    def __init__(self, local_bundle, bundle_url):
        with open(bundle_url + local_bundle, 'r') as f:
            self.runtime = execjs.compile(f.read())

    """
    Returns the rendered html
    """
    def render_page(self, app, props):
       
        return self.runtime.eval(
            'require("render").renderServer("%s", %s)' % (app, props))


# Initialize our render class        
djangoReact = DjangoReact('bundle.min.js', 'flux/static/js/')


class ComponentListView(ListView):
    model = Component
    react_app = "app"   # The 'exposed' app name

    def get_context_data(self, **kwargs):
        context = super(ComponentListView, self).get_context_data(**kwargs)

        props = serializers.serialize('json', self.object_list)
        app = self.react_app

        urls = {
            'create': reverse('flux:component_create'),
            'update': reverse('flux:component_update'),
        }

        try:
            var = djangoReact.render_page(app, props)
        except e:
            var = None

        context.update({
            'var': var,
            'props': props,
        })
        
        return context


class ComponentCreateView(CreateView):
    pass

class ComponentUpdateView(UpdateView):
    pass
