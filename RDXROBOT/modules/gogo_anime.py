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

from gogoanimeapi import gogoanime as anime
from telethon import Button, events

from RDXROBOT import telethn


@telethn.on(events.NewMessage(pattern="^/gogo ?(.*)"))
async def gogo(event):
    args = event.pattern_match.group(1)
    if not args:
        return await event.respond(
            "❍ ʏᴏᴜʀ ǫᴜᴇʀʏ sʜᴏᴜʟᴅ ʙᴇ ɪɴ ᴛʜɪs ғᴏʀᴍᴀᴛ : /search <space> ɴᴀᴍᴇ ᴏғ ᴛʜᴇ ᴀɴɪᴍᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴇᴀʀᴄʜ."
        )
    result = anime.get_search_results(args)
    buttons = []
    for i in result:
        k = [Button.inline(f'{i["name"]}', data=f'search_{i["animeid"]}')]
        buttons.append(k)
        if len(buttons) == 99:
            break
    await event.reply("search", buttons=buttons)


@telethn.on(events.CallbackQuery(pattern=r"search(\_(.*))"))
async def search(event):
    tata = event.pattern_match.group(1)
    data = tata.decode()
    input = data.split("_", 1)[1]
    animeid = input
    await event.answer("❍ ғᴇᴛᴄʜɪɴɢ ᴀɴɪᴍᴇ ᴅᴇᴛᴀɪʟs.")
    result = anime.get_anime_details(animeid)
    episodes = result["episodes"]
    nfo = f"{animeid}?{episodes}"
    buttons = Button.inline("Download", data=f"episode_{nfo}")
    text = """
❍ {} (ʀᴇʟᴇᴀsᴇᴅ ➛ {})
❍ ᴛʏᴘᴇ ➛ {}
❍ sᴛᴀᴛᴜs ➛ {}
❍ ɢᴇɴᴇʀɪᴇs ➛ {}
❍ ᴇᴘɪsᴏᴅᴇs ➛ {}
❍ sᴜᴍᴍᴀʀʏ ➛ {}
"""
    await event.edit(
        text.format(
            result["title"],
            result["year"],
            result["type"],
            result["status"],
            result["genre"],
            result["episodes"],
            result["plot_summary"],
        ),
        buttons=buttons,
    )


@telethn.on(events.CallbackQuery(pattern=r"episode(\_(.*))"))
async def episode(event):
    tata = event.pattern_match.group(1)
    data = tata.decode()
    input = data.split("_", 1)[1]
    animeid, episodes = input.split("?", 1)
    animeid = animeid.strip()
    epsd = int(episodes.strip())
    buttons = []
    cbutton = []
    for i in range(epsd):
        nfo = f"{i}?{animeid}"
        button = Button.inline(f"{i}", data=f"download_{nfo}")
        buttons.append(button)
        if len(buttons) == 4:
            cbutton.append(buttons)
            buttons = []
    text = f"❍ ʏᴏᴜ sᴇʟᴇᴄᴛᴇᴅ {animeid},\n\n❍ sᴇʟᴇᴄᴛ ᴛʜᴇ ᴇᴘɪsᴏᴅᴇ ʏᴏᴜ ᴡᴀɴᴛ."
    await event.edit(text, buttons=cbutton)


@telethn.on(events.CallbackQuery(pattern=r"download(\_(.*))"))
async def episode(event):
    tata = event.pattern_match.group(1)
    data = tata.decode()
    input = data.split("_", 1)[1]
    imd, episode = input.split("?", 1)
    animeid = episode.strip()
    epsd = imd.strip()
    result = anime.get_episodes_link(animeid, epsd)
    text = f"❍ ʏᴏᴜ ᴀʀᴇ ᴡᴀᴛᴄʜɪɴɢ ᴇᴘɪsᴏᴅᴇ {epsd} ᴏғ {animeid}\n\n❍ ɴᴏᴛᴇ : sᴇʟᴇᴄᴛ ʜᴅᴘ ʟɪɴᴋ ғᴏʀ ғᴀsᴛᴇʀ sᴛʀᴇᴀᴍɪɴɢ."

    butons = []
    cbutton = []
    for i in result:
        if i != "title":
            k = Button.url(f"{i}", f"{result[i]}")
            butons.append(k)
            if len(butons) == 1:
                cbutton.append(butons)
                butons = []
    await event.edit(text, buttons=cbutton)
