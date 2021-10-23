import json, config 
from requests_oauthlib import OAuth1Session
import re

CK = config.CONSUMER_KEY
CS = config.CONSUMER_KEY_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

TWITTER = OAuth1Session(CK, CS, AT, ATS)

URL = "https://api.twitter.com/1.1/statuses/lookup.json"

class nyaa():
    def __init__(self, msg):
        self.msg = msg
        self.extractID()

    def extractID(self):
        digitsList =re.findall(r'\d{10,}', self.msg)
        if(digitsList):
            self.digitsStr = "".join(digitsList)
             
        else:return
    pass

def getDirectLink(id):
    params ={'id' : id}
    res = TWITTER.get(URL, params=params)
    
    if res.status_code == 200:
        directLink = json.loads(res.text)
        directLink = directLink[0]['extended_entities']['media'][0]['video_info']['variants']
        return directLink[len(directLink)-2]['url']
    else:
        print("Failed: %d" % res.status_code)
