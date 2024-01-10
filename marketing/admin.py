from django.contrib import admin
from django.http.request import HttpRequest
from .models import About, SocialLink


class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request: HttpRequest) -> bool:
        count = About.objects.all().count()
        if count == 0:
            return True
        return False
    
admin.site.register(About, AboutAdmin)
admin.site.register(SocialLink)