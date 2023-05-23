import snscrape.modules.twitter as sntwitter
import pandas as pd

query="(#flood OR #,fire OR #,rain) lang:en until:2020-09-17 since:2009-04-15"
tweets=[]
limit=100
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets)==limit:
        break
    else:
        tweets.append([tweet.id,tweet.date,tweet.user.username,tweet.content])

df=pd.DataFrame(tweets,columns=['Id','Date','user','Tweet'])
df.to_csv('scra.csv',index=False,encoding='utf-8')