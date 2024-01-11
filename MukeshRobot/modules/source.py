from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from MukeshRobot import OWNER_ID, dispatcher
from MukeshRobot import pbot as client

Mukesh = "https://telegra.ph/file/6f04cb09ff8e8af19ae02.jpg"


@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=Mukesh,
        caption=f"""**❍ ʜᴇʏ {message.from_user.mention()}, ᴡᴇʟᴄᴏᴍᴇ ʙᴀʙʏ !\n\n❍ ɪ ᴀᴍ [{dispatcher.bot.first_name}](t.me/{dispatcher.bot.username})**\n\n❍ **ɪғ ʏᴏᴜ ᴡᴀɴᴛ ๛ᴀ ᴠ ɪ s ʜ ᴀ ༗ ʙᴏᴛ ʀᴇᴘᴏ, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʀᴇᴘᴏ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴏᴡɴᴇʀ",user_id=OWNER_ID
                    ),
                    InlineKeyboardButton(
                        "ʀᴇᴘᴏ",
                        url="https://x-hd.video/video/-aubree-valentine-switch-roles-fta-reality-kings.html",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "ʀᴇᴩᴏ"
_help__ = """
 /repo  ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ 
 /source ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ
"""
