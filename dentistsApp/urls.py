from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create-user/$', views.create_user, name='create-user'),
    url(r'^create-dentist/$', views.create_dentist, name='create-dentist'),
    url(r'^user/(?P<user_id>[0-9]+)/$', views.user, name='user'),
    url(r'^dentist/(?P<dentist_id>[0-9]+)/$', views.dentist, name='dentist'),
    url(r'^dentist/(?P<dentist_id>[0-9]+)/patients/$', views.patients, name='patients'),
    url(r'^match/$', views.match, name='match'),
    url(r'^match/user/(?P<user_id>[0-9]+)/dentist/(?P<dentist_id>[0-9]+)/$', views.match_result, name='match-result'),
]
