from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import FormView, ListView, TemplateView

from rent.forms import RentForm
from rent.models import Rent, RentBreak
from users.models import CustomUser
from vehicle.models import Vehicle


class RentListView(LoginRequiredMixin, ListView):
    model = Rent
    template_name = "rent/rent_list.html"
    context_object_name = "rent_list"

    def get_queryset(self):
        return Rent.objects.filter(user=self.request.user).order_by("-start_time")


class RentCreateView(LoginRequiredMixin, FormView):
    template_name = "rent/rent_add.html"
    form_class = RentForm
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form: RentForm):
        rent: Rent = form.save(commit=False)

        user: CustomUser = self.request.user
        vehicle: Vehicle = get_object_or_404(Vehicle, pk=self.kwargs.get("pk"))
        rent.user = user
        rent.vehicle = vehicle

        errors = []
        if not rent.user.is_email_verified:
            errors.append("User email not verified")
        if not rent.user.is_payment_account_attached:
            errors.append("User has not payment account")
        if not rent.user.is_enough_money_to_rent:
            errors.append("User has not enough money to rent")
        if not rent.vehicle.is_currently_charged:
            errors.append("This vehicle is currently not charged")
        if rent.vehicle.is_currently_renting:
            errors.append("This vehicle is currently in renting")
        if rent.user.is_currently_renting:
            errors.append("User is currently renting")

        if errors:
            for error in errors:
                messages.error(self.request, error)
            return super().form_invalid(form)

        rent.save()
        messages.success(self.request, "Success creating Rent")
        return super().form_valid(form)


class RentEndView(LoginRequiredMixin, TemplateView):
    model = Rent
    success_url = reverse_lazy("rating")
    template_name = "rent/rent_end.html"

    def post(self, request, *args, **kwargs):
        rent: Rent = get_object_or_404(Rent, pk=self.kwargs.get("pk"), user=self.request.user)
        rent.end_time = timezone.now()
        rent.status = Rent.Status.END
        rent.total_cost = rent.calculate_total_cost()
        rent.save()

        if rent.is_currently_in_break:
            rent_break: RentBreak = rent.current_rent_break
            rent_break.end_time = rent.end_time
            rent_break.save()

        return redirect(reverse("rating", kwargs={"pk": rent.id}))


class RentBreakStartView(LoginRequiredMixin, TemplateView):
    model = RentBreak
    success_url = reverse_lazy("rating")
    template_name = "rent_break/rent_break_start.html"

    def post(self, request, *args, **kwargs):
        rent_break = RentBreak(pk=self.kwargs.get("pk"))
        rent: Rent = get_object_or_404(Rent, pk=self.kwargs.get("pk"), user=self.request.user)

        if rent.is_currently_in_break or rent.status == Rent.Status.BREAK:
            messages.error(self.request, "Rent has already started")
            return redirect(reverse("dashboard"))

        rent.status = Rent.Status.BREAK
        rent.save()
        rent_break.rent = rent
        rent_break.save()
        return redirect(reverse("dashboard"))


class RentBreakEndView(LoginRequiredMixin, TemplateView):
    model = RentBreak
    template_name = "rent_break/rent_break_end.html"

    def post(self, request, *args, **kwargs):
        rent_break = get_object_or_404(RentBreak, pk=self.kwargs.get("pk"))
        rent: Rent = get_object_or_404(Rent, pk=self.kwargs.get("pk"), user=self.request.user)
        if rent.status != Rent.Status.BREAK:
            messages.error(self.request, "Rent break has already been finished")
            return redirect(reverse("dashboard"))

        rent.status = Rent.Status.DURING
        rent.save()
        rent_break.end_time = timezone.now()
        rent_break.save()
        return redirect(reverse("dashboard"))
