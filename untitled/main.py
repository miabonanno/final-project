from urllib import urlopen
import json
import itertools
import datetime
import json
import sqlite3

group_ids = ['34963423', '26676347', '36638238', '16927339', '25449094']
base_url = "https://api.groupme.com/v3"


access_token = "517966831.7a61c9e.1ad29a68d08f4aa883d06bbd2deba6c7"


response = urlopen('https://api.instagram.com/v1/users/self/media/recent/?access_token=517966831.7a61c9e.1ad29a68d08f4aa883d06bbd2deba6c7')
str_response=response.read().decode('utf-8')
obj = json.loads(str_response)
print (obj)


CACHE_FNAME= '206_FinalProj_cache.json'
try:
    cache_file=open(CACHE_FNAME, 'r') #attempting to read data from file
    cache_data=cache_file.read()#puts data into string if it is there
    cache_file.close() #close file, put data in dictionary
    CACHE_DICTION= json.loads(cache_data) #loads into dictionary
except:
    CACHE_DICTION= {}

conn= sqlite3.connect('206FinalProj.sqlite')
cur=conn.cursor()

cur.execute('DROP TABLE IF EXISTS My_Instagram_DB;')
cur.execute('CREATE TABLE MY_Instagram_DB ("created_time" TEXT, "likes" INTEGER, "hashtags" TEXT, "comments" INTEGER, "location" TEXT)')

daycode={6:"Sunday",
         5: "Saturday",
         4: "Friday",
         3: "Thursday",
         2: "Wednesday",
         1: "Tuesday",
         0: "Monday"}

for info in obj['data']: #looping through dictionary of data to access relevant data needed for each database column
   created_time= str(datetime.datetime.fromtimestamp(int(str(info['created_time']))))
   intdayofweek = datetime.datetime.weekday(datetime.datetime.fromtimestamp(int(str(info['created_time']))))
   likes= info['likes']['count']
   comments= info['comments']['count']
   location=info['location']
   hashtags=info['tags']
   strdayofweek = daycode[intdayofweek]
   print (strdayofweek)


   #cur.execute('''INSERT OR IGNORE INTO My_Instagram_DB (created_time, likes, hashtags, comments, location) VALUES (?, ?, ?, ?, ?)''', (created_time, likes, hashtags, comments, location))

conn.commit()


