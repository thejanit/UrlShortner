from django.shortcuts import redirect, render
from .models import Shortner
from .forms import Shortened_Form
import random
import string


# Create your views here.

def urlshort(request):
    template = 'fuzzyurl/index.html'

    if request.method == 'POST':
        form = Shortened_Form(request.POST)

        if form.is_valid():
            short_url = ''.join(random.choice(string.ascii_letters)
                           for x in range(10))
            original_url = form.cleaned_data["original_url"]
            new_url = Shortner(original_url=original_url, short_url=short_url)
            new_url.save()
            request.urlshort.add(new_url)
            return redirect('/')

    else:
        form = Shortened_Form()
    data = Shortner.objects.all()
    context = {
        'form': form,
        'data': data
    }
    return render(request, template, context)


def redirect_url(request, slugs):
    data = Shortner.objects.get(short_url=slugs)
    return redirect(data.original_url)
