# Hiyuki - Line Bot

**Hiyuki** is a Line Bot with access to the APIs of Danbooru, DeviantArt, Reddit, Twitter, and YouTube. This bot can retrieve and send content into Line chatrooms.

- Version: **1.8**
- Licensed under: **GPLv3**

## Packages Used
- [Line-bot-sdk](https://github.com/line/line-bot-sdk-python)
- [Pybooru](https://github.com/LuqueDaniel/pybooru)
- [Deviantart](https://github.com/neighbordog/deviantart)
- [PRAW](https://github.com/praw-dev/praw)
- [Twitter](https://github.com/sixohsix/twitter)
- [Google](https://github.com/googleapis/google-api-python-client)
- [OSRSBox](https://www.osrsbox.com/projects/osrsbox-db/)

## Features
- Fetch images from Danbooru at random or by using tags.
- Fetch images from DeviantArt at random or by using a search query.
- Retrieve a list of threads from a specified subreddit.
- Retrieve search results for a query within a subreddit.
- Retrieve latest Tweet from specified users.
- Retrieve a list of search results for a query from YouTube
- Fetch a random item and description from Runescape.

## Functions
- !help
- !random
- !tag [query]
- !dvart [query]
- !reddit [subreddit]
- !rsearch [subreddit] [query]
- !tw [name]
- !yt [keyword]
- !rs

## Screenshots
![Hiyuki](https://user-images.githubusercontent.com/45186205/53592449-4d3b2180-3b64-11e9-8f4f-4cd2df470bd5.png)
![Hiyuki3](https://user-images.githubusercontent.com/45186205/55526748-280a6900-5664-11e9-8509-c4a3aa4cd26b.png)
![Hiyuki4](https://user-images.githubusercontent.com/45186205/55527703-3ce8fb80-5668-11e9-806f-455c5843b1b3.png)
![Hiyuki6](https://user-images.githubusercontent.com/45186205/68438438-2a9ce600-0192-11ea-83eb-e514c6d5bd1e.png)
![Hiyuki2](https://user-images.githubusercontent.com/45186205/55526651-df52b000-5663-11e9-9190-8a573ea29b5c.png)
![Hiyuki5](https://user-images.githubusercontent.com/45186205/68438425-2375d800-0192-11ea-92e0-080cd515d706.png)



## Required Tokens
# Hiyuki.py
```python
handler = WebhookHandler('LineChannelSecret')
line = LineBotApi('LineChannelAccess')
reddit = praw.Reddit(client_id='REDDIT Client', client_secret="REDDIT Secret", user_agent='REDDIT UserAgent')
dvart = deviantart.Api('DvartChannel', 'DvartSecret')
tw = Twitter(
    auth=OAuth('TWITTER token', 'TWITTER token_secret', 'TWITTER consumer_key', 'TWITTER consumer_secret'))
youtube = build("youtube", "v3", developerKey="GOOGLE API KEY")
```
