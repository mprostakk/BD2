from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView

from report.forms import FaultReportForm
from report.models import FaultReport
from vehicle.models import Vehicle


class FaultReportView(LoginRequiredMixin, FormView):
    template_name = "report/report.html"
    form_class = FaultReportForm
    success_url = reverse_lazy("vehicle-list")

    def form_valid(self, form: FaultReportForm):
        report: FaultReport = form.save(commit=False)

        report.user = self.request.user
        report.vehicle = get_object_or_404(Vehicle, pk=self.kwargs.get("pk"))

        report.save()
        messages.success(self.request, "Success adding fault report")
        return super().form_valid(form)
