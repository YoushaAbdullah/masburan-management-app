from django.contrib import admin
from .models import  Note



class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_per_page = 20


admin.site.register(Note, NoteAdmin)
