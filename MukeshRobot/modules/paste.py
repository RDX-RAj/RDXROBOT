import asyncio
import os
import re

import aiofiles
from pykeyboard import InlineKeyboard
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton

from MukeshRobot import aiohttpsession as session
from MukeshRobot import pbot as app
from MukeshRobot.utils.errors import capture_err
from MukeshRobot.utils.pastebin import paste

pattern = re.compile(r"^text/|json$|yaml$|xml$|toml$|x-sh$|x-shellscript$")


async def isPreviewUp(preview: str) -> bool:
    for _ in range(7):
        try:
            async with session.head(preview, timeout=2) as resp:
                status = resp.status
                size = resp.content_length
        except asyncio.exceptions.TimeoutError:
            return False
        if status == 404 or (status == 200 and size == 0):
            await asyncio.sleep(0.4)
        else:
            return True if status == 200 else False
    return False


@app.on_message(filters.command("paste"))
@capture_err
async def paste_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("❍ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ /paste")
    m = await message.reply_text("🖨️")
    if message.reply_to_message.text:
        content = str(message.reply_to_message.text)
    elif message.reply_to_message.document:
        document = message.reply_to_message.document
        if document.file_size > 1048576:
            return await m.edit("❍ ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ᴘᴀsᴛᴇ ғɪʟᴇs sᴍᴀʟʟᴇʀ ᴛʜᴀɴ 1MB.")
        if not pattern.search(document.mime_type):
            return await m.edit("❍ ᴏɴʟʏ ᴛᴇxᴛ ғɪʟᴇs ᴄᴀɴ ʙᴇ ᴘᴀsᴛᴇᴅ.")
        doc = await message.reply_to_message.download()
        async with aiofiles.open(doc, mode="r") as f:
            content = await f.read()
        os.remove(doc)
    link = await paste(content)
    preview = link 
    button = InlineKeyboard(row_width=1)
    button.add(InlineKeyboardButton(text="ᴘᴀsᴛᴇ ʟɪɴᴋ", url=link))

    await m.delete()
    try:
        await message.reply("❍ ʜᴇʀᴇ ɪs ʏᴏᴜʀ ᴘᴀsᴛᴇ ʟɪɴᴋ ", quote=False, reply_markup=button)
        
    except Exception:
        pass
    


__mod_name__ = "ᴘᴀsᴛᴇ"
__help__ = """
 ❍ ᴘᴀsᴛᴇs ᴛʜᴇ ɢɪᴠᴇɴ ғɪʟᴇ ᴀɴᴅ sʜᴏᴡs ʏᴏᴜ ᴛʜᴇ ʀᴇsᴜʟᴛ

 ❍ /paste *➛* ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ғɪʟᴇ
 """
    
