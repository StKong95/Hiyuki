# Hiyuki - Line Bot

**Hiyuki** is a Line Bot with access to the APIs of Danbooru, DeviantArt, Reddit, and Twitter. This bot can retrieve and send content into Line chatrooms.

- Version: **1.6**
- Licensed under: **GPLv3**

## Packages Used
- [Line-bot-sdk](https://github.com/line/line-bot-sdk-python)
- [Pybooru](https://github.com/LuqueDaniel/pybooru)
- [Deviantart](https://github.com/neighbordog/deviantart)
- [PRAW](https://github.com/praw-dev/praw)
- [Twitter](https://github.com/sixohsix/twitter)
- [OSRSBox](https://www.osrsbox.com/projects/osrsbox-db/)

## Features
- Fetch images from Danbooru at random or by using tags.
- Fetch images from DeviantArt at random or by using a search query.
- Retrieve a list of threads from a specified subreddit.
- Retrieve search results for a query within a subreddit.
- Retrieve latest Tweet from specified users.
- Calculates speed mods for Dance Dance Revolution based on target reading speed.

## Functions
- !help
- !random
- !tag [query]
- !dvart [query]
- !reddit [subreddit]
- !rsearch [subreddit] [query]
- !tw [name]
- !bpm set [###]
- !bpm [###]

## Screenshot
![Hiyuki](https://user-images.githubusercontent.com/45186205/53592449-4d3b2180-3b64-11e9-8f4f-4cd2df470bd5.png)

## Required Tokens
# Hiyuki.py
```python
handler = WebhookHandler('LineChannelSecret')
line = LineBotApi('LineChannelAccess')
reddit = praw.Reddit(client_id='Client', client_secret="Secret", user_agent='UserAgent')
dvart = deviantart.Api('DvartChannel', 'DvartSecret')
tw = Twitter(
    auth=OAuth('token', 'token_secret', 'consumer_key', 'consumer_secret'))
```
