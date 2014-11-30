from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from stories.models import Story, Entity, EntityType, RelatedStories

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

class RelatedStoriesResource(ModelResource):
    story1 = fields.ForeignKey(StoryResource, 'story1', full=False)
    story2 = fields.ForeignKey(StoryResource, 'story2', full=True)
    class Meta:
        queryset = RelatedStories.objects.all().order_by('countsum').filter(matchcount__gt=5)
        resource_name = 'related'
        allowed_methods = ['get']
        filtering = {
                    'story1': ALL_WITH_RELATIONS,
                    'story2': ALL_WITH_RELATIONS,
                    'created': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
                }

    def determine_format(self, request):
        return 'application/json'
