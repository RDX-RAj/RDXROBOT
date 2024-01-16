import requests
from MukeshRobot import pbot as mukesh
from pyrogram import filters

@mukesh.on_message(filters.command("hastag"))
async def hastag(bot, message):
    
    try:
        text = message.text.split(' ',1)[1]
        res = requests.get(f"https://mukesh-api.vercel.app/hastag/{text}").json()["results"]

    except IndexError:
        return await message.reply_text("❍ ᴇxᴀᴍᴘʟᴇ ➛ `/hastag python`")
        
    
    await message.reply_text(f"❍ ʜᴇʀᴇ ɪs ʏᴏᴜʀ  ʜᴀsᴛᴀɢ \n❍ <pre>{res}</pre>", quote=True)
    
__mod_name__ = "ʜᴀsʜᴛᴀɢ"
__help__= """
**❍ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʜᴀsʜᴛᴀɢ ɢᴇɴᴇʀᴀᴛᴏʀ ᴡʜɪᴄʜ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ ᴛʜᴇ ᴛᴏᴘ 𝟹𝟶 ᴀɴᴅ ᴍᴏʀᴇ ʜᴀsʜᴛᴀɢs ʙᴀsᴇᴅ ᴏғғ ᴏғ ᴏɴᴇ ᴋᴇʏᴡᴏʀᴅ sᴇʟᴇᴄᴛɪᴏɴ.**
❍ /hastag ➛ ᴇɴᴛᴇʀ ᴡᴏʀᴅ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ʜᴀsᴛᴀɢ.
❍ ᴇxᴀᴍᴘʟᴇ ➛ ` /hastag ᴘʏᴛʜᴏɴ `"""

