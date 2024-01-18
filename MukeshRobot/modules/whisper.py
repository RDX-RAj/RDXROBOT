# Credits to Reeshuxd

from telethon import events, Button
import logging
from telethon.tl.functions.users import GetFullUserRequest as us
from MukeshRobot import BOT_USERNAME, telethn as bot

logging.basicConfig(level=logging.INFO)


db = {}

@bot.on(events.NewMessage(pattern=f"^[!?@/]({BOT_USERNAME} | wspr)$"))
async def stsrt(event):
    await event.reply(
            f"**❍ ʜᴇʏ, ɪ ᴀᴍ ᴀ ᴡʜɪsᴘᴇʀ ʙᴏᴛ ғᴜɴᴄᴛɪᴏɴ ғᴏʀ @{BOT_USERNAME} !**",
            buttons=[
                [Button.switch_inline("ɢᴏ ɪɴʟɪɴᴇ", query="")]
                ]
            )


@bot.on(events.InlineQuery())
async def die(event):
    if len(event.text) != 0:
        return
    me = (await bot.get_me()).username
    dn = event.builder.article(
            title="❍ ɪᴛ's ᴀ ᴡʜɪsᴘᴇʀ ʙᴏᴛ !",
            description=f"❍ ᴡʜɪsᴘᴇʀ ʙᴏᴛ ғᴜɴᴄᴛɪᴏɴ ғᴏʀ @{BOT_USERNAME} !",
            text=f"**❍ ɪᴛ's ᴀ ᴡʜɪsᴘᴇʀ ʙᴏᴛ**\n❍ `@{me} ᴡsᴘʀ ᴜsᴇʀɴᴀᴍᴇ|ᴍᴇssᴀɢᴇ`",
            buttons=[
                [Button.switch_inline(" ɢᴏ ɪɴʟɪɴᴇ ", query="wspr ")]
                ]
            )
    await event.answer([dn])

@bot.on(events.InlineQuery(pattern="wspr"))
async def inline(event):
    me = (await bot.get_me()).username
    try:
        inp = event.text.split(None, 1)[1]
        user, msg = inp.split("|")
    except IndexError:
        await event.answer(
                [], 
                switch_pm=f"@{me} [Username]|[Message]",
                switch_pm_param="ᴡʜɪsᴘᴇʀ"
                )
    except ValueError:
        await event.answer(
                [],
                switch_pm="❍ ɢɪᴠᴇ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏᴏ !",
                switch_pm_param="ᴡʜɪsᴘᴇʀ"
                )
    try:
        ui = await bot(us(user))
    except BaseException:
        await event.answer(
                [],
                switch_pm="ɪɴᴠᴀʟɪᴅ ᴜsᴇʀ ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ",
                switch_pm_param="ᴡʜɪsᴘᴇʀ"
                )
        return
    db.update({"user_id": ui.user.id, "msg": msg, "self": event.sender.id})
    text = f"""
💌 ᴀ ᴡʜɪsᴘᴇʀ ʜᴀs ʙᴇᴇɴ sᴇɴᴛ ᴛᴏ [{ui.user.first_name}](tg://user?id={ui.user.id}) !\n\n💌 ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ sᴇᴇ ᴛʜᴇ ᴍᴇssᴀɢᴇ !
**💌 ɴᴏᴛᴇ ➛** ᴏɴʟʏ {ui.user.first_name} ᴄᴀɴ ᴏᴘᴇɴ ᴛʜɪs.
    """
    dn = event.builder.article(
            title="❍ ɪᴛs ᴀ sᴇᴄʀᴇᴛ ᴍᴇssᴀɢᴇ ! sssʜ",
            description="❍ ɪᴛ's ᴀ sᴇᴄʀᴇᴛ ᴍᴇssᴀɢᴇ ! sssʜ!",
            text=text,
            buttons=[
                [Button.inline("💌 sʜᴏᴡ ᴍᴇssᴀɢᴇ 💌", data="wspr")]
                ]
            )
    await event.answer(
            [dn],
            switch_pm="❍ ɪᴛ's ᴀ sᴇᴄʀᴇᴛ ᴍᴇssᴀɢᴇ ! sssʜ",
            switch_pm_param="ᴡʜɪsᴘᴇʀ"
            )


@bot.on(events.CallbackQuery(data="wspr"))
async def ws(event):
    user = int(db["user_id"])
    lol = [int(db["self"]), user]
    if event.sender.id not in lol:
        await event.answer("💌 ᴛʜɪs ᴍᴇssᴀɢᴇ ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ !", alert=True)
        return
    msg = db["msg"]
    if msg == []:
        await event.anwswer(
                "ᴏᴏᴘs !\n❍ ɪᴛ's ʟᴏᴏᴋs ʟɪᴋᴇ ᴍᴇssᴀɢᴇ ɢᴏᴛ ᴅᴇʟᴇᴛᴇᴅ ғʀᴏᴍ ᴍʏ sᴇʀᴠᴇʀ !", alert=True)
        return
    await event.answer(msg, alert=True)

__help__ = """
✿ *ᴡʜɪsᴘᴇʀ ɪɴʟɪɴᴇ ғᴜɴᴄᴛɪᴏɴ ғᴏʀ sᴇᴄʀᴇᴛ ᴄʜᴀᴛs* ✿

๏ @AvishaXbot ʏᴏᴜʀ ᴍᴇssᴀɢᴇ @username
๏ @AvishaxBot @username ʏᴏᴜʀ ᴍᴇssᴀɢᴇ
"""

__mod_name__ = "ᴡʜɪsᴘᴇʀ"
