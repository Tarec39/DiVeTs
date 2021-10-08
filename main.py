import json, config 
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_KEY_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

twitter = OAuth1Session(CK, CS, AT, ATS)

url = "https://api.twitter.com/1.1/statuses/lookup.json"

params ={'id' : "1384037445029617671"} #パラメーターに充てる
res = twitter.get(url, params=params)

if res.status_code == 200:
    timelines = json.loads(res.text)
    timelines = timelines[0]['extended_entities']['media'][0]['video_info']['variants']
    print(timelines[len(timelines)-2]['url'])
else:
    print("Failed: %d" % res.status_code)

