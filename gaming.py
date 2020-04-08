import urllib.request
import json

key = "" #Put your key here. You can get it from console.developers.google.com


def channelData(channel_name, channel_id):
    data=urllib.request.urlopen(generate_url(channel_id)).read()

    subs = json.loads(data)['items'][0]['statistics']['subscriberCount']
    views = json.loads(data)['items'][0]['statistics']['viewCount']
    videoCount = json.loads(data)['items'][0]['statistics']['videoCount']
    print(f'\n{channel_name}')
    print("--------------------")
    print(f'Subscribers: {subs} \nViews: {views} \nNumer of videos: {videoCount}')
    print("--------------------\n")

def generate_url(channel_id):
    return f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={key}'

# Usage example
channelData("Eversti", "UC5Fxcdrh9-f4HHdTVhUA8VQ")