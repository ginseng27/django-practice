from django.contrib import admin
from polls.models import Poll
from polls.models import Choice

# Register your models here.
class ChoiceInline(admin.TabularInline):
    #admin.tabularinline makes it a table
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    #fieldsets describes the order to display the model variables
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date Info', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    #inlines define the inline choice based off the given class
    inlines = [ChoiceInline]

    #this makes the poll change list page display more than just the str()
    list_display = ('question', 'pub_date', 'was_published_recently')
    #this gives teh filter list on the right
    #after the propler properties are added in polls/models.py
    list_filter = ['pub_date']

    #add a search bar on the top
    search_fields = ['question']

admin.site.register(Poll, PollAdmin)
