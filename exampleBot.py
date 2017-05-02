import praw
import time
import sqlite3

sql = sqlite3.connect('YOUR_DATA_BASE_FILE_HERE.db')
db = sql.cursor()

print ("Logging in...")
r = praw.Reddit(client_id='',
                     client_secret='',
                     password='',
                     user_agent='',
                     username='')



def run_bot():
    print ("*** Polling subreddit...")
    submission = r.subreddit("CatsStandingUp").new(limit=1)



    for x in submission:
        if db.execute('SELECT count(*) FROM posts WHERE post_id=?', (x.id, )).fetchone()[0] == 0:
            x.reply("Cat.")
            print("	  Comment on post_id " + x.id + " was successful!")
            db.execute('INSERT into posts VALUES (?, ?)', (x.id, time.time()))
            sql.commit()


while True:
    run_bot()
    time.sleep(20)
