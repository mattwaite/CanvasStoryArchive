from django.core.management.base import BaseCommand, CommandError

from stories.models import Story, RelatedStories


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
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
                mcnt = len(matches)
                stycnt = len(set1)
                scr = sum(set1sum)
                if mcnt > 0 and mcnt != 1:
                    rs = RelatedStories.objects.create(story1=object, story2=object2, story1count=stycnt, matchcount=mcnt, countsum=scr)
                else:
                    continue