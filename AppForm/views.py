from django.shortcuts import render, get_object_or_404,redirect,render_to_response
from AppForm.models import Message
from AppForm.forms import MessageForm


def mess_list(request):
    go = Message.objects.all()
    return render_to_response('all.html', {'go':go})


def mess_detail(request, pk):
    mess = get_object_or_404(Message, pk=pk)
    return render(request, 'general.html', {'mess':mess})


def new_mess(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            mess = form.save(commit=False)
            mess.author = request.user
            mess.save()
            return redirect('forum:mess_detail', pk=mess.pk)
    else:
        form = MessageForm

    return render(request,'new_message.html', {'form': form})

def edit_mess(request, pk):
    mess = get_object_or_404(Message, pk=pk)
    if request.method == 'POST':
        form = MessageForm(request.POST, instance=mess)
        if form.is_valid():
            mess = form.save(commit=False)
            mess.author = request.user
            mess.save()
        return redirect('forum:mess_detail', pk=mess.pk)
    else:
        form = MessageForm(instance=mess)
    return render(request, 'new_message.html', {'form': form})

