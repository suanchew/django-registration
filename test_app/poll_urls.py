from django.conf.urls import include, url
from . import views

app_name = 'test_app'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index1'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail1'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results1'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote1'),
]



