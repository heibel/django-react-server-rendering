from django.conf.urls import url

from .views import ComponentListView

urlpatterns = [
    url(r'^', ComponentListView.as_view()),
]