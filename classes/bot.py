from __future__ import unicode_literals
from pybooru import Danbooru
from random import *
from urllib.request import urlopen
import deviantart

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import *
from linebot.models import *

import re
import praw
import json
from twitter import *


# bot reply class
class BotClass:
    def __init__(self, line, reddit, dvart, tw):
        self.client = Danbooru(site_url='https://safebooru.donmai.us/')
        self.limit = 3
        self.bpm = 660
        self.line_bot_api = line
        self.reddit = reddit
        self.da = dvart
        self.tw = tw

    # Check input and reply according
    def check(self, event):
        check = re.match(r"(!\w+)(\s)?(\D+)?", event.message.text)

        # Command list
        if check.group(1) == "!help":
            message = TextSendMessage(
                text="Commands:\n!tag [query]\n!random\n!dvart [query]\n!rs\n!reddit [subreddit]\n!rsearch [subreddit] [query]\n!tw [name] {#}\n!bpm set [###]\n!bpm [###]")
            self.line_bot_api.reply_message(event.reply_token, message)

        # !random !tag - Image functions
        elif check.group(1) == "!random":
            self.reply(event)
        elif check.group(1) == "!tag":
            self.reply(event, check.group(3))

        # !site - Check current site
        elif check.group(1) == "!site":
            message = TextSendMessage(text=self.client.site_url)
            self.line_bot_api.reply_message(event.reply_token, message)

        # !hiyuki - Safe mode toggle
        elif check.group(1) == "!hiyuki" and check.group(3) == "lewd":
            self.client = Danbooru('danbooru')
            message = TextSendMessage(text="Safe Mode Off.")
            self.line_bot_api.reply_message(event.reply_token, message)

        elif check.group(1) == "!hiyuki":
            self.client = Danbooru(site_url='https://safebooru.donmai.us/')
            message = TextSendMessage(text="Hiyuki Online!")
            self.line_bot_api.reply_message(event.reply_token, message)

        # !reddit - Reddit Hot
        elif check.group(1) == "!reddit":
            check = re.match(r"!reddit\s(\w+)?", event.message.text)
            subreddit = self.reddit.subreddit(check.group(1))
            search = "r/{0}\n\n".format(check.group(1))
            for submission in subreddit.hot(limit=self.limit):
                search += "{0}\n{1}\n\n".format(submission.title, submission.url)
            message = TextSendMessage(text=search)
            self.line_bot_api.reply_message(event.reply_token, message)

        # !rsearch - Reddit Search
        elif check.group(1) == "!rsearch":
            check = re.match(r"!rsearch\s(\w+)?(\s)?(\w+)?", event.message.text)
            search = "Searching for \"{0}\" in r/{1}:\n\n".format(check.group(3), check.group(1))
            for submission in self.reddit.subreddit(check.group(1)).search(check.group(3), limit=self.limit):
                search += "{0}\n{1}\n\n".format(submission.title, submission.url)
            message = TextSendMessage(text=search)
            self.line_bot_api.reply_message(event.reply_token, message)

        # !limit - Reddit Limit
        elif check.group(1) == "!limit":
            check = re.match(r"!limit\s(\d)?", event.message.text)
            if check.group(1) is not None:
                self.limit = int(check.group(1))
            message = TextSendMessage(text="Limit set to {0}.".format(self.limit))
            self.line_bot_api.reply_message(event.reply_token, message)

        # !rs - Display information about a random Runescape item
        elif check.group(1) == "!rs":
            random = randint(0, 23100)
            url = ("https://www.osrsbox.com/osrsbox-db/items-json/{0}.json".format(random))
            response = urlopen(url)
            data = response.read().decode("utf-8")
            json_obj = json.loads(data)
            message = TextSendMessage(text="{0}\n\n{1}".format(json_obj["name"], json_obj["examine"]))
            image = ImageSendMessage(
                original_content_url='https://www.osrsbox.com/osrsbox-db/items-icons/{0}.png'.format(
                    random),
                preview_image_url='https://www.osrsbox.com/osrsbox-db/items-icons/{0}.png'.format(
                    random))
            self.line_bot_api.reply_message(event.reply_token,
                                            [image, message])

        # !dvart - DeviantArt
        elif check.group(1) == "!dvart":
            loop = 0
            max = 30000
            self.dvart(event, loop, max, check.group(3))

        # !bpm - BPM calculator
        elif check.group(1) == "!bpm":
            check = re.match(r"(!bpm+?)(\s)*(set)*(\s)*(\d+)*", event.message.text)

            # Set the target BPM
            if check.group(3) == "set":
                self.bpm = int(check.group(5))
                message = TextSendMessage(text="BPM set to {0}.".format(self.bpm))
                self.line_bot_api.reply_message(event.reply_token, message)

            # Do BPM multiplication calculations
            else:
                if check.group(5) is not None:
                    input = int(check.group(5))
                    calc = self.bpm / input
                    multi = [0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00, 3.25, 3.50, 3.75,
                             4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0]
                    lower = min(multi, key=lambda x: abs(x - calc))
                    if lower * input > self.bpm:
                        upper = multi[multi.index(lower) - 1]
                    elif multi.index(lower) < 23:
                        upper = multi[multi.index(lower) + 1]
                    else:
                        upper = lower
                    low = lower * input
                    up = upper * input
                    if upper == lower or calc == lower:
                        message = TextSendMessage(
                            text="Target: {0}\nInput: {1}\n\n{2}x = {3}".format(self.bpm, input, lower, low))
                    else:
                        message = TextSendMessage(
                            text="Target: {0}\nInput: {1}\n\n{2}x = {3}\n{4}x = {5}".format(self.bpm, input,
                                                                                            lower, low,
                                                                                            upper, up))
                    self.line_bot_api.reply_message(event.reply_token, message)

                # Show the current target BPM if nothing is specified
                else:
                    message = TextSendMessage(text="BPM is currently set to {0}.".format(self.bpm))
                    self.line_bot_api.reply_message(event.reply_token, message)

        # !tw - Retrieve latest Tweet from specified username
        elif check.group(1) == "!tw":
            check = re.match(r"!tw\s(\w+)?\s?(\d+)?", event.message.text)

            # Check for count
            if check.group(2) is None or int(check.group(2)) < 0:
                i = 0
            else:
                i = int(check.group(2))

            # Check for user's existence
            try:
                obj = self.tw.statuses.user_timeline(screen_name=check.group(1), count=i + 1)

                text = TextSendMessage(
                    text="@{0} ({1})\n\n{2}".format(obj[i]['user']['screen_name'], obj[i]['created_at'],
                                                    obj[i]['text']))

                # Check for video
                try:
                    video = VideoSendMessage(
                        original_content_url='{0}'.format(
                            obj[i]['extended_entities']['media'][0]['video_info']['variants'][0]['url']),
                        preview_image_url='{0}'.format(
                            obj[i]['entities']['media'][0]['media_url_https']))
                    self.line_bot_api.reply_message(event.reply_token, [text, video])

                # If no video is posted, check for image.
                except KeyError:
                    try:
                        image = ImageSendMessage(
                            original_content_url=obj[i]['entities']['media'][0]['media_url_https'],
                            preview_image_url=obj[i]['entities']['media'][0]['media_url_https'])
                        self.line_bot_api.reply_message(event.reply_token, [text, image])

                    # If no image is posted, send text only.
                    except KeyError:
                        self.line_bot_api.reply_message(event.reply_token, text)

            # If user is not found.
            except:
                message = TextSendMessage(
                    text="User not found.")
                self.line_bot_api.reply_message(event.reply_token, message)

    # DeviantArt search, multiple tries or else not found
    def dvart(self, event, loop, max, search):
        while loop < 10:
            send = ""
            deviations = []
            fetched_deviations = self.da.browse(endpoint='newest', q=search, limit=1, offset=randint(0, max))
            deviations += fetched_deviations['results']
            for deviation in deviations:
                send += "{0}".format(deviation.content)

            message = re.match(r"{'src': '(\w.+)',", send)
            if message is not None:
                image = ImageSendMessage(original_content_url=message.group(1),
                                         preview_image_url=message.group(1))
                self.line_bot_api.reply_message(event.reply_token, image)
                loop = 10
            else:
                if loop == 9:
                    message = TextSendMessage(text="Not Found.")
                    self.line_bot_api.reply_message(event.reply_token, message)
                    loop += 1
                else:
                    self.dvart(event, loop + 1, max // 3, search)

    # Image reply function
    def reply(self, event, *tag):
        for post in self.client.post_list(tags=tag, limit=1, random=True):
            try:
                image = ImageSendMessage(original_content_url=post['file_url'],
                                         preview_image_url=post['file_url'])
                self.line_bot_api.reply_message(event.reply_token, image)
            except KeyError:
                message = TextSendMessage(text="Too Lewd!")
                self.line_bot_api.reply_message(event.reply_token, message)
