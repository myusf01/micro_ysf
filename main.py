import tweepy
from tweepy import Stream, OAuthHandler
from tweepy.streaming import StreamListener
 
consumer_key = 'YOUR-CONSUMER-KEY'
consumer_secret = 'YOUR-CONSUMER-SECRET'
access_token = 'YOUR-ACCESS-TOKEN'
access_secret = 'YOUR-ACCESS-SECRET'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True



twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#python'])


def process_or_store(tweet):
    print(json.dumps(tweet))


for friend in tweepy.Cursor(api.friends).items():
    process_or_store(friend._json)



