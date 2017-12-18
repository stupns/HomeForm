from django.conf.urls import url
from AppForm.views import new_mess, mess_detail,edit_mess, mess_list

app_name = 'forum'
urlpatterns = [
    url(r'^$', mess_list, name='mess_list'),
    url(r'^new/', new_mess, name='new_mess'),
    url(r'^message/(?P<pk>[0-9]+)/edit/', edit_mess, name='edit_mess'),
    url(r'^message/(?P<pk>[0-9]+)/$',mess_detail, name='mess_detail')
]