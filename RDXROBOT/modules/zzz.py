import os
import random
from unidecode import unidecode
from PIL import ImageDraw, Image, ImageFont, ImageChops
from pyrogram import *
from pyrogram.types import *
from logging import getLogger

from RDXROBOT import pbot as app

from RDXROBOT.database.wel_db import *

COMMAND_HANDLER = ". /".split() # COMMAND HANDLER

LOGGER = getLogger(__name__)

class temp:
    ME = None
    CURRENT = 2
    CANCEL = False
    MELCOW = {}
    U_NAME = None
    B_NAME = None

def circle(pfp, size=(450, 450)):
    pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp

def welcomepic(pic, user, chat, id, uname):
    background = Image.open("RDXROBOT/resources/bg.jpg")
    pfp = Image.open(pic).convert("RGBA")
    pfp = circle(pfp)
    pfp = pfp.resize(
        (450, 450)
    ) 
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype('RDXROBOT/resources/SwanseaBold-D0ox.ttf', size=40)
    welcome_font = ImageFont.truetype('RDXROBOT/resources/SwanseaBold-D0ox.ttf', size=60)
    draw.text((30, 300), f'NAME: {unidecode(user)}', fill=(255, 255, 255), font=font)
    draw.text((30, 370), f'ID: {id}', fill=(255, 255, 255), font=font)
    draw.text((30, 40), f"Welcome to {unidecode(chat)}", fill=(225, 225, 225), font=welcome_font)
    draw.text((30,430), f"USERNAME : {uname}", fill=(255,255,255),font=font)
    pfp_position = (770, 140)  
    background.paste(pfp, pfp_position, pfp)  
    background.save(
        f"downloads/welcome#{id}.png"
    )
    return f"downloads/welcome#{id}.png"


@app.on_message(filters.command("zwelcome", COMMAND_HANDLER) & ~filters.private)
async def auto_state(_, message):
    usage = "**๏ ᴜsᴀɢᴇ ➠ **/zwelcome [ᴇɴᴀʙʟᴇ|ᴅɪsᴀʙʟᴇ]"
    if len(message.command) == 1:
        return await message.reply_text(usage)
    chat_id = message.chat.id
    user = await app.get_chat_member(message.chat.id, message.from_user.id)
    if user.status in (
        enums.ChatMemberStatus.ADMINISTRATOR,
        enums.ChatMemberStatus.OWNER,
    ):
      A = await wlcm.find_one({"chat_id" : chat_id})
      state = message.text.split(None, 1)[1].strip()
      state = state.lower()
      if state == "enable":
        if A:
           return await message.reply_text("๏ sᴘᴇᴄɪᴀʟ ᴡᴇʟᴄᴏᴍᴇ ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ")
        elif not A:
           await add_wlcm(chat_id)
           await message.reply_text(f"๏ ᴇɴᴀʙʟᴇᴅ sᴘᴇᴄɪᴀʟ ᴡᴇʟᴄᴏᴍᴇ ɪɴ {message.chat.title}")
      elif state == "disable":
        if not A:
           return await message.reply_text("๏ sᴘᴇᴄɪᴀʟ ᴡᴇʟᴄᴏᴍᴇ ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ")
        elif A:
           await rm_wlcm(chat_id)
           await message.reply_text(f"๏ ᴅɪsᴀʙʟᴇᴅ sᴘᴇᴄɪᴀʟ ᴡᴇʟᴄᴏᴍᴇ ɪɴ {message.chat.title}")
      else:
        await message.reply_text(usage)
    else:
        await message.reply("๏ ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ")

@app.on_chat_member_updated(filters.group, group=-3)
async def greet_group(_, member: ChatMemberUpdated):
    chat_id = member.chat.id
    A = await wlcm.find_one({"chat_id" : chat_id})
    if not A:
       return
    if (
        not member.new_chat_member
        or member.new_chat_member.status in {"banned", "left", "restricted"}
        or member.old_chat_member
    ):
        return
    user = member.new_chat_member.user if member.new_chat_member else member.from_user
    try:
        pic = await app.download_media(
            user.photo.big_file_id, file_name=f"pp{user.id}.png"
        )
    except AttributeError:
        pic = "HuTao/resources/profilepic.jpg"
    if (temp.MELCOW).get(f"welcome-{member.chat.id}") is not None:
        try:
            await temp.MELCOW[f"welcome-{member.chat.id}"].delete()
        except Exception as e:
            LOGGER.error(e)
    try:
        welcomeimg = welcomepic(
            pic, user.first_name, member.chat.title, user.id, user.username
        )
        temp.MELCOW[f"welcome-{member.chat.id}"] = await app.send_photo(
            member.chat.id,
            photo=welcomeimg,
            caption= f"""
**❀ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ {member.chat.title} ɢʀᴏᴜᴘ ❀

๏ ɴᴀᴍᴇ ➠ {user.mention}
๏ ɪᴅ ➠ {user.id}
๏ ᴜsᴇʀɴᴀᴍᴇ ➠ @{user.username}
๏ ᴍᴀᴅᴇ ʙʏ ➠ [ʀᴏʏ-ᴇᴅɪᴛx](https://t.me/roy_editx)**
""",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton (f"ᴠɪᴇᴡ ᴜsᴇʀ", url=f"https://t.me/{user.username}")]])

            )
    except Exception as e:
        LOGGER.error(e)
    try:
        os.remove(f"downloads/welcome#{user.id}.png")
        os.remove(f"downloads/pp{user.id}.png")
    except Exception as e:
        return 


__mod_name__ = "ᴢ-ᴡᴇʟᴄᴏᴍᴇ"
__help__ = """
 ❍ ᴛʜɪs ɪs sᴘᴇᴄɪᴀʟ ᴡᴇʟᴄᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs.

 ❍ /zwelcome <enable> ➛ ᴇɴᴀʙʟᴇ sᴘᴇᴄɪᴀʟ ᴡᴇʟᴄᴏᴍᴇ.
 ❍ /zwelcome <disable> ➛ ᴅɪsᴀʙʟᴇ sᴘᴇᴄɪᴀʟ ᴡᴇʟᴄᴏᴍᴇ.
 """
