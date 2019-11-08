from flask import Flask, request, abort
from classes.bot import BotClass
import os

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import *
from linebot.models import *
from pybooru import Danbooru
import deviantart
import praw
from twitter import *
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

app = Flask(__name__)

# Tokens
handler = WebhookHandler('LINE ChannelSecret')
line = LineBotApi('LINE ChannelAccess')
reddit = praw.Reddit(client_id='REDDIT Client',
                     client_secret="REDDIT Secret", user_agent='REDDIT UserAgent')
dvart = deviantart.Api('DVART Channel', 'DVART Secret')
tw = Twitter(
    auth=OAuth('TWITTER token', 'TWITTER token_secret', 'TWITTER consumer_key', 'TWITTER consumer_secret'))
youtube = build("youtube", "v3", developerKey="GOOGLE API KEY")

# Initialize bot
bot = BotClass(line, reddit, dvart, tw, youtube)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# Runs when a message is received
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # message = TextSendMessage(text=event.message.text)
    # line_bot_api.reply_message(event.reply_token, message)

    # ! Bot Command
    if event.message.text[0] == '!':
        bot.check(event)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
