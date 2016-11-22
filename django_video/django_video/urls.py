from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),

    url(r'^about$', TemplateView.as_view(template_name="about.html"), name='about'),
    url(r'^', include('curated_videos.urls', namespace="curated_videos")),


]
