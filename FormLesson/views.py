from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def func_lesson(request):
    errors = []
    form = {}

    if request.POST:
        form['name'] = request.POST.get('name')
        form['email'] = request.POST.get('email')
        form['message'] = request.POST.get('message')

        if not form['name']:
            errors.append('Введіть коректно ім`я')
        if '@' not in form['email']:
            errors.append('Введіть коректно емейл')
        if not form['message']:
            errors.append('Поле повідомлення не заповнено')

        if not errors:
            return HttpResponse('Дякую, ваше повідомлення заповнено')
    return render(request,'lesson.html',{'errors':errors, 'form':form},)