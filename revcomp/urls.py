from django.conf.urls import url
from . import views

app_name='revcomp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rcomp/$', views.rcomp, name='rcomp'),

]
