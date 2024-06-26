from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        Receipe.objects.create(
            receipe_image= receipe_image,
            receipe_name= receipe_name,
            receipe_description = receipe_description,
        )
    return render(request, 'receipes.html',)