from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),

    # url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^', include('curated_videos.urls', namespace="curated_videos")),


]
