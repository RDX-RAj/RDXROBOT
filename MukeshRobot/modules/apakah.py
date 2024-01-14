import random
from MukeshRobot.events import register
from MukeshRobot import telethn

APAKAH_STRING = [
    "ɪʏᴀ",
    "ᴛɪᴅᴀᴋ",
    "ᴍᴜɴɢᴋɪɴ",
    "ᴍᴜɴɢᴋɪɴ ᴛɪᴅᴀᴋ",
    "ʙɪsᴀ ᴊᴀᴅɪ",
    "ᴍᴜɴɢᴋɪɴ ᴛɪᴅᴀᴋ",
    "ᴛɪᴅᴀᴋ ᴍᴜɴɢᴋɪɴ",
    "ʏɴᴛᴋᴛs",
    "ᴘᴀʟᴀ ʙᴀᴘᴀᴋ ᴋᴀᴜ ᴘᴇᴄᴀʜ",
    "ᴀᴘᴀ ɪʏᴀ?",
    "ᴛᴀɴʏᴀ ᴀᴊᴀ sᴀᴍᴀ ᴍᴀᴍᴀᴋ ᴋᴀᴜ ᴛᴜ ᴘʟᴇʀ",
]


@register(pattern="^/apakah ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply("❍ ʙᴇʀɪᴋᴀɴ sᴀʏᴀ ᴘᴇʀᴛᴀɴʏᴀᴀɴ 😐")
        return
    await event.reply(random.choice(APAKAH_STRING))

__mod_name__ = "ᴀᴘᴀᴋᴀʜ"
__help__ = """
 ❍ /apakah ➛ ᴄʜᴇᴄᴋ ᴀᴘᴀᴋᴀʜ sᴛᴀᴛᴜs.
 """
