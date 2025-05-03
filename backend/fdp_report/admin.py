# from django.contrib import admin
# from django.utils.html import format_html

# # Register your models here.
# from django.contrib import admin
# from .models import FdpReport

# class FdpReportAdmin(admin.ModelAdmin):
#     list_display = ('id', 'project', 'fdp', 'fdc', 'meter_reading', 'image_preview')
#     list_display_links = ('id', 'project')
#     search_fields = ('project__project_name',)
#     list_filter = ('project','fdp', 'fdc')
#     list_per_page = 25

#     def image_preview(self, obj):
#         if obj.image:
#             return format_html('<img src="{}" width="80" height="60" style="object-fit:cover;" />', obj.image.url)
#         return "(No Image)"
#     image_preview.short_description = 'Image Preview'

# admin.site.register(FdpReport, FdpReportAdmin)
