from django.contrib import admin
from django import forms
from .models import Suggestion, Main_page, Rating, Information_page, Price, Blog_detail, Team
from .forms import SuggestionForm


# Custom ModelAdmin for Suggestion
class SuggestionAdmin(admin.ModelAdmin):
    form = SuggestionForm
    list_display = ('fullname', 'email', 'phone', 'subject')
    search_fields = ('fullname', 'email', 'phone', 'subject')
    list_filter = ('subject',)  # Corrected to be a tuple


admin.site.register(Main_page)
admin.site.register(Rating)
admin.site.register(Information_page)
admin.site.register(Price)
admin.site.register(Team)
admin.site.register(Blog_detail)
admin.site.register(Suggestion, SuggestionAdmin)
