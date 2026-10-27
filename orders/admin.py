from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Inquiry


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer_name',
        'customer_email',
        'customer_phone',
        'product',
        'desired_quantity',
        'status',
        'created_at',
    )

    list_filter = ('status', 'created_at')
    search_fields = (
        'customer_name',
        'customer_email',
        'customer_phone',
    )
    readonly_fields = ('created_at',)
