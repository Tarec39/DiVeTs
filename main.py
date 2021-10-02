import json, config 
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_KEY_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

twitter = OAuth1Session(CK, CS, AT, ATS)

url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

params ={'count' : 5}
res = twitter.get(url, params = params)

if res.status_code == 200:
    timelines = json.loads(res.text)
    for line in timelines:
        print(line)
        print('*******************************************')
else:
    print("Failed: %d" % res.status_code)