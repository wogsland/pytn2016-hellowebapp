from django.shortcuts import render, redirect
from collection.forms import ThingForm
from collection.models import Thing

# Create your views here.
def index(request):
    munber = 6
    thing = "Thinnged Nam"
    things = Thing.objects.all()
    thing_one = Thing.objects.get(name="thing one")
    things_named_thing = Thing.objects.filter(name__contains='thing').order_by('?')
    return render(request, 'index.html', {
        'munber': munber,
        'single': 1,
        'thing': thing,
        'things':things,
        'uno': thing_one,
        'things_named_thing': things_named_thing,
    })

def thing_detail(request, slug):
    # grab the object...
    thing = Thing.objects.get(slug=slug)
    # and pass to the template
    return render(request, 'things/thing_detail.html', {
        'thing': thing,
    })

def edit_thing(request, slug):
    thing = Thing.objects.get(slug=slug)
    form_class = ThingForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=thing)
        if form.is_valid():
            form.save()
            return redirect('thing_detail', slug=thing.slug)
    else:
        form = form_class(instance=thing)
    return render(request, 'things/edit_thing.html', {
        'thing': thing,
        'form': form,
    })
