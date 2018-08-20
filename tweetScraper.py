import tweepy #https://github.com/tweepy/tweepy
import csv

c_key = 'MINE'
c_secret = 'MINE'

access_token = 'MINE'
access_token_secret = 'MINE'

fieldnames = ['text', 'handle']
csvfile = open('obama_tweets.csv', 'w')
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)


auth = tweepy.OAuthHandler(c_key, c_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = []
new_tweets = api.user_timeline(' BarackObama ',count=200)

tweets.extend(new_tweets)
oldest = tweets[-1].id - 1

while len(new_tweets) > 0:
	print ("getting tweets before " + str(oldest))
	new_tweets = api.user_timeline(' BarackObama ',count=200, max_id=oldest)
	tweets.extend(new_tweets)
	oldest = tweets[-1].id - 1
	print ("... tweets downloades yet " + str((len(tweets))))

print ("done")

writer.writeheader()
for tweet in tweets:
	if (not tweet.retweeted) and ('RT @' not in tweet.text):
		writer.writerow({'text': tweet.text.encode("utf-8"), 'handle': 'BarackObama'})

