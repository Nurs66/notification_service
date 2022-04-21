from django.contrib import admin

from apps.customers import models


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'phone_number',
        'mobile_operator_code',
        'timezone',
    )
    search_fields = (
        'phone_number',
    )
