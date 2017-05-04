## Reddit Comment Bot
This is something I have been working on, now this was specifically developed to farm [Karma](https://reddit.zendesk.com/hc/en-us/articles/204511829-What-is-karma-)

This is a great working bot that incorporates sqlite along with the Reddit API. An important thing to notice is to not go above twenty seconds in the while loop because it would be against the [Reddit API Guidelines](https://github.com/reddit/reddit/wiki/API)
```
while True:
  run_bot()
  time.sleep(20)
```

All of the sqlite3 code in this file was written by [Charlton Trezevant](https://github.com/ctrezevant). Go check him out, he's a fantastic developer and I've learned a lot from him.

## Praw
Praw is the [Reddit API](https://praw.readthedocs.io/en/latest/) package for Python. It's extremely easy to install with pip, and here's the [guide](https://praw.readthedocs.io/en/latest/getting_started/installation.html) for that. Keep in mind which version of Python and Pip you are using. Make sure you also are installing the Praw package to the correct directory.

## Generating the bot's keys and ID's
In order to have a bot that communicates with Reddit, it needs to have approval. Which is generally quick to be approved so don't worry about wait time. In order to make a request visit this page [here](https://www.reddit.com/prefs/apps). Of course you'll need a reddit account dedicated to the bot. This is what this piece of code is here:
```
r = praw.Reddit(client_id='',
                     client_secret='',
                     password='',
                     user_agent='',
                     username='')
```
You will need this in every bot that you create. 

If you have any questions or need any help, feel free to contact myself or [Charlton](https://github.com/ctrezevant). Being fair, Charlton is by in large a much more experienced developer than myself and has way more languages under his belt.

Also as stated in the license, please contact me before copying the code.

Thank you, Julian.
