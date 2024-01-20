from datetime import datetime
import os
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
    Message,
)

from MukeshRobot import pbot as app
ENV = bool(os.environ.get("ENV", True))
OWNER_ID = "6922271843"
OWNER_USERNAME = "AFK_MR_ROY"
LOG_CHANNEL = "-1001929735324"

from MukeshRobot.utils.errors import capture_err


def content(msg: Message) -> [None, str]:
    text_to_return = msg.text

    if msg.text is None:
        return None
    if " " in text_to_return:
        try:
            return msg.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


@app.on_message(filters.command("reqgban"))
@capture_err
async def reqgban(_, msg: Message):
    if msg.chat.username:
        chat_username = (f"@{msg.chat.username} / `{msg.chat.id}`")
    else:
        chat_username = (f"Private Group / `{msg.chat.id}`")

    bugs = content(msg)
    user_id = msg.from_user.id
    mention = "["+msg.from_user.first_name+"](tg://user?id="+str(msg.from_user.id)+")"
    datetimes_fmt = "%d-%m-%Y"
    datetimes = datetime.utcnow().strftime(datetimes_fmt)

    thumb = "https://telegra.ph/file/d06abcefe7e1eaff972c1.jpg"
    
    bug_report = f"""
**✦ #ɢʙᴀɴ-ʀᴇǫ ➛** **@{OWNER_USERNAME}**
**✦ ғʀᴏᴍ ᴜsᴇʀ ➛** **{mention}**
**✦ ᴜsᴇʀ ɪᴅ ➛** **{user_id}**
**✦ ɢʀᴏᴜᴘ ➛** **{chat_username}**
**✦ ɢʙᴀɴ ᴛᴀʀɢᴇᴛ ➛** **{bugs}**
**✦ ᴇᴠᴇɴᴛ sᴛᴀᴍᴘ ➛** **{datetimes}**"""

    
    if msg.chat.type == "private":
        await msg.reply_text("<b>✦ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ ɢʀᴏᴜᴘs.</b>")
        return

    if user_id == OWNER_ID:
        if bugs:
            await msg.reply_text(
                "<b>✦ ʜᴏᴡ ᴄᴀɴ ʙᴇ ʙᴏᴛ ᴏᴡɴᴇʀ ʀᴇǫᴜᴇsᴛɪɴɢ ɢʙᴀɴ ??</b>",
            )
            return
        else:
            await msg.reply_text(
                "✦ ɴᴏ ᴜsᴇʟᴇss ɢʙᴀɴs !"
            )
    elif user_id != OWNER_ID:
        if bugs:
            await msg.reply_text(
                f"<b>✦ ɢʙᴀɴ ʀᴇǫᴜᴇsᴛ ➛ {bugs}</b>\n\n"
                "<b>✦ ᴛʜᴇ ɢʙᴀɴ ᴡᴀs sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇǫᴜᴇsᴛᴇᴅ ᴛᴏ ᴛʜᴇ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ !</b>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "ᴄʟᴏsᴇ", callback_data=f"close_reply")
                        ]
                    ]
                )
            )
            await app.send_photo(
                LOG_CHANNEL,
                photo=thumb,
                caption=f"{bug_report}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "ᴠɪᴇᴡ ʀᴇᴀsᴏɴ", url=f"{msg.link}")
                        ],
                        [
                            InlineKeyboardButton(
                                "ᴄʟᴏsᴇ", callback_data="close_send_photo")
                        ]
                    ]
                )
            )
        else:
            await msg.reply_text(
                f"<b>✦ ɴᴏ ɢʙᴀɴ ᴛᴏ ʀᴇǫᴜᴇsᴛ !</b>",
            )
        

@app.on_callback_query(filters.regex("close_reply"))
async def close_reply(msg, CallbackQuery):
    await CallbackQuery.message.delete()

@app.on_callback_query(filters.regex("close_send_photo"))
async def close_send_photo(_, CallbackQuery):
    is_Admin = await Client.get_chat_member(
        CallbackQuery.message.chat.id, CallbackQuery.from_user.id
    )
    if not is_Admin.can_delete_messages:
        return await CallbackQuery.answer(
            "✦ ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴄʟᴏsᴇ ᴛʜɪs.", show_alert=True
        )
    else:
        await CallbackQuery.message.delete()
