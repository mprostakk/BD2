from django.urls import path

import users.views as user_views

urlpatterns = [
    path("login", user_views.CustomLoginView.as_view(), name="login"),
    path("logout", user_views.CustomLogoutView.as_view(), name="logout"),
    path("register", user_views.CustomRegisterView.as_view(), name="register"),
    path("profile", user_views.CustomUserEditView.as_view(), name="edit"),
    path("profile/delete", user_views.CustomUserDeleteView.as_view(), name="delete"),
]
