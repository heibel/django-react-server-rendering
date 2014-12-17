from django.conf.urls import url

from .views import ComponentListView, ComponentListSimpleView

urlpatterns = [
    url(r'^react/', ComponentListView.as_view()),
    url(r'^simple/', ComponentListSimpleView.as_view()),
]