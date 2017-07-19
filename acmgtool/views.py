from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import codeForms
from .acmg_calc import main as acmg


# Create your views here.


def index(request):
    if request.method == 'POST':
        selected = request.POST.getlist('checks')
        selected = acmg(selected)
        return render(request, 'acmgtool/acmg.html', {'checks': selected})


    return render(request, 'acmgtool/acmg.html')

