from django.urls import path

from report import views

urlpatterns = [
    path("<pk>", views.FaultReportView.as_view(), name="report"),
]
