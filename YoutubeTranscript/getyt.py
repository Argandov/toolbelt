#!/usr/bin/env python3

from youtube_transcript_api import YouTubeTranscriptApi as yta
import sys

# retrieve the available transcripts

video_id = youtube_id = sys.argv[1].split("/")[-1]

data = yta.get_transcript(video_id)

transcript= ""

for value in data:
    for key,val in value.items():
        if key== "text":
            transcript += val
            l= transcript.splitlines()
            final_tra = " ".join(l)
            transcript += " "

print(final_tra)
