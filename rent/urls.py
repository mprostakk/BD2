from django.urls import path

from rent import views

urlpatterns = [
    path("", views.RentListView.as_view(), name="rent-list"),
    path("add/<pk>", views.RentCreateView.as_view(), name="rent-add"),
    path("end/<pk>", views.RentEndView.as_view(), name="rent-end"),
    path("break/start/<pk>", views.RentBreakStartView.as_view(), name="rent-break-start"),
    path("break/end/<pk>", views.RentBreakEndView.as_view(), name="rent-break-end"),
]
