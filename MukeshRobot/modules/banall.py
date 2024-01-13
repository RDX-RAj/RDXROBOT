"""
GNU General Public License v3.0

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

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

from telethon.tl.types import ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest
from telethon import events
from MukeshRobot import telethn as tbot, DEV_USERS

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

@tbot.on(events.NewMessage(pattern="/banall$"))
async def banall(hmm):
    if not hmm.is_group:
        return
    if hmm.is_group:
        if hmm.sender_id not in DEV_USERS:
            return
    async for user in tbot.iter_participants(hmm.chat_id):
        if not user.deleted:
            try:
                await hmm.client(
                        EditBannedRequest(hmm.chat_id, user.id, BANNED_RIGHTS)
                    )
            except:
                pass
