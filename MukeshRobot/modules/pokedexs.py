# Pokedex Module Credits Pranav Ajay 🐰Github = Red-Aura 🐹 Telegram= @madepranav

import aiohttp
from pyrogram import filters
from MukeshRobot import pbot as app


@app.on_message(filters.command("pokedex"))
async def PokeDex(_, message):
    if len(message.command) != 2:
        await message.reply_text("❍ /pokedex ᴘᴏᴋᴇᴍᴏɴ ɴᴀᴍᴇ.")
        return
    pokemon = message.text.split(None, 1)[1]
    pokedex = f"https://sugoi-api.vercel.app/pokemon?name={name}"
    async with aiohttp.ClientSession() as session:
        async with session.get(pokedex) as request:
            if request.status == 404:
                return await message.reply_text("❍ ᴡʀᴏɴɢ ᴘᴏᴋᴇᴍᴏɴ ɴᴀᴍᴇ")

            result = await request.json()
            try:
                pokemon = result["name"]
                pokedex = result["id"]
                type = result["type"]
                poke_img = f"https://img.pokemondb.net/artwork/large/{pokemon}.jpg"
                abilities = result["abilities"]
                height = result["height"]
                weight = result["weight"]
                gender = result["gender"]
                stats = result["stats"]
                description = result["description"]
                caption = f"""
**❍ ᴘᴏᴋᴇᴍᴏɴ ➛** `{pokemon}`
**❍ ᴘᴏᴋᴇᴅᴇx ➛** `{pokedex}`
**❍ ᴛʏᴘᴇ ➛** `{type}`
**❍ ᴀʙɪʟɪᴛɪᴇs ➛** `{abilities}`
**❍ ʜᴇɪɢʜᴛ ➛** `{height}`
**❍ ᴡᴇɪɢʜᴛ ➛** `{weight}`
**❍ ɢᴇɴᴅᴇʀ ➛** `{gender}`
**❍ sᴛᴀᴛs ➛** `{stats}`
**❍ ᴅᴇsᴄʀɪᴘᴛɪᴏɴ ➛** `{description}`"""
            except Exception as e:
                print(str(e))
                pass
    await message.reply_photo(photo=poke_img, caption=caption)


__mod_name__ = "ᴘᴏᴋᴇᴅᴇx"
__help__ = """
 ❍ /pokedex ➛ sᴇᴀʀᴄʜ ᴘᴏᴋɪᴍᴀɴ ᴄʜᴀʀᴀᴄᴛᴇʀ.
 """
