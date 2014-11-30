from django.db import models

from textblob import TextBlob
from collections import Counter
from bs4 import BeautifulSoup
from django.utils.html import strip_tags
from django.utils.text import slugify
from nltk.stem.snowball import SnowballStemmer

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


class NounCount(models.Model):
    noun = models.CharField(max_length=255)
    noun_count = models.IntegerField()
    def __unicode__(self):
        return self.noun

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
    nouns = models.ManyToManyField(NounCount, blank=True, null=True)
    class Meta:
        verbose_name_plural = "stories"
    def update_nouns(self):
        text = self.full_text
        soup = BeautifulSoup(text)
        soup = soup.get_text()
        blobtext = TextBlob(soup)
        nouns = blobtext.noun_phrases
        nouns = [elem for elem in nouns if not elem.startswith("'s ",0,4)] # strips out some junk that TextBlob is returning with possessive nouns
        stems = []
        for n in nouns:
            stems.append(stemmer.stem(n))
        counts = dict(Counter(stems))
        for k, v in counts.items():
            nounct = NounCount.objects.create(noun=k, noun_count=v)
            noun = self.nouns.add(nounct)
    def save(self, *args, **kwargs):
        self.word_count = len(strip_tags(self.full_text).split(' '))
        self.headline_slug = slugify(self.headline)
        super(Story, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.headline
        
class RelatedStories(models.Model):
    story1 = models.ForeignKey(Story, related_name="story1")
    story2 = models.ForeignKey(Story, related_name="story2")
    story1count = models.IntegerField()
    matchcount = models.IntegerField()
    countsum = models.IntegerField()
    def __unicode__(self):
        return self.story1.headline