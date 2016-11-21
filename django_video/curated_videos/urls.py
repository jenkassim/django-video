from django.conf.urls import url
from .views import HomePageView, CategoryListingView, ConferenceListingView


urlpatterns = [
    url(r'^$', HomePageView.as_view()),
    url(r'^category/(?P<slug>[\w-]+)$', CategoryListingView.as_view(), name='category-listing'),
    url(r'^conference/(?P<slug>[\w-]+)$', ConferenceListingView.as_view(), name='conference-listing'),
]
