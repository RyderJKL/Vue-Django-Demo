from django.conf.urls import url
from backend import views as backend_views

urlpatterns = [
    url(r'^$', backend_views.index, name='index')
]
