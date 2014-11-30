from django.conf.urls import patterns, include, url
from django.contrib import admin
from api.resources import StoryResource, EntityResource, RelatedStoriesResource

story_resource = StoryResource()
entity_resource = EntityResource()
related_resource = RelatedStoriesResource()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(story_resource.urls)),
    url(r'^api/', include(entity_resource.urls)),
    url(r'^api/', include(related_resource.urls)),
    url(r'^fulltext/', 'stories.views.get_nested_entities', name='get_nested_entities')
)
