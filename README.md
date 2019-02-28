# Hiyuki - Line Bot

**Hiyuki** is a Line Bot with access to the APIs of Danbooru, Reddit, and DeviantArt. This bot can retrieve and send content into Line chatrooms.

- Version: **1.4**
- Licensed under: **GPLv3**

## Packages Used
- [line-bot-sdk](https://github.com/line/line-bot-sdk-python)
- [Pybooru](https://github.com/LuqueDaniel/pybooru)
- [PRAW](https://github.com/praw-dev/praw)
- [deviantart](https://github.com/neighbordog/deviantart)

## Screenshot
![Hiyuki](https://user-images.githubusercontent.com/45186205/53592449-4d3b2180-3b64-11e9-8f4f-4cd2df470bd5.png)

## Features
- Fetch images from Safebooru at random or by using tags.
- Fetch images from DeviantArt at random or by using a search query.
- Retrieve a list of threads from a specified subreddit.
- Retrieve search results for a query within a subreddit.
- Calculates speed mods for Dance Dance Revolution based on target reading speed.

## Functions
- !help
- !random
- !tag "term"
- !reddit "subreddit"
- !rsearch "subreddit" "query"
- !dvart "term"
- !bpm set ###
- !bpm ###

## Required Tokens
# Hiyuki.py
```python
handler = WebhookHandler('LineChannelSecret')
```

# classes\bot.py
```python
self.line_bot_api = LineBotApi('LineChannelAccess')
self.reddit = praw.Reddit(client_id='Client', client_secret="Secret", user_agent='UserAgent')
self.da = deviantart.Api("DvartChannel", "DvartSecret")
```
