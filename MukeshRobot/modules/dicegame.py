from pyrogram import Client, enums, filters
#from config import *
import asyncio
from MukeshRobot import pbot as mukesh

from pyrogram.handlers import MessageHandler


@mukesh.on_message(filters.command("dice"))
async def dice(bot, message):
    x=await bot.send_dice(message.chat.id)
    m=x.dice.value
    await message.reply_text(f"❍ ʜᴇʏ {message.from_user.mention} ʏᴏᴜʀ sᴄᴏʀᴇ ɪs : {m}",quote=True)
  
@mukesh.on_message(filters.command("dart"))
async def dart(bot, message):
    x=await bot.send_dice(message.chat.id, "🎯")
    m=x.dice.value
    await message.reply_text(f"❍ ʜᴇʏ {message.from_user.mention} ʏᴏᴜʀ sᴄᴏʀᴇ ɪs ➛ {m}",quote=True)

@mukesh.on_message(filters.command("basket"))
async def basket(bot, message):
    x=await bot.send_dice(message.chat.id, "🏀")
    m=x.dice.value
    await message.reply_text(f"❍ ʜᴇʏ {message.from_user.mention} ʏᴏᴜʀ sᴄᴏʀᴇ ɪs ➛ {m}",quote=True)
@mukesh.on_message(filters.command("jackpot"))
async def basket(bot, message):
    x=await bot.send_dice(message.chat.id, "🎰")
    m=x.dice.value
    await message.reply_text(f"❍ ʜᴇʏ {message.from_user.mention} ʏᴏᴜʀ sᴄᴏʀᴇ ɪs ➛ {m}",quote=True)
@mukesh.on_message(filters.command("ball"))
async def basket(bot, message):
    x=await bot.send_dice(message.chat.id, "🎳")
    m=x.dice.value
    await message.reply_text(f"❍ ʜᴇʏ {message.from_user.mention} ʏᴏᴜʀ sᴄᴏʀᴇ ɪs ➛ {m}",quote=True)
@mukesh.on_message(filters.command("football"))
async def basket(bot, message):
    x=await bot.send_dice(message.chat.id, "⚽")
    m=x.dice.value
    await message.reply_text(f"❍ ʜᴇʏ {message.from_user.mention} ʏᴏᴜʀ sᴄᴏʀᴇ ɪs ➛ {m}",quote=True)
__help__ = """
✦ ᴘʟᴀʏ ɢᴀᴍᴇ ᴡɪᴛʜ ᴇᴍᴏᴊɪs ✦

❍ /dice ➛ ᴅɪᴄᴇ 🎲
❍ /dart ➛ ᴅᴀʀᴛ 🎯
❍ /basket ➛ ʙᴀsᴋᴇᴛ ʙᴀʟʟ 🏀
❍ /ball ➛ ʙᴏᴡʟɪɴɢ ʙᴀʟʟ 🎳
❍ /football ➛ ғᴏᴏᴛʙᴀʟʟ ⚽
❍ /jackpot ➛ sᴘɪɴ sʟᴏᴛ ᴍᴀᴄʜɪɴᴇ 🎰
 """

__mod_name__ = "ɢᴀᴍᴇ"
