from django.contrib import admin
from stories.models import EntityType, Entity, Story, NounCount, RelatedStories

admin.site.register(EntityType)
admin.site.register(Entity)
admin.site.register(Story)
admin.site.register(NounCount)
admin.site.register(RelatedStories)