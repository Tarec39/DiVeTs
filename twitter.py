import json, config 
from requests_oauthlib import OAuth1Session
import re

CK = config.CONSUMER_KEY
CS = config.CONSUMER_KEY_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

TWITTER = OAuth1Session(CK, CS, AT, ATS)

URL = "https://api.twitter.com/1.1/statuses/lookup.json"

class nyaa:
    def __init__(self, msg):
        self.msg = msg
        self.extractID()
        self.isVideo()
    def extractID(self):
        digits =re.findall(r'\d{10,}', self.msg)
        if(digits):
            self.id = "".join(digits)
            return

        else:return
    
    def isVideo(self):
        params ={'id' : self.id}
        res = TWITTER.get(URL, params=params)
    
        if res.status_code == 200:
            tweetObject = json.loads(res.text)

            if "video" in json.dumps(tweetObject):
                self.tweetObject = tweetObject
                return

            else:return
        else:
            print("Failed: %d" % res.status_code)
    
    def extractDirectLink(self):
        directLink = self.tweetObject[0]['extended_entities']['media'][0]['video_info']['variants']
        return(directLink[len(directLink)-2]['url'])
        