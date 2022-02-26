from django.forms import ModelForm

from city.models import City, Zone


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ["name"]


class ZoneForm(ModelForm):
    class Meta:
        model = Zone
        fields = ["city", "zone_name", "geometry"]
