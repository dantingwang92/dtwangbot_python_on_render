# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 22:31:11 2023

@author: Administrator
"""

#載入LineBot所需要的模組 
from flask import Flask, request, abort  

from linebot import (
    LineBotApi, WebhookHandler
)

from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)  
# 必須放上自己的Channel Access Token 
line_bot_api = LineBotApi('W5sEiFJScoUkTHYX/XVjofwRBCj4KRnTveLBjkHvFku9910686iD80PSkXMZfVW4g3IgZBU3D5FL9QZ/QG6WFZgqw0mXvoKOEGvfto+8642cI90kAtNwTYdnaur55Nr+c8sE0cvDJTtWNnAVniObuwdB04t89/1O/w1cDnyilFU=')  
# 必須放上自己的Channel Secret
handler = WebhookHandler('935a71727b14589a7f700885e73d00d5')

#訊息傳遞區塊 
##### 基本上程式編輯都在這個function ##### 
@handler.add(MessageEvent, message=TextMessage) 
def handle_message(event):     
    message = event.message.text
    line_bot_api.reply_message(event.reply_token,TextSendMessage(message))

#主程式 
import os 
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))     
    app.run(host='0.0.0.0', port=port)