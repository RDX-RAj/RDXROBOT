from pyrogram import Client, filters , enums
import requests


@Client.on_message(filters.command("nude"))
async def nudes(_,message):
    if message.chat.type != enums.ChatType.PRIVATE:
        return await message.reply_text("**This Command Is Only Usable In PM for Group Protection.**")
    x = requests.get('https://api.night-api.com/images/nsfw',headers={"authorization": "pUieNWJRIs-2Q073qw9dddUcM3Vncmn-eusGidDCIw"})
    await message.reply_photo(x.json()["content"]["url"])
