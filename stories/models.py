from django.db import models
from django.utils.html import strip_tags
from django.utils.text import slugify

class EntityType(models.Model):
    entity_type = models.CharField(max_length=255)
    entity_type_slug = models.SlugField()
    def __unicode__(self):
        return self.entity_type
    def save(self, *args, **kwargs):
        self.entity_type_slug = slugify(self.entity_type)
        super(EntityType, self).save(*args, **kwargs)


class Entity(models.Model):
    entity_type = models.ForeignKey(EntityType, blank=True, null=True)
    entity_name = models.CharField(max_length=255)
    entity_name_slug = models.SlugField()
    class Meta:
        verbose_name_plural = "entities"
    def __unicode__(self):
        return self.entity_name
    def save(self, *args, **kwargs):
        self.entity_name_slug = slugify(self.entity_name)
        super(Entity, self).save(*args, **kwargs)


class Story(models.Model):
    headline = models.CharField(max_length=255)
    headline_slug = models.SlugField(blank=True, null=True)
    byline = models.CharField(max_length=255)
    pubdate = models.DateTimeField()
    description = models.TextField()
    full_text = models.TextField()
    large_image_url = models.URLField(blank=True, null=True)
    small_image_url = models.URLField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    word_count = models.IntegerField()
    entities = models.ManyToManyField(Entity)
    class Meta:
        verbose_name_plural = "stories"
    def __unicode__(self):
        return self.headline
    def save(self, *args, **kwargs):
        self.word_count = len(strip_tags(self.full_text).split(' '))
        self.headline_slug = slugify(self.headline)
        super(Story, self).save(*args, **kwargs)