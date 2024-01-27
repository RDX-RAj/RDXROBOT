import html
import json
import os
from typing import Optional

from telegram import ParseMode, TelegramError, Update
from telegram.ext import CallbackContext, CommandHandler
from telegram.utils.helpers import mention_html

from MukeshRobot import (
    DEMONS,
    DEV_USERS,
    DRAGONS,
    OWNER_ID,
    SUPPORT_CHAT,
    TIGERS,
    WOLVES,
    dispatcher,
)
from MukeshRobot.modules.helper_funcs.chat_status import (
    dev_plus,
    sudo_plus,
    whitelist_plus,
)
from MukeshRobot.modules.helper_funcs.extraction import extract_user
from MukeshRobot.modules.log_channel import gloggable

ELEVATED_USERS_FILE = os.path.join(os.getcwd(), "MukeshRobot/elevated_users.json")


def check_user_id(user_id: int, context: CallbackContext) -> Optional[str]:
    bot = context.bot
    if not user_id:
        reply = "๏ ᴛʜᴀᴛ...ɪs ᴀ ᴄʜᴀᴛ ! ʙᴀᴋᴀ ᴋᴀ ᴏᴍᴀᴇ ?"

    elif user_id == bot.id:
        reply = "๏ ᴛʜɪs ᴅᴏᴇs ɴᴏᴛ ᴡᴏʀᴋ ᴛʜᴀᴛ ᴡᴀʏ."

    else:
        reply = None
    return reply


@dev_plus
@gloggable
def addsudo(update: Update, context: CallbackContext) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)
    rt = ""

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in DRAGONS:
        message.reply_text("๏ ᴛʜɪs ᴍᴇᴍʙᴇʀ ɪs ᴀʟʀᴇᴀᴅʏ ᴀ ᴅʀᴀɢᴏɴ ᴅɪsᴀsᴛᴇʀ")
        return ""

    if user_id in DEMONS:
        rt += "๏ ʀᴇǫᴜᴇsᴛᴇᴅ ʜᴀ ᴛᴏ ᴘʀᴏᴍᴏᴛᴇ ᴀ ᴅᴇᴍᴏɴ ᴅɪsᴀsᴛᴇʀ ᴛᴏ ᴅʀᴀɢᴏɴ."
        data["supports"].remove(user_id)
        DEMONS.remove(user_id)

    if user_id in WOLVES:
        rt += "๏ ʀᴇǫᴜᴇsᴛᴇᴅ ʜᴀ ᴛᴏ ᴘʀᴏᴍᴏᴛᴇ ᴀ ᴡᴏʟғ ᴅɪsᴀsᴛᴇʀ ᴛᴏ ᴅʀᴀɢᴏɴ."
        data["whitelists"].remove(user_id)
        WOLVES.remove(user_id)

    data["sudos"].append(user_id)
    DRAGONS.append(user_id)

    with open(ELEVATED_USERS_FILE, "w") as outfile:
        json.dump(data, outfile, indent=4)

    update.effective_message.reply_text(
        rt
        + "\n๏ sᴜᴄᴄᴇssғᴜʟʟʏ sᴇᴛ ᴅɪsᴀsᴛᴇʀ ʟᴇᴠᴇʟ ᴏғ {} ᴛᴏ ᴅʀᴀɢᴏɴ !".format(
            user_member.first_name
        )
    )

    log_message = (
        f"๏ #sᴜᴅᴏ\n"
        f"๏ <b>ᴀᴅᴍɪɴ ➠</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        f"๏ <b>ᴜsᴇʀ ➠</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
    )

    if chat.type != "private":
        log_message = f"๏ <b>{html.escape(chat.title)}</b>\n" + log_message

    return log_message


@sudo_plus
@gloggable
def addsupport(
    update: Update,
    context: CallbackContext,
) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)
    rt = ""

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in DRAGONS:
        rt += "๏ ʀᴇǫᴜᴇsᴛᴇᴅ ʜᴀ ᴛᴏ ᴅᴇᴍᴏᴛᴇ ᴛʜɪs ᴅʀᴀɢᴏɴ ᴛᴏ ᴅᴇᴍᴏɴ"
        data["sudos"].remove(user_id)
        DRAGONS.remove(user_id)

    if user_id in DEMONS:
        message.reply_text("๏ ᴛʜɪs ᴜsᴇʀ ɪs ᴀʟʀᴇᴀᴅʏ ᴀ ᴅᴇᴍᴏɴ ᴅɪsᴀsᴛᴇʀ.")
        return ""

    if user_id in WOLVES:
        rt += "๏ ʀᴇǫᴜᴇsᴛᴇᴅ ʜᴀ ᴛᴏ ᴘʀᴏᴍᴏᴛᴇ ᴛʜɪs ᴡᴏʟғ ᴅɪsᴀsᴛᴇʀ ᴛᴏ ᴅᴇᴍᴏɴ"
        data["whitelists"].remove(user_id)
        WOLVES.remove(user_id)

    data["supports"].append(user_id)
    DEMONS.append(user_id)

    with open(ELEVATED_USERS_FILE, "w") as outfile:
        json.dump(data, outfile, indent=4)

    update.effective_message.reply_text(
        rt + f"\n๏ {user_member.first_name} ᴡᴀs ᴀᴅᴅᴇᴅ ᴀs ᴀ ᴅᴇᴍᴏɴ ᴅɪsᴀsᴛᴇʀ !"
    )

    log_message = (
        f"๏ #sᴜᴘᴘᴏʀᴛ\n"
        f"๏ <b>ᴀᴅᴍɪɴ ➠</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        f"๏ <b>ᴜsᴇʀ ➠</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
    )

    if chat.type != "private":
        log_message = f"๏ <b>{html.escape(chat.title)}</b>\n" + log_message

    return log_message


@sudo_plus
@gloggable
def addwhitelist(update: Update, context: CallbackContext) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)
    rt = ""

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in DRAGONS:
        rt += "๏ ᴛʜɪs ᴍᴇᴍʙᴇʀ ɪs ᴀ ᴅʀᴀɢᴏɴ ᴅɪsᴀsᴛᴇʀ, ᴅᴇᴍᴏᴛɪɴɢ ᴛᴏ ᴡᴏʟғ."
        data["sudos"].remove(user_id)
        DRAGONS.remove(user_id)

    if user_id in DEMONS:
        rt += "๏ ᴛʜɪs ᴜsᴇʀ ɪs ᴀʟʀᴇᴀᴅʏ ᴀ ᴅᴇᴍᴏɴ ᴅɪsᴀsᴛᴇʀ, ᴅᴇᴍᴏᴛɪɴɢ ᴛᴏ ᴡᴏʟғ."
        data["supports"].remove(user_id)
        DEMONS.remove(user_id)

    if user_id in WOLVES:
        message.reply_text("๏ ᴛʜɪs ᴜsᴇʀ ɪs ᴀʟʀᴇᴀᴅʏ ᴀ ᴡᴏʟғ ᴅɪsᴀsᴛᴇʀ.")
        return ""

    data["whitelists"].append(user_id)
    WOLVES.append(user_id)

    with open(ELEVATED_USERS_FILE, "w") as outfile:
        json.dump(data, outfile, indent=4)

    update.effective_message.reply_text(
        rt + f"\n๏ sᴜᴄᴄᴇssғᴜʟʟʏ ᴘʀᴏᴍᴏᴛᴇᴅ {user_member.first_name} ᴛᴏ ᴀ ᴡᴏʟғ ᴅɪsᴀsᴛᴇʀ !"
    )

    log_message = (
        f"๏ #ᴡʜɪᴛᴇʟɪsᴛ\n"
        f"๏ <b>ᴀᴅᴍɪɴ ➠</b> {mention_html(user.id, html.escape(user.first_name))} \n"
        f"๏ <b>ᴜsᴇʀ ➠</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
    )

    if chat.type != "private":
        log_message = f"๏ <b>{html.escape(chat.title)}</b>\n" + log_message

    return log_message


@sudo_plus
@gloggable
def addtiger(update: Update, context: CallbackContext) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)
    rt = ""

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in DRAGONS:
        rt += "๏ ᴛʜɪs ᴍᴇᴍʙᴇʀ ɪs ᴀ ᴅʀᴀɢᴏɴ ᴅɪsᴀsᴛᴇʀ, ᴅᴇᴍᴏᴛɪɴɢ ᴛᴏ ᴛɪɢᴇʀ."
        data["sudos"].remove(user_id)
        DRAGONS.remove(user_id)

    if user_id in DEMONS:
        rt += "๏ ᴛʜɪs ᴜsᴇʀ ɪs ᴀʟʀᴇᴀᴅʏ ᴀ ᴅᴇᴍᴏɴ ᴅɪsᴀsᴛᴇʀ, ᴅᴇᴍᴏᴛɪɴɢ ᴛᴏ ᴛɪɢᴇʀ."
        data["supports"].remove(user_id)
        DEMONS.remove(user_id)

    if user_id in WOLVES:
        rt += "๏ ᴛʜɪs ᴜsᴇʀ ɪs ᴀʟʀᴇᴀᴅʏ ᴀ ᴡᴏʟғ ᴅɪsᴀsᴛᴇʀ, ᴅᴇᴍᴏᴛɪɴɢ ᴛᴏ ᴛɪɢᴇʀ."
        data["whitelists"].remove(user_id)
        WOLVES.remove(user_id)

    if user_id in TIGERS:
        message.reply_text("๏ ᴛʜɪs ᴜsᴇʀ ɪs ᴀʟʀᴇᴀᴅʏ ᴀ ᴛɪɢᴇʀ.")
        return ""

    data["tigers"].append(user_id)
    TIGERS.append(user_id)

    with open(ELEVATED_USERS_FILE, "w") as outfile:
        json.dump(data, outfile, indent=4)

    update.effective_message.reply_text(
        rt + f"\n๏ sᴜᴄᴄᴇssғᴜʟʟʏ ᴘʀᴏᴍᴏᴛᴇᴅ {user_member.first_name} ᴛᴏ ᴀ ᴛɪɢᴇʀ ᴅɪsᴀsᴛᴇʀ !"
    )

    log_message = (
        f"๏ #ᴛɪɢᴇʀ\n"
        f"๏ <b>ᴀᴅᴍɪɴ ➠</b> {mention_html(user.id, html.escape(user.first_name))} \n"
        f"๏ <b>ᴜsᴇʀ ➠</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
    )

    if chat.type != "private":
        log_message = f"๏ <b>{html.escape(chat.title)}</b>\n" + log_message

    return log_message


@dev_plus
@gloggable
def removesudo(update: Update, context: CallbackContext) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in DRAGONS:
        message.reply_text("๏ ʀᴇǫᴜᴇsᴛᴇᴅ ʜᴀ to ᴅᴇᴍᴏᴛᴇ ᴛʜɪs ᴜsᴇʀ ᴛᴏ ᴄɪᴠɪʟɪᴀɴ")
        DRAGONS.remove(user_id)
        data["sudos"].remove(user_id)

        with open(ELEVATED_USERS_FILE, "w") as outfile:
            json.dump(data, outfile, indent=4)

        log_message = (
            f"๏ #ᴜɴsᴜᴅᴏ\n"
            f"๏ <b>ᴀᴅᴍɪɴ ➠</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"๏ <b>ᴜsᴇʀ ➠</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
        )

        if chat.type != "private":
            log_message = "๏ <b>{}</b>\n".format(html.escape(chat.title)) + log_message

        return log_message

    else:
        message.reply_text("๏ ᴛʜɪs ᴜsᴇʀ ɪs ɴᴏᴛ ᴀ ᴅʀᴀɢᴏɴ ᴅɪsᴀsᴛᴇʀ !")
        return ""


@sudo_plus
@gloggable
def removesupport(update: Update, context: CallbackContext) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in DEMONS:
        message.reply_text("๏ ʀᴇǫᴜᴇsᴛᴇᴅ ʜᴀ ᴛᴏ ᴅᴇᴍᴏᴛᴇ ᴛʜɪs ᴜsᴇʀ ᴛᴏ ᴄɪᴠɪʟɪᴀɴ")
        DEMONS.remove(user_id)
        data["supports"].remove(user_id)

        with open(ELEVATED_USERS_FILE, "w") as outfile:
            json.dump(data, outfile, indent=4)

        log_message = (
            f"๏ #ᴜɴsᴜᴘᴘᴏʀᴛ\n"
            f"๏ <b>ᴀᴅᴍɪɴ ➠</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"๏ <b>ᴜsᴇʀ ➠</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
        )

        if chat.type != "private":
            log_message = f"๏ <b>{html.escape(chat.title)}</b>\n" + log_message

        return log_message

    else:
        message.reply_text("๏ ᴛʜɪs ᴜsᴇʀ ɪs ɴᴏᴛ ᴀ ᴅᴇᴍᴏɴ ʟᴇᴠᴇʟ ᴅɪsᴀsᴛᴇʀ !")
        return ""


@sudo_plus
@gloggable
def removewhitelist(update: Update, context: CallbackContext) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in WOLVES:
        message.reply_text("๏ ᴅᴇᴍᴏᴛɪɴɢ ᴛᴏ ɴᴏʀᴍᴀʟ ᴜsᴇʀ")
        WOLVES.remove(user_id)
        data["whitelists"].remove(user_id)

        with open(ELEVATED_USERS_FILE, "w") as outfile:
            json.dump(data, outfile, indent=4)

        log_message = (
            f"๏ #ᴜɴᴡʜɪᴛᴇʟɪsᴛ\n"
            f"๏ <b>ᴀᴅᴍɪɴ ➠</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"๏ <b>ᴜsᴇʀ ➠</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
        )

        if chat.type != "private":
            log_message = f"๏ <b>{html.escape(chat.title)}</b>\n" + log_message

        return log_message
    else:
        message.reply_text("๏ ᴛʜɪs ᴜsᴇʀ ɪs ɴᴏᴛ ᴀ ᴡᴏʟғ ᴅɪsᴀsᴛᴇʀ !")
        return ""


@sudo_plus
@gloggable
def removetiger(update: Update, context: CallbackContext) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in TIGERS:
        message.reply_text("๏ ᴅᴇᴍᴏᴛɪɴɢ ᴛᴏ ɴᴏʀᴍᴀʟ ᴜsᴇʀ")
        TIGERS.remove(user_id)
        data["tigers"].remove(user_id)

        with open(ELEVATED_USERS_FILE, "w") as outfile:
            json.dump(data, outfile, indent=4)

        log_message = (
            f"๏ #ᴜɴᴛɪɢᴇʀ\n"
            f"๏ <b>ᴀᴅᴍɪɴ ➠</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"๏ <b>ᴜsᴇʀ ➠</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
        )

        if chat.type != "private":
            log_message = f"๏ <b>{html.escape(chat.title)}</b>\n" + log_message

        return log_message
    else:
        message.reply_text("๏ ᴛʜɪs ᴜsᴇʀ ɪs ɴᴏᴛ ᴀ ᴛɪɢᴇʀ ᴅɪsᴀsᴛᴇʀ !")
        return ""


@whitelist_plus
def whitelistlist(update: Update, context: CallbackContext):
    reply = "๏ <b>ᴋɴᴏᴡɴ ᴡᴏʟғ ᴅɪsᴀsᴛᴇʀs 🐺</b>\n"
    m = update.effective_message.reply_text(
        "<code>..</code>", parse_mode=ParseMode.HTML
    )
    bot = context.bot
    for each_user in WOLVES:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)

            reply += f"๏ {mention_html(user_id, html.escape(user.first_name))}\n"
        except TelegramError:
            pass
    m.edit_text(reply, parse_mode=ParseMode.HTML)


@whitelist_plus
def tigerlist(update: Update, context: CallbackContext):
    reply = "๏ <b>ᴋɴᴏᴡɴ ᴛɪɢᴇʀ ᴅɪsᴀsᴛᴇʀs 🐯</b>\n"
    m = update.effective_message.reply_text(
        "<code>ɢᴀᴛʜᴇʀɪɴɢ ɪɴᴛᴇʟ..</code>", parse_mode=ParseMode.HTML
    )
    bot = context.bot
    for each_user in TIGERS:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)
            reply += f"๏ {mention_html(user_id, html.escape(user.first_name))}\n"
        except TelegramError:
            pass
    m.edit_text(reply, parse_mode=ParseMode.HTML)


@whitelist_plus
def supportlist(update: Update, context: CallbackContext):
    bot = context.bot
    m = update.effective_message.reply_text(
        "<code>ɢᴀᴛʜᴇʀɪɴɢ ɪɴᴛᴇʟ..</code>", parse_mode=ParseMode.HTML
    )
    reply = "๏<b> ᴋɴᴏᴡɴ ᴅᴇᴍᴏɴ ᴅɪsᴀsᴛᴇʀs 👹</b>\n"
    for each_user in DEMONS:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)
            reply += f"๏ {mention_html(user_id, html.escape(user.first_name))}\n"
        except TelegramError:
            pass
    m.edit_text(reply, parse_mode=ParseMode.HTML)


@whitelist_plus
def sudolist(update: Update, context: CallbackContext):
    bot = context.bot
    m = update.effective_message.reply_text(
        "<code>ɢᴀᴛʜᴇʀɪɴɢ ɪɴᴛᴇʟ..</code>", parse_mode=ParseMode.HTML
    )
    true_sudo = list(set(DRAGONS)- set(DEV_USERS))
    reply = "๏ <b> ᴋɴᴏᴡɴ ᴅʀᴀɢᴏɴ ᴅɪsᴀsᴛᴇʀs 🐉</b>\n"
    for each_user in true_sudo:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)
            reply += f"๏ {mention_html(user_id, html.escape(user.first_name))}\n"
        except TelegramError:
            pass
    m.edit_text(reply, parse_mode=ParseMode.HTML)


@whitelist_plus
def devlist(update: Update, context: CallbackContext):
    bot = context.bot
    m = update.effective_message.reply_text(
        "<code>ɢᴀᴛʜᴇʀɪɴɢ..</code>", parse_mode=ParseMode.HTML
    )
    true_dev = list(set(DEV_USERS) -{OWNER_ID})
    reply = "๏ <b>ᴅᴇᴠs ᴜsᴇʀ ʟɪsᴛ </b>\n"
    for each_user in true_dev:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)
            reply += f"๏ {mention_html(user_id, html.escape(user.first_name))}\n"
        except TelegramError:
            pass
    m.edit_text(reply, parse_mode=ParseMode.HTML)


__help__ = f"""
 ✿ *ʟɪsᴛ ᴀʟʟ sᴘᴇᴄɪᴀʟ ᴜsᴇʀs* ✿

 ❍ /sudolist* ➛* ʟɪsᴛs ᴀʟʟ ᴅʀᴀɢᴏɴ ᴅɪsᴀsᴛᴇʀs
 ❍ /supportlist *➛* ʟɪsᴛs ᴀʟʟ ᴅᴇᴍᴏɴ ᴅɪsᴀsᴛᴇʀs
 ❍ /tigers *➛* ʟɪsᴛs ᴀʟʟ ᴛɪɢᴇʀs ᴅɪsᴀsᴛᴇʀs
 ❍ /wolves *➛* ʟɪsᴛs ᴀʟʟ ᴡᴏʟғ ᴅɪsᴀsᴛᴇʀs
 ❍ /devlist *➛* ʟɪsᴛs ᴀʟʟ ʜᴇʀᴏ ᴀssᴏᴄɪᴀᴛɪᴏɴ ᴍᴇᴍʙᴇʀs
 ❍ /addsudo  *➛* ᴀᴅᴅs ᴀ ᴜsᴇʀ ᴛᴏ ᴅʀᴀɢᴏɴ
 ❍ /adddemon *➛* ᴀᴅᴅs ᴀ ᴜsᴇʀ ᴛᴏ ᴅᴇᴍᴏɴ
 ❍ /addtiger *➛* ᴀᴅᴅs ᴀ ᴜsᴇʀ ᴛᴏ ᴛɪɢᴇʀ
 ❍ /addwolf *➛* ᴀᴅᴅs ᴀ ᴜsᴇʀ ᴛᴏ ᴡᴏʟғ
 
 ❍ ᴀᴅᴅ ᴅᴇᴠ ᴅᴏᴇsɴᴛ ᴇxɪsᴛ, ᴅᴇᴠs sʜᴏᴜʟᴅ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴀᴅᴅ ᴛʜᴇᴍsᴇʟᴠᴇs
"""

SUDO_HANDLER = CommandHandler("addsudo", addsudo, run_async=True)
SUPPORT_HANDLER = CommandHandler(("addsupport", "adddemon"), addsupport, run_async=True)
TIGER_HANDLER = CommandHandler(("addtiger"), addtiger, run_async=True)
WHITELIST_HANDLER = CommandHandler(
    ("addwhitelist", "addwolf"), addwhitelist, run_async=True
)
UNSUDO_HANDLER = CommandHandler(("removesudo", "rmsudo"), removesudo, run_async=True)
UNSUPPORT_HANDLER = CommandHandler(
    ("removesupport", "removedemon"), removesupport, run_async=True
)
UNTIGER_HANDLER = CommandHandler(("removetiger"), removetiger, run_async=True)
UNWHITELIST_HANDLER = CommandHandler(
    ("removewhitelist", "removewolf"), removewhitelist, run_async=True
)
WHITELISTLIST_HANDLER = CommandHandler(
    ["whitelistlist", "wolves"], whitelistlist, run_async=True
)
TIGERLIST_HANDLER = CommandHandler(["tigers"], tigerlist, run_async=True)
SUPPORTLIST_HANDLER = CommandHandler("supportlist", supportlist, run_async=True)
SUDOLIST_HANDLER = CommandHandler("sudolist", sudolist, run_async=True)
DEVLIST_HANDLER = CommandHandler("devlist", devlist, run_async=True)

dispatcher.add_handler(SUDO_HANDLER)
dispatcher.add_handler(SUPPORT_HANDLER)
dispatcher.add_handler(TIGER_HANDLER)
dispatcher.add_handler(WHITELIST_HANDLER)
dispatcher.add_handler(UNSUDO_HANDLER)
dispatcher.add_handler(UNSUPPORT_HANDLER)
dispatcher.add_handler(UNTIGER_HANDLER)
dispatcher.add_handler(UNWHITELIST_HANDLER)
dispatcher.add_handler(WHITELISTLIST_HANDLER)
dispatcher.add_handler(TIGERLIST_HANDLER)
dispatcher.add_handler(SUPPORTLIST_HANDLER)
dispatcher.add_handler(SUDOLIST_HANDLER)
dispatcher.add_handler(DEVLIST_HANDLER)

__mod_name__ = "ᴅɪsᴀsᴛᴇʀ"
__handlers__ = [
    SUDO_HANDLER,
    SUPPORT_HANDLER,
    TIGER_HANDLER,
    WHITELIST_HANDLER,
    UNSUDO_HANDLER,
    UNSUPPORT_HANDLER,
    UNTIGER_HANDLER,
    UNWHITELIST_HANDLER,
    WHITELISTLIST_HANDLER,
    TIGERLIST_HANDLER,
    SUPPORTLIST_HANDLER,
    SUDOLIST_HANDLER,
    DEVLIST_HANDLER,
]
