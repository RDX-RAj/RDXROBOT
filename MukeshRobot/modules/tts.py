"""
STATUS: Code is working. ✅
"""

"""
GNU General Public License v3.0

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

Credits:-
    I don't know who originally wrote this code. If you originally wrote this code, please reach out to me. 

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import os

from gtts import gTTS
from gtts import gTTSError
from telethon import *
from telethon.tl.types import *

from MukeshRobot import *

from MukeshRobot import telethn as tbot
from MukeshRobot.events import register


@register(pattern="^/tts (.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await event.reply(
            "❍ ɪɴᴠᴀʟɪᴅ sʏɴᴛᴀx\n\n❍ ғᴏʀᴍᴀᴛ `/tts lang | text`\n\n❍ ғᴏʀ ᴇɢ : `/tts en | hello`"
        )
        return
    text = text.strip()
    lan = lan.strip()
    try:
        tts = gTTS(text, tld="com", lang=lan)
        tts.save("avisha.mp3")
    except AssertionError:
        await event.reply(
            "❍ ᴛʜᴇ ᴛᴇxᴛ ɪs ᴇᴍᴘᴛʏ.\n"
            "❍ ɴᴏᴛʜɪɴɢ ʟᴇғᴛ ᴛᴏ sᴘᴇᴀᴋ ᴀғᴛᴇʀ ᴘʀᴇ-ᴘʀᴇᴄᴇssɪɴɢ, "
            "❍ ᴛᴏᴋᴇɴɪᴢɪɴɢ ᴀɴᴅ ᴄʟᴇᴀɴɪɴɢ."
        )
        return
    except ValueError:
        await event.reply("❍ ʟᴀɴɢᴜᴀɢᴇ ɪs ɴᴏᴛ sᴜᴘᴘᴏʀᴛᴇᴅ.")
        return
    except RuntimeError:
        await event.reply("❍ ᴇʀʀᴏʀ ʟᴏᴀᴅɪɴɢ ᴛʜᴇ ʟᴀɴɢᴜᴀɢᴇs ᴅɪᴄᴛɪᴏɴᴀʀʏ.")
        return
    except gTTSError:
        await event.reply("❍ ᴇʀʀᴏʀ ɪɴ ɢᴏᴏɢʟᴇ ᴛᴇxᴛ-ᴛᴏ-sᴘᴇᴇᴄʜ ᴀᴘɪ ʀᴇǫᴜᴇsᴛ !")
        return
    with open("avisha.mp3", "r"):
        await tbot.send_file(
            event.chat_id, "avisha.mp3", voice_note=True, reply_to=reply_to_id
        )
        os.remove("avisha.mp3")

__mod_name__ = "ɢᴛᴛs"
__help__ = """
❍ ғᴏʀᴍᴀᴛ ➛ `/tts lang | text`

❍ ғᴏʀ ᴇɢ ➛ /tts en | hello
"""
