from django.conf.urls import url

from .views import ComponentListView

urlpatterns = [
    url(r'^react/', ComponentListView.as_view()),
]