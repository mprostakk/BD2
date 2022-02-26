from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

handler404 = "scooters.views.custom_page_not_found_view"

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"^vehicle/", include("vehicle.urls")),
    re_path(r"^rent/", include("rent.urls")),
    re_path(r"^report/", include("report.urls")),
    re_path(r"^rating/", include("rating.urls")),
    re_path(r"^users/", include("users.urls")),
    re_path(r"", include("dashboard.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
