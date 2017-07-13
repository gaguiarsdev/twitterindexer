from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import tweepy
import requests

ckey = 'odv8ArZCY8jYF1I0ouA6YhUkc'
csecret = 'uCItp88lB7JXx9KjOSFmucieBbdDmDQV2pGgyszs7NmDsjV5GI'
atoken = '3003780227-dSNYMNV0rSagWlXFQKThVj2FbpdRiDKkkKGNimf'
asecret = 'O94WtGID6f41FuifTBy6ddm6uNyG5s2BvYUXNghEnk5mc'

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)


def getImageUrlFile(sentUser):

    api = tweepy.API(auth)

    user = api.get_user(sentUser)
    print (user.screen_name)

    filename = user.screen_name+".csv"

    print (filename)
    saveFile = open(filename,'w')



    public_tweets = api.user_timeline(screen_name = user.screen_name,count=200)
    for tweet in public_tweets:
        if 'media' in tweet.entities:
            for image in  tweet.entities['media']:
                data = image['media_url']
                saveFile.write(data)
                saveFile.write('\n')

    saveFile.close()
