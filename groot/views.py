from django.shortcuts import render
from .models import Publication, Register
# Create your views here.

def home(request):

    #publications = Publication.objects.all()
    register = Register.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')

        if name and email:
            Register.objects.create(
                name = name, email = email
            )
        return render(request, 'layout.html', {'register': register})

    #TODO: WRITE CODE TO ACCEPT POST REQUEST TO REGISTER EMAILS

    return render(request, 'layout.html', {'register': register})
