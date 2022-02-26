from django.urls import path

from city import views

urlpatterns = [
    path("", views.CityView.as_view(), name="city"),
    path("zone", views.ZoneView.as_view(), name="zone"),
]
