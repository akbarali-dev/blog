from django.db import models


class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)
    referring_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.ip_address

    class Meta:
        db_table = 'visitor'
