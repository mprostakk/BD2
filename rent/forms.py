from django.forms import ModelForm

from rent.models import Rent


class RentForm(ModelForm):
    class Meta:
        model = Rent
        fields = ["city"]
