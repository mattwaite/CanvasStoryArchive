from django.core.management.base import BaseCommand, CommandError

from stories.models import Story, RelatedStories


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        stories1 = Story.objects.all() # SELECT ALL THE STORIES!
        for object in stories1: # Loop through them
            set1 = [] # let's make some empty lists yo
            set1sum = [] 
            for nouns in object.nouns.all():
                set1.append(nouns.noun) # populate the empty lists so we can compare them
                set1sum.append(nouns.noun_count)
            stories2 = Story.objects.exclude(id=object.id) # Now that we have the reference story loaded into a list, lets get all other stories
            for object2 in stories2: # Now we loop through them
                set2 = [] # Now we create a corresponding set of noun phrases to compare to
                set2sum = [] 
                for nouns2 in object2.nouns.all():
                    set2.append(nouns2.noun) # Populate the second noun list
                    set2sum.append(nouns2.noun_count)
                matches = set(set1) & set(set2) # Find the matches between them
                mcnt = len(matches) # How many matches are there?
                stycnt = len(set1) # How many noun phrases were in the candidate story?
                scr = sum(set1sum) # What does the number of instances of those keywords add up to?
                if mcnt > 0 and mcnt != 1: #Strip some garbage. This could be adjusted to cut waaaaay down on the number of matches to reduce bad matches in the database. This is what we went with in the proof of concept to see what we got.
                    rs = RelatedStories.objects.create(story1=object, story2=object2, story1count=stycnt, matchcount=mcnt, countsum=scr)
                else:
                    continue