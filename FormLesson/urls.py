from django.conf.urls import url
from FormLesson.views import func_lesson

app_name = 'lesson'
urlpatterns = [
    url(r'^contact/$', func_lesson, name='form_send'),

]