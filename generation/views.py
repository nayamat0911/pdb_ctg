from django.shortcuts import render

# Create your views here.
def Generation_Disply(request):
    return render(request, 'gendisply.html')

def Generation_11AM(request):
    return render(request, 'generation_1100Hr.html')

def Generation_19PM(request):
    return render(request, 'generation_1900Hr.html')

def Generation_33kv(request):
    return render(request, 'hourly_33kv_gen.html')

def Generation_page_link(request):
    return render(request, 'generation_page_link.html')