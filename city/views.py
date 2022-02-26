from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView

from city.forms import CityForm, ZoneForm


class CityView(LoginRequiredMixin, FormView):
    template_name = "city/city.html"
    form_class = CityForm
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Success adding City")
        return super().form_valid(form)


class ZoneView(LoginRequiredMixin, FormView):
    template_name = "city/zone.html"
    form_class = ZoneForm
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Success adding Zone")
        return super().form_valid(form)
