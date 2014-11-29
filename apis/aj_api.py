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
        for k, v in story['metadata'].items():
            entity_type = EntityType(entity_type=k)
            entity_type.save()
            if isinstance(v, dict):
                entity_obj = Entity(
                    entity_name=v['@value'],
                    entity_type=entity_type
                    )
                entity_obj.save()
                entities.append(entity_obj)
            else:
                for e in v:
                    entity = Entity(
                        entity_name=e['@value'],
                        entity_type=entity_type
                    )
                    entity.save()
                    entities.append(entity)
        s.entities.add(*entities)

def get_all_stories():
    n = 1
    while True:
        print 'Page %d' % n
        try:
            api = AlJazeeraAPI()
        except Exception as e:
            print 'Failed on page %d with message %s' % (n, e.message)
        stories = api.query_story('latest', pagenumber=n)
        for story in stories:
            api.save_story(story)
        n += 1

