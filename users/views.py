from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import DeleteView, FormView, UpdateView

from users.forms import CustomRegisterForm, CustomUserEditForm


class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    success_url = reverse_lazy("dashboard")

    def get_success_url(self):
        messages.success(self.request, "Logged in")
        return reverse_lazy("dashboard")


class CustomLogoutView(LogoutView):
    template_name = "registration/logout.html"
    success_url = reverse_lazy("dashboard")

    def get_success_url(self):
        messages.success(self.request, "Logged out")
        return reverse_lazy("dashboard")


class CustomRegisterView(FormView):
    form_class = CustomRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Success creating user")
        return super().form_valid(form)


class CustomUserEditView(LoginRequiredMixin, UpdateView):
    form_class = CustomUserEditForm
    template_name = "users/edit.html"
    success_url = reverse_lazy("edit")

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Successfully saved user profile")
        return super().form_valid(form)


class CustomUserDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy("login")
    template_name = "users/delete.html"

    def get_object(self, queryset=None):
        return self.request.user
