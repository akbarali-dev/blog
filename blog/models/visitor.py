from django.db import models


class Visitor(models.Model):
    CATEGORY_CHOICES = (
        ('M', 'Media'),
        ('A', 'Admin'),
        ('S', 'Static'),
        ('W', 'Wep'),
    )

    ip_address = models.GenericIPAddressField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    referring_url = models.URLField(null=True, blank=True)
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, default='W')

    def __str__(self):
        return self.ip_address

    class Meta:
        db_table = 'visitor'
