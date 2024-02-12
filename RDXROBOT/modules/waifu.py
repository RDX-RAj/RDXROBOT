"""
STATUS: Code is working. ✅
"""

"""
BSD 2-Clause License

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

# Created By: https://telegram.dog/SOME1_HING 
# Assisted By: https://telegram.dog/SastaDev from https://telegram.dog/SastaNetwork

# Imports from external libraries. (DON'T EDIT)
import requests
from telegram import ParseMode
from telegram.ext import CommandHandler

import random
# Imports dispatcher = updater.dispatcher from __init__.py (*MUST EDIT* CHANGE MODULE NAME TO THE FOLDER NAME OF MODULES IN YOUR BOT)
from RDXROBOT import dispatcher

# Main code, Credit to https://github.com/itspro-dev for making the API. 

def waifu(update, context):
    try:
        msg = update.effective_message
        # API (DON'T EDIT)
        url = f'https://api.animeepisode.org/waifu/'
        result = requests.get(url).json()
        img = result['Character_Image']
        # Message (EDIT THIS PART AS HTML *IF YOU WANT*)
        text = f'''
<b>❍ ɴᴀᴍᴇ ➛</b> <code>{result['Character_Name']}</code>
        
<b>❍ ᴀɴɪᴍᴇ ➛</b> <code>{result['Anime_name']}</code>
'''
        msg.reply_photo(photo=img, caption=text, parse_mode=ParseMode.HTML)

    except Exception as e:
        text = f'<b>❍ ᴇʀʀᴏʀ</b> ➛ <code>' + e + '</code>'
        msg.reply_text(text, parse_mode=ParseMode.HTML)


# Code Handler (YOU CAN CHANGE 'waifu' TO ANY 'cmd' FOR THIS TO BE WORKED AS '/cmd' *IF YOU WANT*.)
WAIFUINFO_HANDLER = CommandHandler('waifuinfo', waifu, run_async=True)
dispatcher.add_handler(WAIFUINFO_HANDLER)

#  Buttons for /help .
__mod_name__ = "ᴡᴀɪғᴜs"
__help__ = '''
   ❍ `/waifu`* ➛* sᴇɴᴅs ʟɪᴍɪᴛᴇᴅ ʙᴜᴛ ʙᴇsᴛ ᴡᴀɪғᴜ ɪᴍᴀɢᴇ.
   
   ❍ `/waifuinfo`*➛* ɢɪᴠᴇs ʀᴀɴᴅᴏᴍ ɪᴍᴀɢᴇ ᴏғ ᴡᴀɪғᴜ ᴡɪᴛʜ ɪɴғᴏ. 

   ✿ *ɴsғᴡ ᴄᴏɴᴛᴇɴᴛ* ✿
   
   ❍ `/nsfwwaifu`
   ❍ `/nwaifu`  
'''

# DON'T EDIT
__handlers__ = [WAIFUINFO_HANDLER]
