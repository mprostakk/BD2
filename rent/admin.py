from django.contrib import admin
from django.contrib.admin import ModelAdmin

from rent.models import Rent, RentBreak


class RentBreakAdmin(ModelAdmin):
    readonly_fields = ("start_time",)


admin.site.register(Rent)
admin.site.register(RentBreak, RentBreakAdmin)
