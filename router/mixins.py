import json
import requests
import zerorpc

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

        return ['router/base_react.html', ]

    def get_context_data(self, **kwargs):
        """
        We want to render our JSON to out template
        """
        context = super(ReactServerMixin, self).get_context_data(**kwargs)
        
        props = serializers.serialize('json', self.object_list)
        path = self.request.path
        
        payload = {
            'props': props,
        }
        
        content = None
        request = None  
        error = True
        
        # try:
        #     request = requests.get(NODE_URL + path, params=payload)
        #     content = request.content
        # except ConnectionError as e:
        #     error = e

        c = zerorpc.Client()
        c.connect("tcp://127.0.0.1:4242")

        content = c.render(path, props)


        context.update({
            'var': content if content else error,
            'props': props,
        })
        
        return context

    def render_to_response(self, context, **response_kwargs):
        """
        More rendering logic?
        """
        response = super(ReactServerMixin, self).render_to_response(context, **response_kwargs)

        return response