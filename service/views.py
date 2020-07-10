from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.timezone import now

from service.forms import AddFeedbackForm
from service.models import Slider, Service, Gallery, Feedback, ServiceCategory


def index(request):
    form = AddFeedbackForm()
    if request.method == 'POST':
        form = AddFeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f"{reverse('service:index')}#feedback")
        else:
            form = AddFeedbackForm(initial={'fio': 'request',
                                            'add_datetime': now()
                                            })
    context = {
        'title': 'Автосервис',
        'sliders': Slider.objects.all(),
        'services': Service.objects.all(),
        'categories': ServiceCategory.objects.all(),
        'gallery': Gallery.objects.filter(category="COMMON"),
        'staffs': Gallery.objects.filter(category="STAFF"),
        'feedbacks': Feedback.objects.all(),
        'form': form,
    }

    return render(request, 'service/index.html', context)
