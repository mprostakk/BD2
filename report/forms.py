from django.forms import ModelForm

from report.models import FaultReport


class FaultReportForm(ModelForm):
    class Meta:
        model = FaultReport
        fields = ["malfunction_type", "description"]
