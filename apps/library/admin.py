from django.contrib import admin
from .models import (
    BookAuthor, BookCategory,
    Book, UserBookProgress,
    AudioBook, AudioSection,
    AudioUnit, UserAudiobookProgress,
    LibrarySearchHistory
)

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ["pages"]


class AudioBookAdmin(admin.ModelAdmin):
    readonly_fields = ["duration"]


class AudioSectionAdmin(admin.ModelAdmin):
    readonly_fields = ["duration"]


class AudioUnitAdmin(admin.ModelAdmin):
    readonly_fields = ["duration"]


class UserAudiobookProgressAdmin(admin.ModelAdmin):
    readonly_fields = ["audiobook", "duration_so_far"]

admin.site.register(Book, BookAdmin)
admin.site.register(AudioBook, AudioBookAdmin)
admin.site.register(AudioSection, AudioSectionAdmin)
admin.site.register(AudioUnit, AudioUnitAdmin)
admin.site.register(UserAudiobookProgress, UserAudiobookProgressAdmin)
admin.site.register(BookAuthor)
admin.site.register(BookCategory)
admin.site.register(UserBookProgress)
admin.site.register(LibrarySearchHistory)
