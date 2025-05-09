# Register your models here.
from django.contrib import admin
from .models import InvoiceDetails

@admin.register(InvoiceDetails)
class InvoiceDetailsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'inv_no', 'po_no', 'date', 'project_codename', 'attn_to', 
        'payment_terms', 'account',
        'invoice_to_company_location', 'invoice_percentage', 'invoice_company_name', 'project'
    )
    search_fields = ('inv_no', 'po_no', 'project_codename', 'invoice_company_name')
    list_filter = ('date', 'invoice_company_name', 'invoice_percentage')
    ordering = ('-id',)
