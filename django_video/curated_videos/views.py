from django.views.generic import TemplateView
from .models import Video, HomeFeaturedVideo

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        home_featured_video = HomeFeaturedVideo.objects.latest('id')
        context['home_featured_video'] = home_featured_video.video
        return context
