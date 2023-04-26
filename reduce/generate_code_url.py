from .models import UrlRedirect
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse


class CodeUrl:
    def __init__(self, url: UrlRedirect):
        if not isinstance(url, UrlRedirect):
            raise ValueError('url precisa ser uma instância de UrlRedirect') 
        self.url = url
    
    def _generate_url(self):
        protocol = 'http' if settings.DEBUG else 'https'
        domain = settings.DOMAIN
        uid = urlsafe_base64_encode(force_bytes(self.url.id))
        return f'{protocol}://{domain}{reverse("reduce:generate_url")}{uid}'
