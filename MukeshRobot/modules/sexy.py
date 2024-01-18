import random

from telethon import Button, events

from .. import telethn as asst, SUPPORT_CHAT as c

BUTTON = [[Button.url("ꜱᴜᴘᴘᴏʀᴛ", f"https://t.me/{c}")]]
HOT = "https://telegra.ph/file/daad931db960ea40c0fca.gif"
SMEXY = "https://telegra.ph/file/a23e9fd851fb6bc771686.gif"
LEZBIAN = "https://telegra.ph/file/5609b87f0bd461fc36acb.gif"
BIGBALL = "https://i.gifer.com/8ZUg.gif"
LANG = "https://telegra.ph/file/423414459345bf18310f5.gif"
CUTIE = "https://64.media.tumblr.com/d701f53eb5681e87a957a547980371d2/tumblr_nbjmdrQyje1qa94xto1_500.gif"


@asst.on(events.NewMessage(pattern="/horny ?(.*)"))
async def horny(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    HORNY = f"**❍ 🤤** {mention} **ɪꜱ** {mm}**% ʜᴏʀɴʏ !**"
    await e.reply(HORNY, buttons=BUTTON, file=HOT)


@asst.on(events.NewMessage(pattern="/gay ?(.*)"))
async def gay(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    GAY = f"**❍ 🧝** {mention} **ɪꜱ** {mm}**% ɢᴀʏ !**"
    await e.reply(GAY, buttons=BUTTON, file=SMEXY)


@asst.on(events.NewMessage(pattern="/lezbian ?(.*)"))
async def lezbian(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    FEK = f"**❍ 🥶** {mention} **ɪꜱ** {mm}**% ʟᴇᴢʙɪᴀɴ !**"
    await e.reply(FEK, buttons=BUTTON, file=LEZBIAN)


@asst.on(events.NewMessage(pattern="/boob ?(.*)"))
async def boob(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    BOOBS = f"**❍ 🥵** {mention}**'ꜱ ʙᴏᴏʙꜱ ꜱɪᴢᴇ ɪᴢ** {mm}** !**"
    await e.reply(BOOBS, buttons=BUTTON, file=BIGBALL)


@asst.on(events.NewMessage(pattern="/cock ?(.*)"))
async def cock(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    COCK = f"**❍ 🍆** {mention}**'ꜱ ᴄᴏᴄᴋ ꜱɪᴢᴇ ɪᴢ** {mm}**ᴄᴍ !**"
    await e.reply(COCK, buttons=BUTTON, file=LANG)


@asst.on(events.NewMessage(pattern="/dull ?(.*)"))
async def cute(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    CUTE = f"**❍ 🧟** {mention} {mm}**% ᴅᴜʟʟ !**"
    await e.reply(CUTE, buttons=BUTTON, file=CUTIE)


@asst.on(events.NewMessage(pattern="/wish ?(.*)"))
async def wish(e):
    api = requests.get("https://nekos.best/api/v2/happy").json()
    url = api["results"][0]['url']
    text = m.text.split(None, 1)[1]
    wish_count = random.randint(1,100)
    wish = f"❍ **ɢᴇᴛ {m.from_user.first_name} !**\n"
    wish += f"❍ **ʏᴏᴜʀ ᴡɪꜱʜ** ➛ **{text}**\n"
    wish += f"❍ **ᴘᴏꜱꜱɪʙʟᴇ ᴛᴏ ➛ {wish_count}%**"
    await e.reply(WISH, buttons=BUTTON, file=WISHES)


@asst.on(events.NewMessage(pattern="/guess ?(.*)"))
async def guess(e):
        user_id = e.sender.id
        user_name = e.sender.frist_name
        mention = f"[{user_name}](tg://user?id={str(user_id)})"
        mm = random.randint(1, 100)
        GUESS = f"∆ **Hey [{e.sender.first_name}](tg://user?id={e.sender.id}), Your Guess is {mm}% !**"
        await e.reply(GUESS, button=BUTTON, file=GUESS)
        
              

__help__ = """
❍ /horny ➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ʜᴏʀɴʏᴇꜱꜱ.

❍ /gay ➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ɢᴜʏɴᴇꜱꜱ.

❍ /lezbian ➛ ᴄʜᴇᴄᴋ ᴜʀ ᴄᴜʀʀᴇɴᴛ ʟᴀᴢʙɪᴀɴ.

❍ /boob ➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ʙᴏᴏʙꜱ ꜱɪᴢᴇ.

❍ /cock ➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴄᴏᴄᴋ sɪᴢᴇ.

❍ /dull ➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴅᴜʟʟɴᴇss.
"""

__mod_name__ = "sᴇxʏ"
    
