from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'special_message': "Now I've got context"
    }
    return render(request, 'index.html', context)