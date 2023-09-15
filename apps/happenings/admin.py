from django.contrib import admin
from .models import (
    News, Poll, PollChoice,
    Tag, Event, UserPoll
)

class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}


class PollAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "updated_at",
        "is_active",
        "total_votes"
    ]
    prepopulated_fields = {"slug": ["title"]}

    def total_votes(self, obj):
        return obj.get_total_votes()


class PollChoiceAdmin(admin.ModelAdmin):
    readonly_fields = ["votes"]


class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}


admin.site.register(Poll, PollAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(PollChoice, PollChoiceAdmin)
admin.site.register(UserPoll)
admin.site.register(Tag)
