import json
import requests

from django.core import serializers
from django.http import HttpResponse
from requests.exceptions import ConnectionError

from .settings import NODE_URL

class ReactServerMixin(object):

    def get_template_names(self):
        """
        Override all templates with our React base template
        """
        if not self.template_name is None:
            return [self.template_name, ]

        return ['component/base_react.html', ]

    def get_context_data(self, **kwargs):
        """
        We want to render our JSON to out template
        """
        context = super(ReactServerMixin, self).get_context_data(**kwargs)
        
        props = serializers.serialize('json', self.object_list)
        
        payload = {
            'component': self.react_component,
            'props': props,
        }
        
        request = None
        error = None
        
        try:
            request = requests.get(NODE_URL, params=payload)
        except ConnectionError as e:
            error = e

        context.update({
            'var': (error if error else request.content),
            'props': props,
        })
        
        return context

    def render_to_response(self, context, **response_kwargs):
        """
        More logic for rendering?
        """
        response = super(ReactServerMixin, self).render_to_response(context, **response_kwargs)

        return response