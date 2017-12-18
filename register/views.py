from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader, RequestContext
from django.template.context_processors import csrf
from django.contrib.auth import login, authenticate

from register.forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('base.html')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def log(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            args['login_error'] = 'Логін введено невірно.'
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def index(request):
    return render_to_response( {'username': auth.get_user(request).username})

def index1(request):
    return render_to_response('navbar.html', {'username': auth.get_user(request).username})


# не працює


# def index(request):
#     template = loader.get_template('base.html')
#     c = {
#         'username': auth.get_user(request).username
#     }
#     return HttpResponse(template.render(c, request))

# def index(request):
#     template = loader.get_template('base.html')
#     c = RequestContext(request,{
#         'username': auth.get_user(request).username
#     })
#     return HttpResponse(template.render(c, request))