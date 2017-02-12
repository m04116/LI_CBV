from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'parent', 'pk', 'published_date')


admin.site.register(Comment, CommentAdmin)
