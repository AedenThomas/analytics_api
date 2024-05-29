from django.db import models

class PageView(models.Model):
    url = models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    referrer = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.url
