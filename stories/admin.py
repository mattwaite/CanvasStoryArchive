from django.contrib import admin
from stories.models import EntityType, Entity, Story

admin.site.register(EntityType)
admin.site.register(Entity)
admin.site.register(Story)