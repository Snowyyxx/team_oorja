from django.shortcuts import render
from .models import Sponsors
# Create your views here.

def index(request):

    sponsors = Sponsors.objects.all()
    context = {'sponsors':sponsors}

    return render(request,'index.html',context)