from django.shortcuts import render

# Create your views here.

from base import models as base_models
from doctor import models as doctor_models
from patient import models as patient_models


def index(request):
    services = base_models.Service.objects.all()
    context = {
        "services": services
    }
    return render(request, "base/index.html", context)


def service_detail(request, service_id):
    service = base_models.Service.objects.get(id=service_id)
    context = {
        "service": service
    }
    return render(request, "base/service_detail.html", context)
