from django.contrib import admin
from .models import profile,Song,Album
# Register your models here.
class profileAdmin(admin.ModelAdmin):
    class Meta():
        model=profile
admin.site.register(profile,profileAdmin)

admin.site.register(Album)

admin.site.register(Song)

