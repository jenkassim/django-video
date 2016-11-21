from django.views.generic import TemplateView
from .models import Video, HomeFeaturedVideo, Category

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        home_featured_video = HomeFeaturedVideo.objects.latest('id')

        featured_categories = Category.objects.filter(is_featured=True)

        context['home_featured_video'] = home_featured_video.video
        context['featured_categories'] = featured_categories
        return context
