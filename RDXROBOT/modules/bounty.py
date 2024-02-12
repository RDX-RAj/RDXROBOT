# Author: Sasta Dev || https://t.me/SastaDev.
# Author's github: https://github.com/SastaDev.
# Github Repository: https://github.com/SastaDev/bounty.py.
# Created on: Friday, 05 May, 2023.
# Released on: Monday, 08 May, 2023.
# MIT LICENSE.
# Written in python using pyrogram.
# This python script works for both pyrogram versions (1.4 and older as well as 2.0 and newer).
# Original Bot Idea: @WantedBountyBot by Sasta Dev.
# © Sasta Dev ~ 2023.

import uuid
from pyrogram import Client, filters
from pyrogram.types import (InlineKeyboardMarkup, InlineKeyboardButton, Message)
import httpx

# Replace `YourBot` to your actual telegram bot module and import pyrogram client from it.
from RDXROBOT import pbot

API_URL = 'https://sasta.tk/bounty'

class STRINGS:
    ONLY_USERS = '<b>❍ ᴏɴʟʏ ᴜsᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜɪs command!</b>'
    DOWNLOADING_PHOTO = '<b>❍ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴘʜᴏᴛᴏ...</b>'
    REQUESTING_API = '<b>❍ ʀᴇǫᴜᴇsᴛɪɴɢ ᴀᴘɪ...</b>'
    API_ERROR = '<b>❍ ᴀɴ ᴀᴘɪ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀᴇᴅ ᴡʜɪʟᴇ ʀᴇǫᴜᴇsᴛɪɴɢ</b> ➛\n{}'
    SUPPORT_CHAT = '<b>❍ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ ➛</b> https://t.me/+RObRa7kXPIJmMjU1'
    BOUNTY_RESULT = '''
<b>✦ ʜᴇʀᴇ ɪs ʏᴏᴜʀ ʙᴏᴜɴᴛʏ ✦</b>

<b>❍ ᴄʀᴇᴅɪᴛs ➛</b> https://t.me/+RObRa7kXPIJmMjU1
    '''

COMMANDS = ['bounty', 'wanted']

@pbot.on_message(filters.command(COMMANDS))
async def on_bounty(client: Client, message: Message) -> Message:
    from_user = message.from_user
    if not from_user:
        await message.reply(STRINGS.ONLY_USERS)
        return
    name = f'{from_user.first_name} {from_user.last_name}' if from_user.last_name else from_user.first_name
    status_msg = await message.reply(STRINGS.DOWNLOADING_PHOTO)
    file_path = f'downloads/{uuid.uuid4()}'
    big_file_id = from_user.photo.big_file_id
    await client.download_media(big_file_id, file_path)
    await status_msg.edit(STRINGS.REQUESTING_API)
    async with httpx.AsyncClient(timeout=30) as async_client:
        with open(file_path, 'rb') as file:
            params = {
                'name': name
            }
            files = {'file': file}
            response = await async_client.post(API_URL, params=params, files=files)
        try:
            response_json = response.json()
        except:
            await message.reply(STRINGS.API_ERROR.format(response.text) + '\n\n' +  STRINGS.SUPPORT_CHAT)
            return
        if response.status_code != 200:
            await message.reply(STRINGS.API_ERROR.format(response_json['error']) + '\n\n' + STRINGS.SUPPORT_CHAT)
            return
    # For those regions where telegra.ph is blocked.
    # Replacing `telegra.ph` with `te.legra.ph`.
    url = response_json['url'].replace('telegra.ph','te.legra.ph')
    reply_markup = [
        [InlineKeyboardButton('ᴛᴇʟᴇɢʀᴀᴘʜʏ ʟɪɴᴋ', url=url)]
        ]
    await message.reply_photo(url, caption=STRINGS.BOUNTY_RESULT, reply_markup=InlineKeyboardMarkup(reply_markup))
    await status_msg.delete()


__mod_name__ = "ʙᴏᴜɴᴛʏ"
__help__ = """
 ❍ /wanted ➛ ʀᴇᴘʟᴀʏ ᴀ ᴘʜᴏᴛᴏ.
 ❍ /bounty ➛ ʀᴇᴘʟᴀʏ ᴀ ᴘʜᴏᴛᴏ.
 """
