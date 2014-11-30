import json
import string
from stories.models import Entity
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def get_relevant_stories(entity):
    return [{
        'id': story.id,
        'headline': story.headline,
        'byline': story.byline,
        'pubdate': story.pubdate.strftime('%Y-%m-%dT%H:%M:%S'),
        'description': story.description,
        'large_image_url': story.large_image_url,
        'small_image_url': story.small_image_url,
        'video_url': story.video_url,
    } for story in entity.story_set.all()]


def loop_through_words(words, words_offset=0, entity_matches=[]):
    for index, word in enumerate(words):
        e = Entity.objects.filter(entity_name__startswith=word
            ).select_related('entity_type__entity_type'
            ).prefetch_related('story_set')
        for entity in e:
            entity_words = entity.entity_name.split(' ')
            if words[index:index+len(entity_words)] == entity_words and not entity.id in [i['id'] for i in entity_matches]:
                new_offset = words_offset + index
                entity_matches.append({
                    'id': entity.id,
                    'entity_name': entity.entity_name,
                    'entity_type': entity.entity_type.entity_type,
                    'stories': get_relevant_stories(entity),
                    'words_offset': new_offset
                    })
                return loop_through_words(words[index+len(entity_words):], words_offset=new_offset+len(entity_words), entity_matches=entity_matches)
    return entity_matches


def get_matching_entities(fulltext):
    words = [i.strip(string.punctuation + string.whitespace) for i in fulltext.split(' ')]
    entity_matches = loop_through_words(words)
    return entity_matches

@csrf_exempt
def get_nested_entities(request):
    if request.GET:
        fulltext = request.GET['text']
    else:
        fulltext = json.loads(request.body)['text']

    entity_matches = get_matching_entities(fulltext)

    return HttpResponse(json.dumps({'results': entity_matches}), content_type='application/json')
