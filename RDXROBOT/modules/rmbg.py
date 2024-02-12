# Created By :- @ImmortalsXKing
# Change The repo according to your repo name
# Don't change anything else


import os
import aiohttp
import aiofiles
from aiohttp import ContentTypeError
from RDXROBOT import pbot as app
from pyrogram import filters

def check_filename(filroid):
    if os.path.exists(filroid):
        no = 1
        while True:
            ult = "{0}_{2}{1}".format(*os.path.splitext(filroid) + (no,))
            if os.path.exists(ult):
                no += 1
            else:
                return ult
    return filroid

async def RemoveBG(input_file_name):
    headers = {"X-API-Key": "u4x2416NAQVefYsfwbzrw7VE"}
    files = {"image_file": open(input_file_name, "rb").read()}
    async with aiohttp.ClientSession() as ses:
        async with ses.post(
            "https://api.remove.bg/v1.0/removebg", headers=headers, data=files
        ) as y:
            contentType = y.headers.get("content-type")
            if "image" not in contentType:
                return False, (await y.json())

            name = check_filename("alpha.png")
            file = await aiofiles.open(name, "wb")
            await file.write(await y.read())
            await file.close()
            return True, name


@app.on_message(filters.command("rmbg"))
async def rmbg(bot, message):
  rmbg = await message.reply("💥") 
  replied = message.reply_to_message
  if not replied:
      return await rmbg.edit("**❍ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴛᴏ ʀᴇᴍᴏᴠᴇ ɪᴛ's ʙᴀᴄᴋɢʀᴏᴜᴅ.**")

  if replied.photo:
      photo = await bot.download_media(replied)
      x, y = await RemoveBG(photo)
      os.remove(photo)
      if not x:
          bruh = y["errors"][0]
          details = bruh.get("detail", "")
          return await rmbg.edit(f"**❍ ᴇʀʀᴏʀ ~** `{bruh['title']}`,\n❍ {details}")
      await message.reply_photo(photo=y,caption="**❍ ʜᴇʀᴇ ɪs ʏᴏᴜʀ ɪᴍᴀɢᴇ ᴡɪᴛʜᴏᴜᴛ ʙᴀᴄᴋɢʀᴏᴜɴᴅ.**")
      await message.reply_document(document=y)
      await rmbg.delete()
      return os.remove(y)
  await rmbg.edit("**❍ ʀᴇᴘʟʏ ᴏɴʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴛᴏ ʀᴇᴍᴏᴠᴇ ɪᴛ's ʙᴀᴄᴋɢʀᴏᴜɴᴅ.**")

__mod_name__ = "ʙɢʀᴍ"
__help__ = """
 ❍ /rmbg ➛ ʀᴇᴘʟʏ ᴏɴʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴛᴏ ʀᴇᴍᴏᴠᴇ ɪᴛ's ʙᴀᴄᴋɢʀᴏᴜɴᴅ.
 """
 
