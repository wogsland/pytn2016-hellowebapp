from django.shortcuts import render

# Create your views here.
def index(request):
    munber = 6
    return render(request, 'index.html', {
        'munber': munber,
        'single': 1,
        'thing': 'velvet worms',
    })
