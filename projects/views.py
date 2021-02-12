from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {'message': 'success'}
    return render(request, 'projects/index.html', context=context)
