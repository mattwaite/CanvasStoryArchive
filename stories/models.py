from django.db import models

class EntityType(models.Model):
    entity_type = models.CharField(max_length=255)
    entity_type_slug = models.SlugField()
    def __unicode__(self):
        return self.entity_type

class Entity(models.Model):
    entity_type = models.ForeignKey(EntityType, blank=True, null=True)
    entity_name = models.CharField(max_length=255)
    entity_name_slug = models.SlugField()
    class Meta:
        verbose_name_plural = "entities"
    def __unicode__(self):
        return self.entity_name

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
