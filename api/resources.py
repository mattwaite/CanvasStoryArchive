from tastypie import fields
from tastypie.resources import ModelResource
from stories.models import Story, Entity, EntityType

class EntityTypeResource(ModelResource):

    class Meta:
        queryset = EntityType.objects.all()
        resource_name = 'entity_type'
        allowed_methods = ['get']


class EntityResource(ModelResource):
    entity_type = fields.ForeignKey(EntityTypeResource, 'entity_type', full=True)
    #story_set = fields.ManyToManyField('api.resources.StoryResource', 'story_set', full=True)

    class Meta:
        queryset = Entity.objects.all()
        resource_name = 'entity'
        allowed_methods = ['get']

    def determine_format(self, request):
        return 'application/json'

class StoryResource(ModelResource):
    entities = fields.ManyToManyField(EntityResource, 'entities', full=True)

    class Meta:
        queryset = Story.objects.all()
        resource_name = 'story'
        allowed_methods = ['get']

    def determine_format(self, request):
        return 'application/json'
