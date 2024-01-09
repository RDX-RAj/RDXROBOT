import requests
from .. import pbot as Mukesh,BOT_NAME,BOT_USERNAME
import time
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
@Mukesh.on_message(filters.command("mahadev"))
async def Mahadev(bot, message):
    try:
        
        await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO) 
        response = requests.get(f'https://mukesh-api.vercel.app/mahadev') 
        x=response.json()["results"]
            
        await message.reply_photo(photo=x,caption=f" \n๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➛ [๛ᴀ ᴠ ɪ s ʜ ᴀ ༗](https://t.me/avishaxbot) ", parse_mode=ParseMode.MARKDOWN)     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ: {e} ")
@Mukesh.on_message(filters.command("uselessfact"))
async def uselessa_fact(bot, message):
    try:
        
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING) 
        response = requests.get(f'https://mukesh-api.vercel.app/uselessfact') 
        x=response.json()["results"]
            
        await message.reply_text(x, parse_mode=ParseMode.MARKDOWN)     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ: {e} ")
