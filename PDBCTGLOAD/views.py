from django.shortcuts import render


# Create your views here.
def Base(request):
    return render(request, 'base.html')
    

def Contact(request):
    return render(request, 'contact.html')

