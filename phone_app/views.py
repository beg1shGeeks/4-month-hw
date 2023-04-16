from django.shortcuts import render, get_object_or_404
from . import models
# Create your views here.


def PhoneView(request):
    phones = models.Phone.objects.all()
    context = {
        'phone_objects': phones
    }
    return render(request, 'phone_list.html', context)


def PhoneDetailView(request, id):
    phone_id = get_object_or_404(models.Phone, id=id)
    context = {
        'phone_id': phone_id
    }
    return render(request, 'phone_detail.html', context)