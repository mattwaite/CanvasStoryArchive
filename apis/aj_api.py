"""
Talks to the Al Jazeera Story API.
Requres a valid AJ_API_KEY environment variable.
"""
import os
import sys
sys.path.append('/Users/liam/projects/canvas/CanvasStoryArchive/archives')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "archives.settings")

import requests
from dateutil import parser
from stories.models import Story, Entity, EntityType



AJ_API_LANGUAGE = 'en'
#AJ_API_SECRET = os.getenv('ALJAZEERA_API_SECRET')

class AlJazeeraAPI(object):
    BASE_URL = 'http://devapi.aljazeera.com/v1/'+AJ_API_LANGUAGE+'/stories/'
    AJ_API_KEY = os.getenv('ALJAZEERA_API_KEY')

    def query_story(self, section, pagesize=100, pagenumber=1):
        params = {
            'format': 'json',
            'apikey': self.AJ_API_KEY,
            'pagesize': pagesize,
            'pagenumber': pagenumber
        }
        endpoint = self.BASE_URL + section
        r = requests.get(endpoint, params=params)
        return r.json()['stories']

    def add_fields_to_story(self, story):
        stories = Story.objects.filter(headline=story['title']['#cdata-section'], pubdate=parser.parse(story['pubDate']))
        if stories.exists():
            for s in stories:
                s.link = story['link']
                s.guid = story['guid']
                s.save()
        else:
            s = Story.objects.create(
                guid=story['guid'],
                link=story['link'],
                headline=story['title']['#cdata-section'],
                byline=story['author'],
                pubdate=parser.parse(story['pubDate']),
                description=story['description']['#cdata-section'],
                full_text=story['body']['#cdata-section'],
                small_image_url=story['smallimage'],
                large_image_url=story['largeimage'],
                video_url=story['video']
            )
            entities = []
            if story['metadata'] is not None:
                for k, v in story['metadata'].items():
                    entity_type, entity_type_created = EntityType.objects.get_or_create(entity_type=k)
                    if isinstance(v, dict):
                        entity_obj, entity_created = Entity.objects.get_or_create(
                            entity_name=v['@value'],
                            entity_type=entity_type
                            )
                        entities.append(entity_obj)
                    else:
                        for e in v:
                            entity, entity_created = Entity.objects.get_or_create(
                                entity_name=e['@value'],
                                entity_type=entity_type
                            )
                            entities.append(entity)
            s.entities.add(*entities)

    def save_story(self, story):
        s = Story(
            headline=story['title']['#cdata-section'],
            byline=story['author'],
            pubdate=parser.parse(story['pubDate']),
            description=story['description']['#cdata-section'],
            full_text=story['body']['#cdata-section'],
            small_image_url=story['smallimage'],
            large_image_url=story['largeimage'],
            video_url=story['video']
        )
        s.save()
        entities = []
        if story['metadata'] is not None:
            for k, v in story['metadata'].items():
                entity_type, entity_type_created = EntityType.objects.get_or_create(entity_type=k)
                if isinstance(v, dict):
                    entity_obj, entity_created = Entity.objects.get_or_create(
                        entity_name=v['@value'],
                        entity_type=entity_type
                        )
                    entities.append(entity_obj)
                else:
                    for e in v:
                        entity, entity_created = Entity.objects.get_or_create(
                            entity_name=e['@value'],
                            entity_type=entity_type
                        )
                        entities.append(entity)
        s.entities.add(*entities)

import time
def get_all_stories(startpage=1):
    while True:
        print 'Page %d' % startpage
        api = AlJazeeraAPI()
        try:
            stories = api.query_story('latest', pagenumber=startpage)
        except Exception as e:
            print 'Failed on page %d with message %s' % (startpage, e.message)
            stories = []
        for story in stories:
            api.add_fields_to_story(story)
        startpage += 1
        time.sleep(2)
