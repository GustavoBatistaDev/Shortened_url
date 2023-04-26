from django.db import models


class UrlRedirect(models.Model):

    destiny = models.URLField(max_length=600)
    shortened = models.URLField(max_length=600, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.destiny
    

class LogUrl(models.Model):
   
    origin = models.URLField(max_length=600, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user_agent = models.CharField(max_length=600, null=True, blank=True )
    host = models.CharField(max_length=600, null=True, blank=True )
    ip = models.GenericIPAddressField( null=True, blank=True )

    url_redirect = models.ForeignKey(UrlRedirect, models.DO_NOTHING, related_name="logs")