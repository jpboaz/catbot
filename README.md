## Reddit Comment Bot
This is something I have been working on, now this was specifically developed to farm [Karma](https://reddit.zendesk.com/hc/en-us/articles/204511829-What-is-karma-)

This is a great working bot that incorporates sqlite along with the Reddit API. An important thing to notice is to not go above twenty seconds in the while loop because it would be against the [Reddit API Guidelines](https://github.com/reddit/reddit/wiki/API)
```
while True:
  run_bot()
  time.sleep(20)
```

All of the sqlite3 code in this file was written by [Charlton Trezevant](https://github.com/ctrezevant). Go check him out, he's a fantastic developer. and I've learned a lot from him.
