from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.student_list, name='student_list'),
    url(r'^(?P<s_pk>\d+)/$', views.student_del, name='student_del')
]
