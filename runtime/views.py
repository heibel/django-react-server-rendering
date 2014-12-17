import json
import hashlib
import execjs

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import ListView

from .models import Component


def memoize(func):
    cache = {}
    
    def helper(cls, app, props):
        checksum = hashlib.md5(props).hexdigest()     
        if checksum not in cache:
            cache[checksum] = func(cls, app, props)

        return cache[checksum]
    
    return helper


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
    @memoize        
    def render_page(self, app, props):
        
        return self.runtime.eval(
            'require("render").renderServer("%s", %s)' % (app, props))


# Initialize our render class        
djangoReact = DjangoReact('runtime.js', 'runtime/js/')


class ComponentListView(ListView):
    model = Component
    react_app = "app"   # The 'exposed' app name

    def get_context_data(self, **kwargs):
        context = super(ComponentListView, self).get_context_data(**kwargs)

        props = serializers.serialize('json', self.object_list)
        app = self.react_app

        context.update({
            'var': djangoReact.render_page(app, props),
            'props': props,
        })
        
        return context
