from tastypie.resources import ModelResource
from stories.models import Story

class StoryResource(ModelResource):
    
    class Meta:
        queryset = Story.objects.all()
        resource_name = 'story'
        allowed_methods = ['get']

    def determine_format(self, request):
        return 'application/json'