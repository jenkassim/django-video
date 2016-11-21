from django.db import models
from model_utils.models import TimeStampedModel


class Speaker(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=450, blank=True, null=True)

    github_handle = models.CharField(
        max_length=200, blank=True, null=True)
    twitter_handle = models.CharField(max_length=200, blank=True, null=True)
    facebook_profile_url = models.URLField(
        max_length=1500, blank=True, null=True)
    youtube_profile_url = models.URLField(
        max_length=1500, blank=True, null=True)

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.full_name


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    is_featured = models.BooleanField(default=False)

    @property
    def featured_videos(self):
        return self.videos.filter(featured_category=True)

    def __str__(self):
        return self.name


class Conference(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    site_url = models.URLField(max_length=1500)

    def __str__(self):
        return self.name


class Video(TimeStampedModel):
    title = models.CharField(max_length=200)
    youtube_video_id = models.CharField(max_length=200)
    speaker = models.ForeignKey(Speaker)
    description = models.TextField(blank=True, null=True)

    conference = models.ForeignKey(Conference)
    year = models.PositiveSmallIntegerField()
    categories = models.ManyToManyField(Category, related_name='videos')

    featured_category = models.BooleanField(default=False)

    @property
    def youtube_watch_url(self):
        return "https://www.youtube.com/watch?v={}".format(
            self.youtube_video_id)

    @property
    def youtube_embed_url(self):
        return "https://www.youtube.com/embed/{}".format(
            self.youtube_video_id)

    def __str__(self):
        return "{title} - {speaker} ({conference} {year})".format(
            title=self.title,
            speaker=self.speaker,
            conference=self.conference,
            year=self.year)


class HomeFeaturedVideo(TimeStampedModel):
    video = models.ForeignKey(Video)

    def __str__(self):
        return "Featured: {}".format(self.video)
