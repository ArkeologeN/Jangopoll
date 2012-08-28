from polls.models import Poll, Choice
from django.contrib import admin
from django.contrib.admin.helpers import Fieldset

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

# PollAdmin class to modify admin
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
                (None,               {'fields': ['question']}),
                ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question','pub_date') # @todo:  was_recently_published not working.
    list_filter  = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'

# Custom Module Formation and fields re-ordering
admin.site.register(Poll, PollAdmin)
#admin.site.register(Choice)