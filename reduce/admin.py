from django.contrib import admin
from .models import UrlRedirect, LogUrl
from django.http import HttpRequest


@admin.register(UrlRedirect)
class UrlRedirectAdmin(admin.ModelAdmin):
    list_display = ('destiny',  'created_at', 'updated_at')


@admin.register(LogUrl)
class UrlRedirectAdmin(admin.ModelAdmin):
    list_display = ('origin', 'created_at', 'ip', 'user_agent', 'host', 'url_redirect')
    
    def has_change_permission(self, request: HttpRequest, obj:None = None) -> bool:
        return False
    
    def has_delete_permission(self, request: HttpRequest, obj: None = None)-> bool: 
        return False
    
    def has_add_permission(self, request: HttpRequest) -> bool:
        return False