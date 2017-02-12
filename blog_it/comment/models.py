from django.db import models
from django.utils import timezone

from mptt.models import MPTTModel, TreeForeignKey


class Comment(MPTTModel):
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

#    class MPTTMeta:
#         order_insertion_by = ['text']
#        order_insertion_by = ['published_date']

    def __str__(self):
        return str(self.text) if self.text else self.id

    def publish(self):
        self.published_date = timezone.now()
        self.save()
