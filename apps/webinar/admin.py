from django.contrib import admin
from .models import Webinar, Comment, CommentComplaint, WebinarSearchHistory

admin.site.register(Webinar)
admin.site.register(Comment)
admin.site.register(CommentComplaint)
admin.site.register(WebinarSearchHistory)
