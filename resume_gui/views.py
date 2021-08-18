from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactModelForm
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def home_view(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)

        if form.is_valid():
            return render(request, 'base.html', {"message": "Your request has been posted"})
    else:
        form = ContactModelForm()
    return render(request, 'base.html', {'form': form})
