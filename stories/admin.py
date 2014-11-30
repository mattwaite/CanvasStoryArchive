from django.contrib import admin
from stories.models import EntityType, Entity, Story, NounCount, RelatedStories


class StoryAdmin(admin.ModelAdmin):
    search_fields = ['headline']
    list_display = ('headline', 'pubdate')

admin.site.register(EntityType)
admin.site.register(Entity)
admin.site.register(Story, StoryAdmin)
admin.site.register(NounCount)
admin.site.register(RelatedStories)