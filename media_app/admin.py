from django.contrib import admin

from media_app.models import Media


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    model = Media
    readonly_fields = ('counter_views', )
