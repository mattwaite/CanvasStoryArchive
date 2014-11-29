from django.db import models

class EntityType(models.Model):
    entity_type = models.CharField(max_length=255)
    entity_type_slug = models.SlugField()
    def __unicode__(self):
        return self.entity_type


class Entity(models.Model):
    entity_name = models.CharField(max_length=255)
    entity_name_slug = models.SlugField()
    class Meta:
        verbose_name_plural = "entities"
    def __unicode__(self):
        return self.entity_name


class Story(models.Model):
    headline = models.CharField(max_length=255)
    byline = models.CharField(max_length=255)
    pubdate = models.DateTimeField()
    description = models.TextField()
    full_text = models.TextField()
    word_count = models.IntegerField()
    entities = models.ManyToManyField(Entity)
    class Meta:
        verbose_name_plural = "stories"
    def __unicode__(self):
        return self.headline