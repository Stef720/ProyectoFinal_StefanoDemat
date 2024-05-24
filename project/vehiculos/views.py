from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

# Create your views here.
from . import models, forms


def home(request):
    consulta_vehiculos = models.Vehiculo.objects.all()
    context = {"vehiculos": consulta_vehiculos}
    return render(request, "vehiculo/index.html", context)