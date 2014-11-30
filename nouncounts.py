import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CanvasStoryArchive.archive.settings")
django.setup()

from stories.models import Story, RelatedStories

stories1 = Story.objects.all()

for object in stories1:
    set1 = []
    set1sum = []
    for nouns in object.nouns.all():
        set1.append(nouns.noun)
        set1sum.append(nouns.noun_count)
    stories2 = Story.objects.exclude(id=object.id)
    for object2 in stories2:
        set2 = []
        for nouns2 in object2.nouns.all():
            set2.append(nouns2.noun)
        matches = set(set1) & set(set2)
        matchcount = len(matches)
        if matchcount != 0:
            pct = float(matchcount/len(set1))
            scr = float(pct * sum(set1sum))
            #rs = RelatedStories.objects.create(story1=object, story2=object2, percent=pct, score=scr)
            print pct, scr
        else:
            continue
        set2 = []
    set1=[]
    set1sum=[]
            
            