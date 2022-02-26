from django.urls import path

from rating import views

urlpatterns = [
    path("<pk>", views.RatingView.as_view(), name="rating"),
]
