#Canvas Archive#

How do we make story archives more useful with smart uses of structured data and text mining?

##The Problem##

Journalists and web producers know that the archives contain valuable context for current stories, but many avoid diving deep into the archives to find it. Why? Often, those archives are in terrible, proprietary systems that offer little more than a search box. More often, the person searching for that context doesn't have the time to dive through dozens or hundreds of stories to find the ones that are the most relevant.

What if a simple algorithm could make the first pass for them? Then the journalist just has to pick the best stories for context using human judgement and news organizations can capture some of the value now trapped in those archives.

##The Algorithm##

Most news organization have some combination of human and machine driven tagging for stories. Then, on pages, those tags generate related story lists. We think those are inadequate. Often the related stories are not quite right, or link to incremental updates to bigger stories, missing the bigger more contextual stories. 

This project devised a simple algorithm for relating stories using two dimensions of overlap in noun phrases between stories to determine relevance. 

First, noun phrases are extracted from a story and stored. The instances of unique noun phrases are counted for each item and the list of unique noun phrases and their magnititude within the story are stored. 

Second, the candidate story's noun phrase list is compared to all other stories noun phrase lists. The overlapping matches are then counted, and the magnitude of their occurrence is summed. This gives both the number of overlapping keywords AND their prevalence in the story. So a story about ebola, that mentions ebola frequently, will relate to other stories about ebola with similar noun phrases more than a story that mentions ebola a single time as an off handed reference.

Third, stories that have greater than 5 matches are filtered and ordered by the magnitude of the matches. This leaves only stories with significant overlap that mention those overlapping noun phrases multiple times. In other word, highly relevant and contextual stories. 

For this proof of concept, we used 3,900 stories from the Al Jazeera API. Finding noun phrase overlap required 15.2 million database operations, and resulted in more than 1 million relationships.

##Next steps##

Clearly, the algorithm will need to be optimized and faster processing methods will have to be found for it to go live. But the proof of concept works. Highly relevant stories are returned to the user based on the content of a given story. Testing it with a deeper archive with more stories would be ideal. 
