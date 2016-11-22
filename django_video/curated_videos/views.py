from django.views.generic import TemplateView
from .models import Video, HomeFeaturedVideo, Category, Conference, Speaker
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
    DEFAULT_ARUGMENT_NAME = 'slug'

    def get_obj_display_name(self, obj):
        return obj.name

    def get_context_data(self, **kwargs):
        context = super(SlugListingView, self).get_context_data(**kwargs)
        filter_argument = kwargs[self.DEFAULT_ARUGMENT_NAME]
        filter_criteria = {
            self.DEFAULT_ARUGMENT_NAME: filter_argument
        }
        listing = get_object_or_404(self.MODEL_CLASS, **filter_criteria)
        context['listing'] = listing
        context['display_listing_name'] = self.get_obj_display_name(listing)
        context['videos'] = self.get_videos(listing)
        return context


class CategoryListingView(SlugListingView):
    MODEL_CLASS = Category

    def get_videos(self, obj):
        return obj.videos.all()


class SpeakerListingView(SlugListingView):
    MODEL_CLASS = Speaker
    DEFAULT_ARUGMENT_NAME = 'id'

    def get_obj_display_name(self, obj):
        return obj.full_name

    def get_videos(self, obj):
        return Video.objects.filter(speaker=obj)


class ConferenceListingView(SlugListingView):
    MODEL_CLASS = Conference

    def get_videos(self, obj):
        return Video.objects.filter(conference=obj)
