from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from api.resources import StoryResource

story_resource = StoryResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'archives.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(story_resource.urls))
)
