from django.urls import path

from vehicle import views

urlpatterns = [
    path("", views.VehicleListView.as_view(), name="vehicle-list"),
]
