from django.views.generic import TemplateView
from .models import Video, HomeFeaturedVideo, Category, Conference
from django.shortcuts import get_object_or_404


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        home_featured_video = HomeFeaturedVideo.objects.latest('id')

        featured_categories = Category.objects.filter(is_featured=True)

        context['home_featured_video'] = home_featured_video.video
        context['featured_categories'] = featured_categories
        return context


class SlugListingView(TemplateView):
    template_name = 'listing.html'
    MODEL_CLASS = None

    def get_context_data(self, **kwargs):
        context = super(SlugListingView, self).get_context_data(**kwargs)
        slug = kwargs['slug']
        listing = get_object_or_404(self.MODEL_CLASS, slug=slug)
        context['listing'] = listing
        context['videos'] = self.get_videos(listing)
        return context


class CategoryListingView(SlugListingView):
    MODEL_CLASS = Category

    def get_videos(self, obj):
        return obj.videos.all()


class ConferenceListingView(SlugListingView):
    MODEL_CLASS = Conference

    def get_videos(self, obj):
        return Video.objects.filter(conference=obj)
