from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import Message
from MukeshRobot import (
    BOT_NAME,
    BOT_USERNAME,
    LOGGER,
    OWNER_ID,
    START_IMG,
    SUPPORT_CHAT,
    TOKEN,
    StartTime,
    dispatcher,
    pbot,
    telethn,
    updater,
    MONGO_DB_URI,
    API_ID,
    API_HASH
)

from MukeshRobot import BOT_NAME,OWNER_ID
from MukeshRobot import pbot as app
@app.on_message(
    filters.command(["con", "var"]) & filters.user(OWNER_ID)
)
async def get_vars(_, message: Message):
    try:
        await app.send_message(
            chat_id=int(OWNER_ID),
            text=f"""✦ **{BOT_NAME} ᴄᴏɴғɪɢ ᴠᴀʀɪᴀʙʟᴇs** ✦

**❍ ʙᴏᴛ ᴛᴏᴋᴇɴ ➛** `{TOKEN}`
**❍ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ ➛** `{SUPPORT_CHAT}`
**❍ sᴛᴀʀᴛ ɪᴍᴀɢᴇ ➛** `{START_IMG}`
**❍ ᴀᴘɪ ɪᴅ ➛** `{API_ID}`
**❍ ᴀᴘɪ ʜᴀsʜ ➛** `{API_HASH}` 
**❍ ᴍᴏɴɢᴏ ᴜʀʟ ➛** `{MONGO_DB_URI}`   




""")
    except:
        return await message.reply_text("❍ ғᴀɪʟᴇᴅ ᴛᴏ sᴇɴᴅ ᴛʜᴇ ᴄᴏɴғɪɢ ᴠᴀʀɪᴀʙʟᴇs.")
    if message.chat.type != ChatType.PRIVATE:
        await message.reply_text(
            "❍ ᴘʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘᴍ, ɪ'ᴠᴇ sᴇɴᴛ ᴛʜᴇ ᴄᴏɴғɪɢ ᴠᴀʀɪᴀʙʟᴇs ᴛʜᴇʀᴇ."
        )
        
