"""
BSD 2-Clause License

Copyright (C) 2017-2019, Paul Larsen
Copyright (C) 2021-2022, Awesome-RJ, [ https://github.com/Awesome-RJ ]
Copyright (c) 2021-2022, Yūki • Black Knights Union, [ https://github.com/Awesome-RJ/CutiepiiRobot ]

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

import random

from telegram import ParseMode
from telethon import Button

from MukeshRobot import OWNER_ID, SUPPORT_CHAT
from MukeshRobot import telethn as tbot

from ..events import register


@register(pattern="/feedback ?(.*)")
async def feedback(e):
    quew = e.pattern_match.group(1)
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
    HOTTIE = (
        "https://graph.org/file/f86b71018196c5cfe7344.jpg",
        "https://graph.org/file/a3db9af88f25bb1b99325.jpg",
        "https://graph.org/file/5b344a55f3d5199b63fa5.jpg",
        "https://graph.org/file/84de4b440300297a8ecb3.jpg",
        "https://graph.org/file/84e84ff778b045879d24f.jpg",
        "https://graph.org/file/a4a8f0e5c0e6b18249ffc.jpg",
        "https://graph.org/file/ed92cada78099c9c3a4f7.jpg",
        "https://graph.org/file/d6360613d0fa7a9d2f90b.jpg",
    )
    FEED = ("https://graph.org/file/d6360613d0fa7a9d2f90b.jpg", )
    BUTTON = [[
        Button.url("ɢᴏ ᴛᴏ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", f"https://t.me/{SUPPORT_CHAT}")
    ]]
    TEXT = "✦ ᴛʜᴀɴᴋs ғᴏʀ ʏᴏᴜʀ ғᴇᴇᴅʙᴀᴄᴋ, ɪ ʜᴏᴘᴇ ʏᴏᴜ ʜᴀᴘᴘʏ ᴡɪᴛʜ ᴏᴜʀ sᴇʀᴠɪᴄᴇ."
    GIVE = "✦ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ғᴏʀ ғᴇᴇᴅʙᴀᴄᴋ."
    logger_text = f"""
**✦ ɴᴇᴡ ғᴇᴇᴅʙᴀᴄᴋ ✦**

**❍ ғʀᴏᴍ ᴜsᴇʀ ➛** {mention}
**❍ ᴜsᴇʀɴᴀᴍᴇ ➛** @{e.sender.username}
**❍ ᴜsᴇʀ ɪᴅ ➛** `{e.sender.id}`
**❍ ғᴇᴇᴅʙᴀᴄᴋ ➛** `{e.text}`

**❍ ᴘᴏᴡᴇʀᴇᴅ ʙʏ** ➛ [๛ᴀ ᴠ ɪ s ʜ ᴀ ༗](https://t.me/avishaxbot)
"""
    if user_id == 1926801217:
        await e.reply("**✦ sʀʏ ɪ ᴄᴀɴ'ᴛ ɪᴅᴇɴᴛɪғʏ ʏᴏᴜʀ ɪɴғᴏ.**",
                      parse_mode=ParseMode.MARKDOWN)
        return

    if user_id == 1087968824:
        await e.reply("**✦ ᴛᴜʀɴ ᴏғғ ᴜʀ ᴀɴᴏɴʏᴍᴏᴜs ᴍᴏᴅᴇ ᴀɴᴅ ᴛʀʏ.**",
                      parse_mode=ParseMode.MARKDOWN)
        return

    if e.sender_id != OWNER_ID and not quew:
        await e.reply(
            GIVE,
            parse_mode=ParseMode.MARKDOWN,
            buttons=BUTTON,
            file=random.choice(FEED),
        ),
        return

    await tbot.send_message(
        SUPPORT_CHAT,
        f"{logger_text}",
        file=random.choice(HOTTIE),
        link_preview=False,
    )
    await e.reply(TEXT, file=random.choice(HOTTIE), buttons=BUTTON)


__mod_name__ = "ғᴇᴇᴅʙᴀᴄᴋ"
__help__ = """
 ❍ /feedback ➛ ɢɪᴠᴇ ғᴇᴇᴅʙᴀᴄᴋ ᴛᴏ ᴀᴠɪsʜᴀ ʙᴏᴛ.
 """
