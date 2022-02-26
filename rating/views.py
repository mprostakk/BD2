from datetime import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView

from rating.forms import RatingForm
from rating.models import Rating
from rent.models import Rent


class RatingView(LoginRequiredMixin, FormView):
    template_name = "rating/rating.html"
    form_class = RatingForm
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form: RatingForm):
        rating: Rating = form.save(commit=False)

        rating.user = self.request.user
        rating.rent = get_object_or_404(Rent, pk=self.kwargs.get("pk"))
        Rent.objects.filter(user=self.request.user).update(end_time=datetime.now())
        rating.save()
        messages.success(self.request, "Success adding rating")
        return super().form_valid(form)
