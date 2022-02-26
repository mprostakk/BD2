from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import ListView

from vehicle.models import Vehicle


class VehicleListView(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = "vehicle/vehicle_list.html"
    context_object_name = "vehicle_list"
    queryset = Vehicle.objects.filter(Q(is_available_for_rent=True) & Q(battery_level__gte=15.0))
