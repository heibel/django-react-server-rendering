from django.conf.urls import url

from .views import ComponentListView, ComponentCreateView, ComponentUpdateView

urlpatterns = [
    url(r'^', ComponentListView.as_view(), name='component_list'),
    url(r'^create/', ComponentCreateView.as_view(), name='component_create'),
    url(r'^update/', ComponentUpdateView.as_view(), name='component_update'),
]