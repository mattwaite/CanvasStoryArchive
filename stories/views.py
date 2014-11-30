import json
import string
from stories.models import Entity, EntityType
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def get_relevant_stories(entity):
    query_by_date = entity.story_set.order_by('pubdate')

    stories = {}
    stories['latest'] = query_by_date.last()
    stories['earliest'] = query_by_date.first()
    excluded_stories = [stories['latest'].id if stories['latest'] is not None else None] + [stories['earliest'].id if stories['earliest'] is not None else None]
    stories['longest'] = entity.story_set.exclude(id__in=excluded_stories).order_by('-word_count').first()
    excluded_stories += [stories['longest'].id if stories['longest'] is not None else None]
    stories['video'] = entity.story_set.exclude(id__in=excluded_stories).filter(video_url__isnull=False).first()
    stories = dict(filter(lambda i: i[1] is not None, stories.items()))
    
    return [{
        'context': context,
        'id': story.id,
        'link': story.link,
        'guid': story.guid,
        'headline': story.headline,
        'byline': story.byline,
        'pubdate': story.pubdate.strftime('%B %m, %Y'),
        'description': story.description,
        'large_image_url': story.large_image_url,
        'small_image_url': story.small_image_url,
        'video_url': story.video_url,
    } for context, story in stories.items()]

def get_color(entity_type):
    if entity_type.supertype == EntityType.PERSON:
        color = '#f4bbd6'
    elif entity_type.supertype == EntityType.PLACE:
        color = '#a6dcf4'
    elif entity_type.supertype in (EntityType.ORGANIZATION, EntityType.THING):
        color = '#e3e960'
    return color

def loop_through_words(words, words_offset=0, entity_matches=[]):
    for index, word in enumerate(words):
        if not word:
            continue
        e = Entity.objects.filter(entity_name__startswith=word,
            ).select_related('entity_type__name', 'entity_type__supertype').prefetch_related('story_set')
        for entity in e:
            entity_words = entity.entity_name.split(' ')
            entity_word_length = len(entity_words)
            if words[index:index+len(entity_words)] == entity_words and not entity.id in [i['id'] for i in entity_matches]:
                new_offset = words_offset + index
                entity_matches.append({
                    'id': entity.id,
                    'entity_name': entity.entity_name,
                    'entity_type': entity.entity_type.entity_type,
                    'color': get_color(entity.entity_type),
                    'entity_name_length': entity_word_length,
                    'stories': get_relevant_stories(entity),
                    'words_offset': new_offset
                    })
                return loop_through_words(words[index+entity_word_length:],
                    words_offset=new_offset+entity_word_length, 
                    entity_matches=entity_matches)
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
