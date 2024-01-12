import requests as r
from pyrogram import filters
from MukeshRobot import pbot
from Mukesh Robot.utils.errors import capture_err
from Mukesh Robot.utils.http import get, resp_get



@pbot.on_message(filters.command("meow"))
@capture_err
async def randomcat(_, message):
    cat = await get("https://aws.random.cat/meow")
    await message.reply_photo(cat.get("file"))

@pbot.on_message(filters.command("woof"))
async def woof(_, message):
        rr = r.get("https://random.dog/woof.json").json()

        A = rr["url"]
        await message.reply_photo(A)

__MODULE__ = "CAT-DOG"
__HELP__ = """
 » `/meow`- ᴛᴏ ɢᴇᴛ ʀᴀɴᴅᴏᴍ ᴘʜᴏᴛᴏ ᴏꜰ ᴄᴀᴛ.
 » `/dog` - ᴛᴏ ɢᴇᴛ ʀᴀɴᴅᴏᴍ ᴘʜᴏᴛᴏ ᴏꜰ ᴅᴏɢ.
"""
