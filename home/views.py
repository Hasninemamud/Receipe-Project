from django.shortcuts import render

# Create your views here.
def home(request):
    peoples = [
        {'name': 'Hasnine', 'age': 24},
        {'name': 'Mamud', 'age': 20},
        {'name': 'Hemel', 'age': 22},
        {'name': 'Yean', 'age': 12},
        {'name': 'Partho', 'age': 14},
    ]
    return render(request,"Home/index.html", context={'page':'home','peoples':peoples })


def contact(request):
    context = {'page':'contact'}
    return render(request,"Home/contact.html", context)



def about(request):
    context = {'page':'About'}
    return render(request,"Home/about.html",context )