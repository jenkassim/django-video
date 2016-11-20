from django.contrib import admin
from .models import Video, Conference, Speaker, Category, HomeFeaturedVideo


class ConferenceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Video)
admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Speaker)
admin.site.register(Category, CategoryAdmin)
admin.site.register(HomeFeaturedVideo)
