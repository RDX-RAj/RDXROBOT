import random
import importlib
import re
import time
import asyncio
from platform import python_version as y
from sys import argv
from pyrogram import __version__ as pyrover
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram import __version__ as telever
from telegram.error import (
    BadRequest,
    ChatMigrated,
    NetworkError,
    TelegramError,
    TimedOut,
    Unauthorized,
)
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.ext.dispatcher import DispatcherHandlerStop
from telegram.utils.helpers import escape_markdown
from telethon import __version__ as tlhver

import MukeshRobot.modules.no_sql.users_db as sql
from MukeshRobot import (
    BOT_NAME,
    BOT_USERNAME,
    LOGGER,
    OWNER_ID,
    START_IMG,
    SUPPORT_CHAT,
    TOKEN,
    StartTime,
    dispatcher,
    pbot,
    telethn,
    updater,
)
from MukeshRobot.modules import ALL_MODULES
from MukeshRobot.modules.helper_funcs.chat_status import is_user_admin
from MukeshRobot.modules.helper_funcs.misc import paginate_modules


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time
PM_START_TEX = """
❍ ʜᴇʟʟᴏ `{}`, ʜᴏᴡ ᴀʀᴇ ʏᴏᴜ \n❍ ʟᴏᴠᴇ ʏᴏᴜ ʙᴀʙʏ... 
"""


PM_START_TEXT = """ 
*❍ ʜᴇʏ {}, ᴡᴇʟᴄᴏᴍᴇ ʙᴀʙʏ* !\n━━━━━━━━━━━━━━━━━━━━━━\n\n❍ *ɪ ᴀᴍ {}, ᴀɴᴅ ɪ ʜᴀᴠᴇ sᴘᴇᴄɪᴀʟ ғᴇᴀᴛᴜʀᴇs.*\n\n❍ *ᴜsᴇʀs ➛ {}*\n❍ *ᴄʜᴀᴛs ➛ {}*\n\n❍ *ɪ ʜᴀᴠᴇ ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟʟ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ + ᴍᴜsɪᴄ ʙᴏᴛ ғᴇᴀᴛᴜʀᴇs.*"""

buttons = [
    [
        InlineKeyboardButton(
            text=" ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ", 
            url=f"https://t.me/{dispatcher.bot.username}?startgroup=true", 
        ),
    ],
    [
        InlineKeyboardButton(text="ʀᴇᴘᴏ", callback_data="gib_source"),
        InlineKeyboardButton(text="ᴀʙᴏᴜᴛ", callback_data="mukesh_"),
    ],
    [
        InlineKeyboardButton(text="ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs", callback_data="Main_help"),
    ],
     
]


roy = [
    [
        InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇ", url=f"https://t.me/roy_editx"),
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = f"""
❍ *{BOT_NAME}  ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟʟᴏᴡ ᴛᴏ ɢᴇᴛ ᴅᴇsᴄʀɪᴘᴛɪᴏɴ ᴀʙᴏᴜᴛ sᴘᴇᴄɪғɪᴄs ᴄᴏᴍᴍᴀɴᴅ*"""

ABHI = [
"https://graph.org/file/f76fd86d1936d45a63c64.jpg",
"https://graph.org/file/69ba894371860cd22d92e.jpg",
"https://graph.org/file/67fde88d8c3aa8327d363.jpg",
"https://graph.org/file/3a400f1f32fc381913061.jpg",
"https://graph.org/file/a0893f3a1e6777f6de821.jpg",
"https://graph.org/file/5a285fc0124657c7b7a0b.jpg",
"https://graph.org/file/25e215c4602b241b66829.jpg",
"https://graph.org/file/a13e9733afdad69720d67.jpg",
"https://graph.org/file/692e89f8fe20554e7a139.jpg",
"https://graph.org/file/db277a7810a3f65d92f22.jpg",
"https://graph.org/file/a00f89c5aa75735896e0f.jpg",
    

]

NYKAA = [
"https://graph.org/file/9bba2b7ee9ba3806de65d.jpg",
"https://graph.org/file/ef82f289043a4fa74f8ff.jpg",
"https://graph.org/file/9c27c68958e06ae074c38.jpg",
"https://graph.org/file/0ff325b1d2efe80299aa3.jpg",
"https://graph.org/file/41167b953cf3579853d47.jpg",
"https://graph.org/file/bd93ab42e69305f274028.jpg",
"https://graph.org/file/97575db5586c05d6b2898.jpg",
"https://graph.org/file/07c393fdf931a407c9bc0.jpg",
"https://graph.org/file/f332767490ad3a5ca20e8.jpg",
"https://graph.org/file/f3449e9069667f647d14e.jpg",
"https://graph.org/file/9f51cdc739f907cbd2c7e.jpg",
"https://telegra.ph/file/d7a6a923c38e051ce35f3.jpg",
    
]


DONATE_STRING = f"""❍ ʜᴇʏ ʙᴀʙʏ, ʜᴀᴩᴩʏ ᴛᴏ ʜᴇᴀʀ ᴛʜᴀᴛ ʏᴏᴜ ᴡᴀɴɴᴀ ᴅᴏɴᴀᴛᴇ. ʏᴏᴜ ᴄᴀɴ ᴅɪʀᴇᴄᴛʟʏ ᴄᴏɴᴛᴀᴄᴛ ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ @roy_editx ғᴏʀ ᴅᴏɴᴀᴛɪɴɢ ᴏʀ ʏᴏᴜ ᴄᴀɴ ᴠɪsɪᴛ ᴍʏ sᴜᴩᴩᴏʀᴛ ᴄʜᴀᴛ @the_friendz ᴀɴᴅ ᴀsᴋ ᴛʜᴇʀᴇ ᴀʙᴏᴜᴛ ᴅᴏɴᴀᴛɪᴏɴ."""

IMPORTED = {}
MIGRATEABLE = []
HELPABLE = {}
STATS = []
USER_INFO = []
DATA_IMPORT = []
DATA_EXPORT = []
CHAT_SETTINGS = {}
USER_SETTINGS = {}

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("MukeshRobot.modules." + module_name)
    if not hasattr(imported_module, "__mod_name__"):
        imported_module.__mod_name__ = imported_module.__name__

    if imported_module.__mod_name__.lower() not in IMPORTED:
        IMPORTED[imported_module.__mod_name__.lower()] = imported_module
    else:
        raise Exception("Can't have two modules with the same name! Please change one")

    if hasattr(imported_module, "__help__") and imported_module.__help__:
        HELPABLE[imported_module.__mod_name__.lower()] = imported_module

    # Chats to migrate on chat_migrated events
    if hasattr(imported_module, "__migrate__"):
        MIGRATEABLE.append(imported_module)

    if hasattr(imported_module, "__stats__"):
        STATS.append(imported_module)

    if hasattr(imported_module, "__user_info__"):
        USER_INFO.append(imported_module)

    if hasattr(imported_module, "__import_data__"):
        DATA_IMPORT.append(imported_module)

    if hasattr(imported_module, "__export_data__"):
        DATA_EXPORT.append(imported_module)

    if hasattr(imported_module, "__chat_settings__"):
        CHAT_SETTINGS[imported_module.__mod_name__.lower()] = imported_module

    if hasattr(imported_module, "__user_settings__"):
        USER_SETTINGS[imported_module.__mod_name__.lower()] = imported_module


# do not async
def send_help(chat_id, text, keyboard=None):
    if not keyboard:
        keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    dispatcher.bot.send_photo(
        chat_id=chat_id,
        photo=START_IMG,
        caption=text,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=keyboard,
    )

def start(update: Update, context: CallbackContext):
    args = context.args
    global uptime
    uptime = get_readable_time((time.time() - StartTime))
    if update.effective_chat.type == "private":
        if len(args) >= 1:
            if args[0].lower() == "help":
                send_help(update.effective_chat.id, HELP_STRINGS)
            elif args[0].lower().startswith("ghelp_"):
                mod = args[0].lower().split("_", 1)[1]
                if not HELPABLE.get(mod, False):
                    return
                send_help(
                    update.effective_chat.id,
                    HELPABLE[mod].__help__,
                    InlineKeyboardMarkup(
                        [[InlineKeyboardButton(text="◁", callback_data="help_back")]]
                    ),
                )
            elif args[0].lower() == "markdownhelp":
                IMPORTED["exᴛʀᴀs"].markdown_help_sender(update)
            elif args[0].lower().startswith("stngs_"):
                match = re.match("stngs_(.*)", args[0].lower())
                chat = dispatcher.bot.getChat(match.group(1))

                if is_user_admin(chat, update.effective_user.id):
                    send_settings(match.group(1), update.effective_user.id, False)
                else:
                    send_settings(match.group(1), update.effective_user.id, True)

            elif args[0][1:].isdigit() and "rᴜʟᴇs" in IMPORTED:
                IMPORTED["rᴜʟᴇs"].send_rules(update, args[0], from_pm=True)

        else:
            first_name = update.effective_user.first_name
            
            x=update.effective_message.reply_sticker(
                "CAACAgUAAxkBAAI33mLYLNLilbRI-sKAAob0P7koTEJNAAIOBAACl42QVKnra4sdzC_uKQQ")
            x.delete()
            usr = update.effective_user
            lol = update.effective_message.reply_text(
                PM_START_TEX.format(usr.first_name), parse_mode=ParseMode.MARKDOWN
            )
            time.sleep(0.4)
            lol.edit_text("💛")
            time.sleep(0.5)
            lol.edit_text("🤍")
            time.sleep(0.3)
            lol.edit_text("❤️")
            time.sleep(0.4)
            lol.delete()
            
            update.effective_message.reply_photo(random.choice(NYKAA),PM_START_TEXT.format(escape_markdown(first_name), BOT_NAME,sql.num_users(),sql.num_chats()),
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
                timeout=60,
            )
    else:
        update.effective_message.reply_photo(
            random.choice(NYKAA),
            caption="❍ ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙʏ...!\n\n❍ <b>ɪ ᴅɪᴅɴ'ᴛ sʟᴇᴘᴛ ʙᴀʙʏ.</b> \n\n❍ ᴜᴘᴛɪᴍᴇ ➛ <code>{}</code>".format(
                uptime
            ),
            reply_markup=InlineKeyboardMarkup(roy),
            parse_mode=ParseMode.HTML,
        )


def error_handler(update, context):
    """๏ ʟᴏɢ ᴛʜᴇ ᴇʀʀᴏʀ ᴀɴᴅ sᴇɴᴅ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇssᴀɢᴇ ᴛᴏ ɴᴏᴛɪғʏ ᴛʜᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ."""
    # Log the error before we do anything else, so we can see it even if something breaks.
    LOGGER.error(msg="Exception while handling an update:", exc_info=context.error)

    # traceback.format_exception returns the usual python message about an exception, but as a
    # list of strings rather than a single string, so we have to join them together.
    tb_list = traceback.format_exception(
        None, context.error, context.error.__traceback__
    )
    tb = "".join(tb_list)

    # Build the message with some markup and additional information about what happened.
    message = (
        "❍ ᴀɴ ᴇxᴄᴇᴘᴛɪᴏɴ ᴡᴀs ʀᴀɪsᴇᴅ ᴡʜɪʟᴇ ʜᴀɴᴅʟɪɴɢ ᴀɴ ᴜᴘᴅᴀᴛᴇ\n"
        "❍ <pre>ᴜᴘᴅᴀᴛᴇ = {}</pre>\n\n"
        "❍ <pre>{}</pre>"
    ).format(
        html.escape(json.dumps(update.to_dict(), indent=2, ensure_ascii=False)),
        html.escape(tb),
    )

    if len(message) >= 4096:
        message = message[:4096]
    # Finally, send the message
    context.bot.send_message(chat_id=OWNER_ID, text=message, parse_mode=ParseMode.HTML)


# for test purposes
def error_callback(update: Update, context: CallbackContext):
    error = context.error
    try:
        raise error
    except Unauthorized:
        print("no nono1")
        print(error)
        # remove update.message.chat_id from conversation list
    except BadRequest:
        print("no nono2")
        print("BadRequest caught")
        print(error)

        # handle malformed requests - read more below!
    except TimedOut:
        print("no nono3")
        # handle slow connection problems
    except NetworkError:
        print("no nono4")
        # handle other connection problems
    except ChatMigrated as err:
        print("no nono5")
        print(err)
        # the chat_id of a group has changed, use e.new_chat_id instead
    except TelegramError:
        print(error)
        # handle all other telegram related errors


def help_button(update, context):
    query = update.callback_query
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)

    print(query.message.chat.id)

    try:
        if mod_match:
            module = mod_match.group(1)
            text = (
                "❅ *ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs ꜰᴏʀ* *{}* ❅\n".format(
                    HELPABLE[module].__mod_name__
                )
                + HELPABLE[module].__help__
            )
            query.message.edit_caption(text,
                parse_mode=ParseMode.MARKDOWN,
                
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="help_back"),InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", callback_data="mukesh_support")]]
                ),
            )

        elif prev_match:
            curr_page = int(prev_match.group(1))
            query.message.edit_caption(HELP_STRINGS,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(curr_page - 1, HELPABLE, "help")
                ),
            )

        elif next_match:
            next_page = int(next_match.group(1))
            query.message.edit_caption(HELP_STRINGS,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(next_page + 1, HELPABLE, "help")
                ),
            )

        elif back_match:
            query.message.edit_caption(HELP_STRINGS,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(0, HELPABLE, "help")
                ),
            )

        # ensure no spinny white circle
        context.bot.answer_callback_query(query.id)
        # query.message.delete()

    except BadRequest:
        pass


def Mukesh_about_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "mukesh_":
        uptime = get_readable_time((time.time() - StartTime))
        query.message.edit_caption(f"*✦ ɪ ᴀᴍ {dispatcher.bot.first_name} ✦*"
            "\n\n*❍ ɪ ʜᴀᴠᴇ ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟʟ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ + ᴍᴜsɪᴄ ʙᴏᴛ ғᴇᴀᴛᴜʀᴇs.*"
            "\n\n*❍ ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ sǫʟᴀʟᴄʜᴇᴍʏ ᴀɴᴅ ᴍᴏɴɢᴏᴅʙ ᴀs ᴅᴀᴛᴀʙᴀsᴇ.*"
            f"\n\n*❍ ᴜsᴇʀs ➛* {sql.num_users()}"
            f"\n*❍ ᴄʜᴀᴛs ➛* {sql.num_chats()}"
            "\n\n❍ ɪ ᴄᴀɴ ʀᴇꜱᴛʀɪᴄᴛ ᴜꜱᴇʀꜱ."
            "\n❍ ɪ ʜᴀᴠᴇ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴛɪ-ꜰʟᴏᴏᴅ ꜱʏꜱᴛᴇᴍ."
            "\n❍ ᴀᴅᴠᴀɴᴄᴇ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ᴄᴀᴘᴀʙɪʟɪᴛʏ."
            "\n❍ ᴀɴɪᴍᴇ ʙᴏᴛ ғᴜɴᴄᴛɪᴏɴᴀʟɪᴛʏ."
            "\n❍ ᴀɪ ɪɴᴛᴇɢʀᴀᴛɪᴏɴ."
            f"\n\n❍ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ғᴏʀ ɢᴇᴛᴛɪɴɢ ʙᴀsɪᴄ ʜᴇʟᴩ ᴀɴᴅ ɪɴғᴏ ᴀʙᴏᴜᴛ {dispatcher.bot.first_name}.",
            parse_mode=ParseMode.MARKDOWN,
                                   
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="ʜᴇʟᴘ ᴍᴇɴᴜ", callback_data="Main_help"
                        ),
                        InlineKeyboardButton(text="ɴʏᴋᴀᴀ ", url="https://t.me/nykaa_update"),
                    ],
                    [
                        InlineKeyboardButton(text="ʜᴏᴍᴇ", callback_data="mukesh_back"),
                    ],
                ]
            ),
            )
    elif query.data == "mukesh_support":
        query.message.edit_caption("**❍ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴊᴏɪɴ ᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴄʜᴀɴɴᴇʟ ᴛᴏ ʙᴏᴛ ᴜᴘᴅᴀᴛᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.**"
            f"\n\n❍ ɪғ ᴀɴʏ ʙᴜɢ ɪɴ {dispatcher.bot.first_name}, ᴩʟᴇᴀsᴇ ʀᴇᴩᴏʀᴛ ɪᴛ ᴀᴛ sᴜᴩᴩᴏʀᴛ ᴄʜᴀᴛ.",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"
                        ),
                        InlineKeyboardButton(
                            text="ᴜᴘᴅᴀᴛᴇ", url=f"https://t.me/roy_editx"
                        ),
                    ],
                    [
                        InlineKeyboardButton(text="ʜᴏᴍᴇ", callback_data="mukesh_back"),
                    ],
                ]
            ),
        )
    elif query.data == "mukesh_back":
        first_name = update.effective_user.first_name 
        query.message.edit_caption(PM_START_TEXT.format(escape_markdown(first_name), BOT_NAME,sql.num_users(),sql.num_chats()),
            reply_markup=InlineKeyboardMarkup(buttons),
            parse_mode=ParseMode.MARKDOWN,
            timeout=60,
        )
def MukeshRobot_Main_Callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "Main_help":
        query.message.edit_caption(f"""
 ✦ ʜᴇʀᴇ ɪꜱ ʜᴇʟᴘ ᴍᴇɴᴜ ꜰᴏʀ {BOT_NAME}
""",
            parse_mode=ParseMode.MARKDOWN,
            
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="ᴍᴀɴᴀɢᴇ", callback_data="help_back"),
                        InlineKeyboardButton(text="ᴍᴜsɪᴄ", callback_data="Music_")
                    ],
                    [
                        InlineKeyboardButton(text="ꜱᴘᴀᴍ", callback_data="Music_roy"),
                        InlineKeyboardButton(text="ᴇxᴛʀᴀ", callback_data="source_") 
                    ],
                    [
                        InlineKeyboardButton(text="ᴀɴɪᴍᴇ", callback_data="Music_avi"),
                        InlineKeyboardButton(text="ʜᴏᴍᴇ", callback_data="mukesh_back")
                    ]
                ]
            ),
            )
    elif query.data=="basic_help":
        query.message.edit_caption("""✿ ʙᴀsɪᴄ ᴄᴏᴍᴍᴀɴᴅs ✿
        
❅ ᴀᴠᴀɪʟᴀʙʟᴇ ᴛᴏ ᴀᴅᴍɪɴs ❅

❍ /reload ➛ ᴜᴘᴅᴀᴛᴇs ᴛʜᴇ ᴀᴅᴍɪɴs ʟɪsᴛ ᴀɴᴅ ᴛʜᴇɪʀ ᴘʀɪᴠɪʟᴇɢᴇs.
❍ /settings ➛ ʟᴇᴛs ʏᴏᴜ ᴍᴀɴᴀɢᴇ ᴀʟʟ ᴛʜᴇ Bᴏᴛ sᴇᴛᴛɪɴɢs ɪɴ ᴀ ɢʀᴏᴜᴘ.
❍ /ban ➛ ʟᴇᴛs ʏᴏᴜ ʙᴀɴ ᴀ ᴜsᴇʀ ғʀᴏᴍ ᴛʜᴇ ɢʀᴏᴜᴘ ᴡɪᴛʜᴏᴜᴛ ɢɪᴠɪɴɢ ʜɪᴍ ᴛʜᴇ ᴘᴏssɪʙɪʟɪᴛʏ ᴛᴏ ᴊᴏɪɴ ᴀɢᴀɪɴ ᴜsɪɴɢ ᴛʜᴇ ʟɪɴᴋ ᴏғ ᴛʜᴇ ɢʀᴏᴜᴘ.
❍ /mute ➛ ᴘᴜᴛs ᴀ ᴜsᴇʀ ɪɴ ʀᴇᴀᴅ-ᴏɴʟʏ ᴍᴏᴅᴇ. Hᴇ ᴄᴀɴ ʀᴇᴀᴅ ʙᴜᴛ ʜᴇ ᴄᴀɴ'ᴛ sᴇɴᴅ ᴀɴʏ ᴍᴇssᴀɢᴇs.
❍ /kick ➛ ʙᴀɴs ᴀ ᴜsᴇʀ ғʀᴏᴍ ᴛʜᴇ ɢʀᴏᴜᴘ, ɢɪᴠɪɴɢ ʜɪᴍ ᴛʜᴇ ᴘᴏssɪʙɪʟɪᴛʏ ᴛᴏ Jᴏɪɴ ᴀɢᴀɪɴ ᴡɪᴛʜ ᴛʜᴇ ʟɪɴᴋ ᴏғ ᴛʜᴇ ɢʀᴏᴜᴘ.
❍ /unban ➛ ʟᴇᴛs ʏᴏᴜ ʀᴇᴍᴏᴠᴇ ᴀ ᴜsᴇʀ ғʀᴏᴍ ɢʀᴏᴜᴘ's ʙʟᴀᴄᴋʟɪsᴛ, ɢɪᴠɪɴɢ ᴛʜᴇᴍ ᴛʜᴇ ᴘᴏssɪʙɪʟɪᴛʏ ᴛᴏ Jᴏɪɴ ᴀɢᴀɪɴ ᴡɪᴛʜ ᴛʜᴇ ʟɪɴᴋ ᴏғ ᴛʜᴇ ɢʀᴏᴜᴘ.
❍ /info ➛ ɢɪᴠᴇs ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜsᴇʀ.

❍ /staff ➛ ɢɪᴠᴇs ᴛʜᴇ ᴄᴏᴍᴘʟᴇᴛᴇ ʟɪsᴛ ᴏғ ɢʀᴏᴜᴘ sᴛᴀғғ!.""",parse_mode=ParseMode.MARKDOWN,
            
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="Main_help"),InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", callback_data="mukesh_support")
                    ]
                ]
            ),
            )
    elif query.data=="mukesh_back":
        query.message.edit_caption("""✿ ᴇxᴘᴇʀᴛ ᴄᴏᴍᴍᴀɴᴅs ✿

❅ ᴀᴠᴀɪʟᴀʙʟᴇ ᴛᴏ ᴀᴅᴍɪɴs ❅

❍  /unbanall ➛ ᴍᴇᴍʙᴇʀs ғʀᴏᴍ ʏᴏᴜʀ ɢʀᴏᴜᴘs
❍  /unmuteall ➛ ᴜɴᴍᴜᴛᴇᴀʟʟ ᴀʟʟ ғʀᴏᴍ ʏᴏᴜʀ ɢʀᴏᴜᴘ

❅ ᴘɪɴɴᴇᴅ Mᴇssᴀɢᴇs ❅

❍  /pin ➛ [ᴍᴇssᴀɢᴇ] sᴇɴᴅs ᴛʜᴇ ᴍᴇssᴀɢᴇ ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ ᴘɪɴs ɪᴛ.
❍  /pin ➛ ᴘɪɴs ᴛʜᴇ ᴍᴇssᴀɢᴇ ɪɴ ʀᴇᴘʟʏ
❍  /unpin ➛ ʀᴇᴍᴏᴠᴇs ᴛʜᴇ ᴘɪɴɴᴇᴅ ᴍᴇssᴀɢᴇ.
❍  /adminlist ➛ ʟɪsᴛ ᴏғ ᴀʟʟ ᴛʜᴇ sᴘᴇᴄɪᴀʟ ʀᴏʟᴇs ᴀssɪɢɴᴇᴅ ᴛᴏ ᴜsᴇʀs.

❍ /bug ➛ (ᴍᴇssᴀɢᴇ) ᴛᴏ sᴇɴᴅ ᴍᴇssᴀɢᴇ ᴀɴᴅ ᴇʀʀᴏʀs ᴡʜɪᴄʜ ʏᴏᴜ ᴀʀᴇ ғᴀᴄɪɴɢ 
ᴇx ➛ /bug Hᴇʏ Tʜᴇʀᴇ Is ᴀ sᴏᴍᴇᴛʜɪɴɢ ᴇʀʀᴏʀ @username ᴏғ ᴄʜᴀᴛ! .""",parse_mode=ParseMode.MARKDOWN,
            
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="Main_help"),InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", callback_data="mukesh_support")
                    ]
                ]
            ),
            )                                        
    elif query.data=="advance_help":
        query.message.edit_caption("""✿ ᴀᴅᴠᴀɴᴄᴇᴅ ᴄᴏᴍᴍᴀɴᴅs ✿

❅ ᴡᴀʀɴ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙʏ ᴀᴅᴍɪɴs ❅

❍ /warn ➛ ᴀᴅᴅs ᴀ ᴡᴀʀɴ ᴛᴏ ᴛʜᴇ ᴜsᴇʀ
❍ /unwarn ➛ ʀᴇᴍᴏᴠᴇs ᴀ ᴡᴀʀɴ ᴛᴏ ᴛʜᴇ ᴜsᴇʀ
❍ /warns ➛ ʟᴇᴛs ʏᴏᴜ sᴇᴇ ᴀɴᴅ ᴍᴀɴᴀɢᴇ ᴜsᴇʀ ᴡᴀʀɴs

❍ /del ➛ ᴅᴇʟᴇᴛᴇs ᴛʜᴇ sᴇʟᴇᴄᴛᴇᴅ ᴍᴇssᴀɢᴇ
❍ /purge ➛ ᴅᴇʟᴇᴛᴇs ғʀᴏᴍ ᴛʜᴇ sᴇʟᴇᴄᴛᴇᴅ ᴍᴇssᴀɢᴇ.""",parse_mode=ParseMode.MARKDOWN,
            
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="Main_help"),InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", callback_data="mukesh_support")
                    ]
                ]
            ),
            )
    elif query.data=="expert_help":
        query.message.edit_caption(f"""━━━━━━━━━━━━━━━━━━━━
❍ ᴍᴀᴋᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴇꜰꜰᴇᴄᴛɪᴠᴇ ɴᴏᴡ.

❍ [{BOT_NAME}]("https://t.me/{BOT_USERNAME}") ɴᴏᴡ ʀᴇᴀᴅʏ ᴛᴏ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

❍ ᴀᴅᴍɪɴ ᴛᴏᴏʟꜱ ➛ ʙᴀꜱɪᴄ ᴀᴅᴍɪɴ ᴛᴏᴏʟꜱ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴘʀᴏᴛᴇᴄᴛ & ᴘᴏᴡᴇʀᴜᴘ ʏᴏᴜʀ ɢʀᴏᴜᴘ. ʏᴏᴜ ᴄᴀɴ ʙᴀɴ, ᴋɪᴄᴋ, ᴘʀᴏᴍᴏᴛᴇᴍᴇᴍʙᴇʀꜱ ᴀꜱ ᴀᴅᴍɪɴ ᴛʜʀᴏᴜɢʜ ʙᴏᴛ.

❍ ɢʀᴇᴇᴛɪɴɢꜱ ➛ ʟᴇᴛꜱ ꜱᴇᴛ ᴀ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴡᴇʟᴄᴏᴍᴇ ɴᴇᴡ ᴜꜱᴇʀꜱ ᴄᴏᴍɪɴɢ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ. ꜱᴇɴᴅ /setwelcome ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ꜱᴇᴛ ᴀ ᴡᴇʟᴄᴏᴍᴇ ᴍᴇꜱꜱᴀɢᴇ!""",
                                   
            parse_mode=ParseMode.MARKDOWN,
            
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="Main_help"),InlineKeyboardButton(text="ᴇxᴛʀᴀ", callback_data="mukesh_support")
                    ]
                ]
            ),
            )
    elif query.data=="donation_help":
        query.message.edit_caption("""💥 ᴀʀᴛɪғɪᴄɪᴀʟ ɪɴᴛᴇʟ ʟɪɢᴇɴᴄᴇ ғᴜɴᴄᴛɪᴏɴs 💥\n\n✿ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ✿\n\n❍ ᴀʙᴏᴜᴛ ➛ ᴛʜᴇ ᴀᴅᴠᴀɴᴄᴇᴅ ᴄʜᴀᴛ ɢᴘᴛ ᴀɪ - 4 ᴍᴏᴅᴇʟ ꜰᴏʀ ᴀɴ ᴇɴʜᴀɴᴄᴇᴅ ᴄʜᴀᴛ ᴇxᴘᴇʀɪᴇɴᴄᴇ. \n\n❍ ᴛʜɪꜱ ɪꜱ ᴀ ɴᴇᴡ ꜰᴇᴀᴛᴜʀᴇ, ᴀɴᴅ ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ɪᴛ ᴜɴʟɪᴍɪᴛᴇᴅʟʏ...\n\n❍ /ask ➛ ᴀ ᴄʜᴀᴛʙᴏᴛ ᴜsɪɴɢ ɢᴘᴛ ғᴏʀ ʀᴇsᴘᴏɴᴅɪɴɢ ᴛᴏ ᴜsᴇʀ ǫᴜᴇʀɪᴇs.""",parse_mode=ParseMode.MARKDOWN,
            
            reply_markup=InlineKeyboardMarkup(
                [ 
                    [
                        InlineKeyboardButton(text="ᴅᴏɴᴀᴛᴇ", url="https://t.me/roy_editx"),InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", callback_data="mukesh_support")
                    ]
                ]
            ),
            )  
def Source_about_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "source_":
        query.message.edit_caption(
            f"""✦ ʜᴇʀᴇ ɪs sᴏᴍᴇ ʙᴀsɪᴄ ᴄᴏᴍᴍᴀᴅs ғᴏʀ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇ.
""",
            parse_mode=ParseMode.MARKDOWN,
            
            reply_markup=InlineKeyboardMarkup(
                [
                     [
                        InlineKeyboardButton(text="ʙᴀsɪᴄ", callback_data="basic_help"),
                        InlineKeyboardButton(text="ᴇxᴘᴇʀᴛ", callback_data="expert_help")
                    ],
                    [
                        InlineKeyboardButton(text="ᴀᴅᴠᴀɴᴄᴇ", callback_data="advance_help"),
                        InlineKeyboardButton(text="ᴄʜᴀᴛ ᴀɪ", callback_data="donation_help") 
                    ],
                    [
                        InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="Main_help")
                    ],
                ]
            ),
        )
    elif query.data == "source_back":
        first_name = update.effective_user.first_name
        query.message.edit_caption(
            PM_START_TEXT.format(escape_markdown(first_name), BOT_NAME,sql.num_users(),sql.num_chats()),
            reply_markup=InlineKeyboardMarkup(buttons),
            parse_mode=ParseMode.MARKDOWN,
            timeout=60,
            
        )

        
def Music_about_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "Music_":
        query.message.edit_caption(f"""✿ ʜᴇʀᴇ ɪꜱ ʜᴇʟᴘ ᴍᴇɴᴜ ꜰᴏʀ ᴍᴜꜱɪᴄ ✿""",
            parse_mode=ParseMode.MARKDOWN,
            
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="ᴀᴅᴍɪɴ", callback_data="Music_admin"
                        ),
                        InlineKeyboardButton(
                            text="ᴘʟᴀʏ", callback_data="Music_play"
                        ),
                    ],
                    [
                        InlineKeyboardButton(text="ʙᴏᴛ", callback_data="Music_bot"),
                        InlineKeyboardButton(
                            text="ᴇxᴛʀᴀ",
                            callback_data="Music_extra",
                        ),
                    ],
                    [
                        InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="Main_help")
                    ],
                ]
            ),
        )
    elif query.data == "Music_admin":
        query.message.edit_caption(f"*✿ ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅꜱ ✿*"
            f"""
❅ ᴀᴅᴍɪɴs ᴀɴᴅ ᴀᴜᴛʜ ᴜsᴇʀᴀ ᴄᴏᴍᴍᴀɴᴅs ❅

❍ /pause ➛ ᴩᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ.

❍ /resume ➛ ʀᴇsᴜᴍᴇ ᴛʜᴇ ᴩᴀᴜsᴇᴅ sᴛʀᴇᴀᴍ.

❍ /skip ➛ sᴋɪᴩ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴀɴᴅ sᴛᴀʀᴛ sᴛʀᴇᴀᴍɪɴɢ ᴛʜᴇ ɴᴇxᴛ ᴛʀᴀᴄᴋ ɪɴ ǫᴜᴇᴜᴇ.

❍ /end ᴏʀ /stop ➛ ᴄʟᴇᴀʀs ᴛʜᴇ ǫᴜᴇᴜᴇ ᴀɴᴅ ᴇɴᴅ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ.

❍ /player ➛ ɢᴇᴛ ᴀ ɪɴᴛᴇʀᴀᴄᴛɪᴠᴇ ᴩʟᴀʏᴇʀ ᴩᴀɴᴇʟ.

❍ /queue ➛ sʜᴏᴡs ᴛʜᴇ ǫᴜᴇᴜᴇᴅ ᴛʀᴀᴄᴋs ʟɪsᴛ.
""",
            parse_mode=ParseMode.MARKDOWN,
            
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=" ʙᴀᴄᴋ ", callback_data="Music_"),InlineKeyboardButton(text="ᴛᴏᴏʟs", callback_data="mukesh_support")
                    ]
                ]
            ),
        )
    elif query.data == "Music_play":
        query.message.edit_caption(f"*✿ ᴘʟᴀʏ ᴄᴏᴍᴍᴀɴᴅꜱ ✿*"
            f"""
❍ /play ᴏʀ /vplay ᴏʀ /cplay ➛ ʙᴏᴛ ᴡɪʟʟ ꜱᴛᴀʀᴛ ᴘʟᴀʏɪɴɢ ʏᴏᴜʀ ɢɪᴠᴇɴ ϙᴜᴇʀʏ on ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴏʀ ꜱᴛʀᴇᴀᴍ ʟɪᴠᴇ ʟɪɴᴋꜱ ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛꜱ.

❍ /playforce ᴏʀ /vplayforce ᴏʀ /cplayforce ➛ ғᴏʀᴄᴇ ᴘʟᴀʏ ꜱᴛᴏᴘꜱ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ ᴛʀᴀᴄᴋ ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴀɴᴅ ꜱᴛᴀʀᴛꜱ ᴘʟᴀʏɪɴɢ ᴛʜᴇ ꜱᴇᴀʀᴄʜᴇᴅ ᴛʀᴀᴄᴋ ɪɴꜱᴛᴀɴᴛʟʏ ᴡɪᴛʜᴏᴜᴛ ᴅɪꜱᴛᴜʀʙɪɴɢ/clearing queue.

❍ /channelplay ➛ [ᴄʜᴀᴛ ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ɪᴅ] ᴏʀ [ᴅɪꜱᴀʙʟᴇ] - ᴄᴏɴɴᴇᴄᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴀ ɢʀᴏᴜᴘ ᴀɴᴅ ꜱᴛʀᴇᴀᴍ ᴍᴜꜱɪᴄ ᴏɴ ᴄʜᴀɴɴᴇʟ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ғʀᴏᴍ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

 ❅ ʙᴏᴛ ꜱᴇʀᴠᴇʀ ᴘʟᴀʏʟɪꜱᴛꜱ ❅
 
❍ /playlist ➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ꜱᴀᴠᴇᴅ ᴘʟᴀʏʟɪꜱᴛ ᴏɴ ꜱᴇʀᴠᴇʀꜱ.
❍ /deleteplaylist ➛ ᴅᴇʟᴇᴛᴇ ᴀɴʏ ꜱᴀᴠᴇᴅ ᴍᴜꜱɪᴄ ɪɴ ʏᴏᴜʀ ᴘʟᴀʏʟɪꜱᴛ
❍ /play ➛ ꜱᴛᴀʀᴛ ᴘʟᴀʏɪɴɢ ʏᴏᴜʀ ꜱᴀᴠᴇᴅ ᴘʟᴀʏʟɪꜱᴛ ғʀᴏᴍ ꜱᴇʀᴠᴇʀꜱ.
""",
            parse_mode=ParseMode.MARKDOWN,
            
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="Music_"),InlineKeyboardButton(text="ᴇxᴛʀᴀ", callback_data="mukesh_support")
                    ]
                ]
            ),
        )
    elif query.data == "Music_bot":
        query.message.edit_caption(f"*✿ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅꜱ ✿*"
           
            f"""
❍ /stats ➛ ɢᴇᴛ ᴛᴏᴘ 10 ᴛʀᴀᴄᴋꜱ ɢʟᴏʙᴀʟ ꜱᴛᴀᴛꜱ, ᴛᴏᴘ 10 ᴜꜱᴇʀꜱ ᴏғ ʙᴏᴛ, ᴛᴏᴘ 10 ᴄʜᴀᴛꜱ ᴏɴ ʙᴏᴛ, ᴛᴏᴘ 10 ᴘʟᴀʏᴇᴅ ɪɴ ᴀ ᴄʜᴀᴛ ᴇᴛᴄ ᴇᴛᴄ.

❍ /sudolist ➛ ᴄʜᴇᴄᴋ sᴜᴅᴏ ᴜsᴇʀs ᴏғ ᴀʙɢ  ʙᴏᴛ

❍ /lyrics [ᴍᴜsɪᴄ ɴᴀᴍᴇ] ➛ sᴇᴀʀᴄʜᴇs ʟʏʀɪᴄs ғᴏʀ ᴛʜᴇ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴍᴜsɪᴄ ᴏɴ ᴡᴇʙ.

❍ /song [ᴛʀᴀᴄᴋ ɴᴀᴍᴇ] or [ʏᴛ ʟɪɴᴋ] ➛ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ ᴛʀᴀᴄᴋ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ ɪɴ ᴍᴘ3 or ᴍᴘ4 ғᴏʀᴍᴀᴛꜱ.

❍ /player ➛  ɢᴇt ᴀ ɪɴᴛᴇʀᴀᴄᴛɪᴠᴇ ᴘʟᴀʏɪɴɢ ᴘᴀɴᴇʟ.

❅ c ꜱᴛᴀɴᴅꜱ ꜰᴏʀ ᴄʜᴀɴɴᴇʟ ᴘʟᴀʏ ❅

❍ /queue ᴏʀ /cqueue ➛ ᴄʜᴇᴄᴋ Qᴜᴇᴜᴇ ʟɪꜱᴛ ᴏꜰ ᴍᴜꜱɪᴄ.
""",
            parse_mode=ParseMode.MARKDOWN,
            
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=" ʙᴀᴄᴋ ", callback_data="Music_"),InlineKeyboardButton(text="ᴛᴏᴏʟs", callback_data="mukesh_support")
                    ]
                ]
            ),
        )
    elif query.data == "Music_extra":
        query.message.edit_caption(f"*✿ ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅꜱ ✿*"
            
             f"""
❍ /mstart ➛ ꜱᴛᴀʀᴛ ᴛʜᴇ ᴍᴜꜱɪᴄ ʙᴏᴛ.

❍ /mhelp ➛ ɢᴇᴛ ᴄᴏᴍᴍᴀɴᴅꜱ ʜᴇʟᴘᴇʀ ᴍᴇɴᴜ ᴡɪᴛʜ ᴅᴇᴛᴀɪʟᴇᴅ ᴇxᴘʟᴀɴᴀᴛɪᴏɴꜱ ᴏғ ᴄᴏᴍᴍᴀɴᴅꜱ.

❍ /ping ➛ ᴘɪɴɢ ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ ᴄʜᴇᴄᴋ ʀᴀᴍ, ᴄᴘᴜ ᴇᴛᴄ ꜱᴛᴀᴛꜱ ᴏғ ʙᴏᴛ.

*❅ ɢʀᴏᴜᴘ ꜱᴇᴛᴛɪɴɢꜱ ❅*

❍ /settings ➛ ɢᴇᴛ a ᴄᴏᴍᴘʟᴇᴛᴇ ɢʀᴏᴜᴘ ꜱᴇᴛᴛɪɴɢꜱ ᴡɪᴛʜ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴꜱ
""",
            parse_mode=ParseMode.MARKDOWN,
            
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=" ʙᴀᴄᴋ ", callback_data="Music_"),InlineKeyboardButton(text="ᴛᴏᴏʟs", callback_data="mukesh_support")
                    ]
                ]
            ),
        )
    elif query.data == "Music_back":
        first_name = update.effective_user.first_name
        query.message.edit_caption(PM_START_TEXT.format(escape_markdown(first_name), BOT_NAME),
            reply_markup=InlineKeyboardMarkup(buttons),
            parse_mode=ParseMode.MARKDOWN,
            timeout=60,

        )

    query = update.callback_query
    if query.data == "Music_roy":
        query.message.edit_caption(f"""✿ ʜᴇʀᴇ ɪꜱ ʜᴇʟᴘ ᴍᴇɴᴜ ꜰᴏʀ ꜱᴘᴀᴍ ʀᴀɪᴅ ✿""",
            parse_mode=ParseMode.MARKDOWN,
            
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="ꜱᴘᴀᴍ", callback_data="Music_roy_admin"
                        ),
                        InlineKeyboardButton(
                            text="ʀᴀɪᴅ", callback_data="Music_roy_play"
                        ),
                    ],
                    [
                        InlineKeyboardButton(text="ᴏᴡɴᴇʀ", callback_data="Music_roy_bot"),
                        InlineKeyboardButton(
                            text="ᴇxᴛʀᴀ",
                            callback_data="Music_roy_extra",
                        ),
                    ],
                    [
                        InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="Main_help")
                    ],
                ]
            ),
        )
    elif query.data == "Music_roy_admin":
        query.message.edit_caption(f"*✿ ꜱᴘᴀᴍ  ᴄᴏᴍᴍᴀɴᴅꜱ ✿*"
            f"""\n\n֍ 𝗦𝗽𝗮𝗺 ➠ ๏ ꜱᴘᴀᴍꜱ ᴀ ᴍᴇꜱꜱᴀɢᴇ. ๏\n  ๛ /spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)\n  ๛ /spam <count> <replying any message>\n\n֍ 𝗣𝗼𝗿𝗻𝗦𝗽𝗮𝗺 ➠ ๏ ᴘᴏʀᴍᴏɢʀᴀᴘʜʏ ꜱᴘᴀᴍ. ๏\n  ๛ /pspam <count>\n\n֍ 𝗛𝗮𝗻𝗴 ➠ ๏ ꜱᴘᴀᴍꜱ ʜᴀɴɢɪɴɢ ᴍᴇꜱꜱᴀɢᴇ ꜰᴏʀ ɢɪᴠᴇɴ ᴄᴏᴜɴᴛᴇʀ.""",
            parse_mode=ParseMode.MARKDOWN,
            
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=" ʙᴀᴄᴋ ", callback_data="Music_roy"),InlineKeyboardButton(text="ᴛᴏᴏʟs", callback_data="mukesh_support")
                    ]
                ]
            ),
        )
    elif query.data == "Music_roy_play":
        query.message.edit_caption(f"*✿ ʀᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅꜱ ✿*"
            f"""\n\n֍ 𝗥𝗮𝗶𝗱 ➠ ๏ ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜꜱᴇʀ ꜰᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ. ๏\n  ๛ /raid <count> <username>\n  ๛ /raid <count> <reply to user>\n\n֍ 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱 ➠ ๏ ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ. ๏\n  ๛ /rraid <replying to user>\n  ๛ /rraid <username>\n\n֍ 𝗗𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱 ➠ ๏ ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ. ๏\n  ๛ /drraid <replying to user>\n  ๛ /drraid <username>\n\n֍ 𝐌𝐑𝐚𝐢𝐝 ➠ ๏ ʟᴏᴠᴇ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ. ๏\n  ๛ /mraid <count> <username>\n  ๛ /mraid <count> <reply to user>\n\n֍ 𝐒𝐑𝐚𝐢𝐝 ➠ ๏ ꜱʜᴀʏᴀʀɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ. ๏\n  ๛ /sraid <count> <username>\n  ๛ /sraid <count> <reply to user>\n\n֍ 𝐂𝐑𝐚𝐢𝐝 ➠ ๏ ᴀʙᴄᴅ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ. ๏\n  ๛ /craid <count> <username>\n  ๛ /craid <count> <reply to user>""",
            parse_mode=ParseMode.MARKDOWN,
            
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="Music_roy"),InlineKeyboardButton(text="ᴇxᴛʀᴀ", callback_data="mukesh_support")
                    ]
                ]
            ),
        )
    elif query.data == "Music_roy_bot":
        query.message.edit_caption(f"*✿ ʙᴏᴛ ᴏᴡɴᴇʀ ᴄᴏᴍᴍᴀɴᴅꜱ ✿*"
           
            f"""\n\n֍ 𝗨𝘀𝗲𝗿𝗕𝗼𝘁 ➠ ๏ ᴜꜱᴇʀʙᴏᴛ ᴄᴍᴅꜱ ๏\n  ๛ /ping \n  ๛ /reboot\n  ๛ /sudo <reply to user>  ➛ Owner Cmd\n  ๛ /logs ➛ Owner Cmd\n\n֍ 𝗘𝗰𝗵𝗼 ➠ ๏ ᴛᴏ ᴀᴄᴛɪᴠᴇ ᴇᴄʜᴏ ᴏɴ ᴀɴʏ ᴜꜱᴇʀ ๏\n  ๛ /echo <reply to user>\n  ๛ /rmecho <reply to user>\n\n֍ 𝗟𝗲𝗮𝘃𝗲 ➠ ๏ ᴛᴏ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ๏\n  ๛ /leave <group/chat id>\n  ๛ /leave ➛ Type in the Group bot will auto leave that group""",
            parse_mode=ParseMode.MARKDOWN,
            
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=" ʙᴀᴄᴋ ", callback_data="Music_roy"),InlineKeyboardButton(text="ᴛᴏᴏʟs", callback_data="mukesh_support")
                    ]
                ]
            ),
        )
    elif query.data == "Music_roy_extra":
        query.message.edit_caption(f"*✿ ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅꜱ ✿*"
            
             f"""
❍ /mstart ➛ ꜱᴛᴀʀᴛ ᴛʜᴇ ᴍᴜꜱɪᴄ ʙᴏᴛ.

❍ /mhelp ➛ ɢᴇᴛ ᴄᴏᴍᴍᴀɴᴅꜱ ʜᴇʟᴘᴇʀ ᴍᴇɴᴜ ᴡɪᴛʜ ᴅᴇᴛᴀɪʟᴇᴅ ᴇxᴘʟᴀɴᴀᴛɪᴏɴꜱ ᴏғ ᴄᴏᴍᴍᴀɴᴅꜱ.

❍ /ping ➛ ᴘɪɴɢ ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ ᴄʜᴇᴄᴋ ʀᴀᴍ, ᴄᴘᴜ ᴇᴛᴄ ꜱᴛᴀᴛꜱ ᴏғ ʙᴏᴛ.

*❅ ɢʀᴏᴜᴘ ꜱᴇᴛᴛɪɴɢꜱ ❅*

❍ /settings ➛ ɢᴇᴛ a ᴄᴏᴍᴘʟᴇᴛᴇ ɢʀᴏᴜᴘ ꜱᴇᴛᴛɪɴɢꜱ ᴡɪᴛʜ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴꜱ
""",
            parse_mode=ParseMode.MARKDOWN,
            
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=" ʙᴀᴄᴋ ", callback_data="Music_roy"),InlineKeyboardButton(text="ᴛᴏᴏʟs", callback_data="mukesh_support")
                    ]
                ]
            ),
        )
    elif query.data == "Music_back":
        first_name = update.effective_user.first_name
        query.message.edit_caption(PM_START_TEXT.format(escape_markdown(first_name), BOT_NAME),
            reply_markup=InlineKeyboardMarkup(buttons),
            parse_mode=ParseMode.MARKDOWN,
            timeout=60,

                        )
                    
def Music_about_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "Music_avi":
        query.message.edit_caption(f"""✿ ʜᴇʀᴇ ɪꜱ ʜᴇʟᴘ ᴍᴇɴᴜ ꜰᴏʀ ᴍᴜꜱɪᴄ ✿""",
            parse_mode=ParseMode.MARKDOWN,
            
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="ʜᴇʀᴇᴍ", callback_data="Music_avi_admin"
                        ),
                        InlineKeyboardButton(
                            text="ᴡᴀɪғᴜ", callback_data="Music_avi_play"
                        ),
                    ],
                    [
                        InlineKeyboardButton(text="ᴀɪʀɪɴɢ", callback_data="Music_avi_bot"),
                        InlineKeyboardButton(
                            text="ᴇxᴛʀᴀ",
                            callback_data="Music_avi_extra",
                        ),
                    ],
                    [
                        InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="Main_help")
                    ],
                ]
            ),
        )
    elif query.data == "Music_avi_admin":
        query.message.edit_caption(f"*✿ ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅꜱ ✿*"
            f"""
❅ ᴀᴅᴍɪɴs ᴀɴᴅ ᴀᴜᴛʜ ᴜsᴇʀᴀ ᴄᴏᴍᴍᴀɴᴅs ❅

❍ /pause ➛ ᴩᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ.

❍ /resume ➛ ʀᴇsᴜᴍᴇ ᴛʜᴇ ᴩᴀᴜsᴇᴅ sᴛʀᴇᴀᴍ.

❍ /skip ➛ sᴋɪᴩ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴀɴᴅ sᴛᴀʀᴛ sᴛʀᴇᴀᴍɪɴɢ ᴛʜᴇ ɴᴇxᴛ ᴛʀᴀᴄᴋ ɪɴ ǫᴜᴇᴜᴇ.

❍ /end ᴏʀ /stop ➛ ᴄʟᴇᴀʀs ᴛʜᴇ ǫᴜᴇᴜᴇ ᴀɴᴅ ᴇɴᴅ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ.

❍ /player ➛ ɢᴇᴛ ᴀ ɪɴᴛᴇʀᴀᴄᴛɪᴠᴇ ᴩʟᴀʏᴇʀ ᴩᴀɴᴇʟ.

❍ /queue ➛ sʜᴏᴡs ᴛʜᴇ ǫᴜᴇᴜᴇᴅ ᴛʀᴀᴄᴋs ʟɪsᴛ.
""",
            parse_mode=ParseMode.MARKDOWN,
            
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=" ʙᴀᴄᴋ ", callback_data="Music_avi"),InlineKeyboardButton(text="ᴛᴏᴏʟs", callback_data="mukesh_support")
                    ]
                ]
            ),
        )
    elif query.data == "Music_avi_play":
        query.message.edit_caption(f"*✿ ᴘʟᴀʏ ᴄᴏᴍᴍᴀɴᴅꜱ ✿*"
            f"""
❍ /play ᴏʀ /vplay ᴏʀ /cplay ➛ ʙᴏᴛ ᴡɪʟʟ ꜱᴛᴀʀᴛ ᴘʟᴀʏɪɴɢ ʏᴏᴜʀ ɢɪᴠᴇɴ ϙᴜᴇʀʏ on ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴏʀ ꜱᴛʀᴇᴀᴍ ʟɪᴠᴇ ʟɪɴᴋꜱ ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛꜱ.

❍ /playforce ᴏʀ /vplayforce ᴏʀ /cplayforce ➛ ғᴏʀᴄᴇ ᴘʟᴀʏ ꜱᴛᴏᴘꜱ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ ᴛʀᴀᴄᴋ ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴀɴᴅ ꜱᴛᴀʀᴛꜱ ᴘʟᴀʏɪɴɢ ᴛʜᴇ ꜱᴇᴀʀᴄʜᴇᴅ ᴛʀᴀᴄᴋ ɪɴꜱᴛᴀɴᴛʟʏ ᴡɪᴛʜᴏᴜᴛ ᴅɪꜱᴛᴜʀʙɪɴɢ/clearing queue.

❍ /channelplay ➛ [ᴄʜᴀᴛ ᴜꜱᴇʀɴᴀᴍᴇ ᴏʀ ɪᴅ] ᴏʀ [ᴅɪꜱᴀʙʟᴇ] - ᴄᴏɴɴᴇᴄᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴀ ɢʀᴏᴜᴘ ᴀɴᴅ ꜱᴛʀᴇᴀᴍ ᴍᴜꜱɪᴄ ᴏɴ ᴄʜᴀɴɴᴇʟ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ғʀᴏᴍ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

 ❅ ʙᴏᴛ ꜱᴇʀᴠᴇʀ ᴘʟᴀʏʟɪꜱᴛꜱ ❅
 
❍ /playlist ➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ꜱᴀᴠᴇᴅ ᴘʟᴀʏʟɪꜱᴛ ᴏɴ ꜱᴇʀᴠᴇʀꜱ.
❍ /deleteplaylist ➛ ᴅᴇʟᴇᴛᴇ ᴀɴʏ ꜱᴀᴠᴇᴅ ᴍᴜꜱɪᴄ ɪɴ ʏᴏᴜʀ ᴘʟᴀʏʟɪꜱᴛ
❍ /play ➛ ꜱᴛᴀʀᴛ ᴘʟᴀʏɪɴɢ ʏᴏᴜʀ ꜱᴀᴠᴇᴅ ᴘʟᴀʏʟɪꜱᴛ ғʀᴏᴍ ꜱᴇʀᴠᴇʀꜱ.
""",
            parse_mode=ParseMode.MARKDOWN,
            
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="Music_avi"),InlineKeyboardButton(text="ᴇxᴛʀᴀ", callback_data="mukesh_support")
                    ]
                ]
            ),
        )
    elif query.data == "Music_avi_bot":
        query.message.edit_caption(f"*✿ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅꜱ ✿*"
           
            f"""
❍ /stats ➛ ɢᴇᴛ ᴛᴏᴘ 10 ᴛʀᴀᴄᴋꜱ ɢʟᴏʙᴀʟ ꜱᴛᴀᴛꜱ, ᴛᴏᴘ 10 ᴜꜱᴇʀꜱ ᴏғ ʙᴏᴛ, ᴛᴏᴘ 10 ᴄʜᴀᴛꜱ ᴏɴ ʙᴏᴛ, ᴛᴏᴘ 10 ᴘʟᴀʏᴇᴅ ɪɴ ᴀ ᴄʜᴀᴛ ᴇᴛᴄ ᴇᴛᴄ.

❍ /sudolist ➛ ᴄʜᴇᴄᴋ sᴜᴅᴏ ᴜsᴇʀs ᴏғ ᴀʙɢ  ʙᴏᴛ

❍ /lyrics [ᴍᴜsɪᴄ ɴᴀᴍᴇ] ➛ sᴇᴀʀᴄʜᴇs ʟʏʀɪᴄs ғᴏʀ ᴛʜᴇ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴍᴜsɪᴄ ᴏɴ ᴡᴇʙ.

❍ /song [ᴛʀᴀᴄᴋ ɴᴀᴍᴇ] or [ʏᴛ ʟɪɴᴋ] ➛ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ ᴛʀᴀᴄᴋ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ ɪɴ ᴍᴘ3 or ᴍᴘ4 ғᴏʀᴍᴀᴛꜱ.

❍ /player ➛  ɢᴇt ᴀ ɪɴᴛᴇʀᴀᴄᴛɪᴠᴇ ᴘʟᴀʏɪɴɢ ᴘᴀɴᴇʟ.

❅ c ꜱᴛᴀɴᴅꜱ ꜰᴏʀ ᴄʜᴀɴɴᴇʟ ᴘʟᴀʏ ❅

❍ /queue ᴏʀ /cqueue ➛ ᴄʜᴇᴄᴋ Qᴜᴇᴜᴇ ʟɪꜱᴛ ᴏꜰ ᴍᴜꜱɪᴄ.
""",
            parse_mode=ParseMode.MARKDOWN,
            
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=" ʙᴀᴄᴋ ", callback_data="Music_avi"),InlineKeyboardButton(text="ᴛᴏᴏʟs", callback_data="mukesh_support")
                    ]
                ]
            ),
        )
    elif query.data == "Music_avi_extra":
        query.message.edit_caption(f"*✿ ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅꜱ ✿*"
            
             f"""
❍ /mstart ➛ ꜱᴛᴀʀᴛ ᴛʜᴇ ᴍᴜꜱɪᴄ ʙᴏᴛ.

❍ /mhelp ➛ ɢᴇᴛ ᴄᴏᴍᴍᴀɴᴅꜱ ʜᴇʟᴘᴇʀ ᴍᴇɴᴜ ᴡɪᴛʜ ᴅᴇᴛᴀɪʟᴇᴅ ᴇxᴘʟᴀɴᴀᴛɪᴏɴꜱ ᴏғ ᴄᴏᴍᴍᴀɴᴅꜱ.

❍ /ping ➛ ᴘɪɴɢ ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ ᴄʜᴇᴄᴋ ʀᴀᴍ, ᴄᴘᴜ ᴇᴛᴄ ꜱᴛᴀᴛꜱ ᴏғ ʙᴏᴛ.

*❅ ɢʀᴏᴜᴘ ꜱᴇᴛᴛɪɴɢꜱ ❅*

❍ /settings ➛ ɢᴇᴛ a ᴄᴏᴍᴘʟᴇᴛᴇ ɢʀᴏᴜᴘ ꜱᴇᴛᴛɪɴɢꜱ ᴡɪᴛʜ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴꜱ
""",
            parse_mode=ParseMode.MARKDOWN,
            
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=" ʙᴀᴄᴋ ", callback_data="Music_avi"),InlineKeyboardButton(text="ᴛᴏᴏʟs", callback_data="mukesh_support")
                    ]
                ]
            ),
        )
    elif query.data == "Music_back":
        first_name = update.effective_user.first_name
        query.message.edit_caption(PM_START_TEXT.format(escape_markdown(first_name), BOT_NAME),
            reply_markup=InlineKeyboardMarkup(buttons),
            parse_mode=ParseMode.MARKDOWN,
            timeout=60,

           )
        
def get_help(update: Update, context: CallbackContext):
    chat = update.effective_chat  # type: Optional[Chat]
    args = update.effective_message.text.split(None, 1)

    # ONLY send help in PM
    if chat.type != chat.PRIVATE:
        if len(args) >= 2 and any(args[1].lower() == x for x in HELPABLE):
            module = args[1].lower()
            update.effective_message.reply_photo(random.choice(ABHI),
                f"❍ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ɪɴ ᴘᴍ ᴛᴏ ɢᴇᴛ ʜᴇʟᴘ ᴏғ {module.capitalize()}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="ʜᴇʟᴘ",
                                url="t.me/{}?start=ghelp_{}".format(
                                    context.bot.username, module
                                ),
                            )
                        ]
                    ]
                ),
            )
            return
        update.effective_message.reply_photo(random.choice(NYKAA),"❍ ᴡʜᴇʀᴇ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴏᴘᴇɴ ᴛʜᴇ sᴇᴛᴛɪɴɢs ᴍᴇɴᴜ?.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="ᴏᴩᴇɴ ɪɴ ᴩʀɪᴠᴀᴛᴇ",
                            url="https://t.me/{}?start=help".format(context.bot.username),
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            text="ᴏᴩᴇɴ ʜᴇʀᴇ",
                            callback_data="help_back",
                        )
                    ],
                ]
            ),
        )
        return

    elif len(args) >= 2 and any(args[1].lower() == x for x in HELPABLE):
        module = args[1].lower()
        text = (
            "Here is the available help for the *{}* module:\n".format(
                HELPABLE[module].__mod_name__
            )
            + HELPABLE[module].__help__
        )
        send_help(
            chat.id,
            text,
            InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="◁", callback_data="help_back"),InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", callback_data="mukesh_support")]]
            ),
        )

    else:
        send_help(chat.id, HELP_STRINGS)


def send_settings(chat_id, user_id, user=False):
    if user:
        if USER_SETTINGS:
            settings = "\n\n".join(
                "*{}*:\n{}".format(mod.__mod_name__, mod.__user_settings__(user_id))
                for mod in USER_SETTINGS.values()
            )
            dispatcher.bot.send_message(
                user_id,
                "These are your current settings:" + "\n\n" + settings,
                parse_mode=ParseMode.MARKDOWN,
            )

        else:
            dispatcher.bot.send_message(
                user_id,
                "Seems like there aren't any user specific settings available :'(",
                parse_mode=ParseMode.MARKDOWN,
            )

    else:
        if CHAT_SETTINGS:
            chat_name = dispatcher.bot.getChat(chat_id).title
            dispatcher.bot.send_message(
                user_id,
                text="Which module would you like to check {}'s settings for?".format(
                    chat_name
                ),
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(0, CHAT_SETTINGS, "stngs", chat=chat_id)
                ),
            )
        else:
            dispatcher.bot.send_message(
                user_id,
                "Seems like there aren't any chat settings available :'(\nSend this "
                "in a group chat you're admin in to find its current settings!",
                parse_mode=ParseMode.MARKDOWN,
            )


def settings_button(update: Update, context: CallbackContext):
    query = update.callback_query
    user = update.effective_user
    bot = context.bot
    mod_match = re.match(r"stngs_module\((.+?),(.+?)\)", query.data)
    prev_match = re.match(r"stngs_prev\((.+?),(.+?)\)", query.data)
    next_match = re.match(r"stngs_next\((.+?),(.+?)\)", query.data)
    back_match = re.match(r"stngs_back\((.+?)\)", query.data)
    try:
        if mod_match:
            chat_id = mod_match.group(1)
            module = mod_match.group(2)
            chat = bot.get_chat(chat_id)
            text = "*{}* has the following settings for the *{}* module:\n\n".format(
                escape_markdown(chat.title), CHAT_SETTINGS[module].__mod_name__
            ) + CHAT_SETTINGS[module].__chat_settings__(chat_id, user.id)
            query.message.reply_text(text,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="◁",
                                callback_data="stngs_back({})".format(chat_id),
                            )
                        ]
                    ]
                ),
            )

        elif prev_match:
            chat_id = prev_match.group(1)
            curr_page = int(prev_match.group(2))
            chat = bot.get_chat(chat_id)
            query.message.reply_text("""Hi there! There are quite a few settings for {} - go ahead and pick what "
                you're interested in.""".format(chat.title),
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(
                        curr_page - 1, CHAT_SETTINGS, "stngs", chat=chat_id
                    )
                ),
            )

        elif next_match:
            chat_id = next_match.group(1)
            next_page = int(next_match.group(2))
            chat = bot.get_chat(chat_id)
            query.message.reply_text(text=
                """Hi there! There are quite a few settings for {} - go ahead and pick what 
                you're interested in.""".format(chat.title),
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(
                        next_page + 1, CHAT_SETTINGS, "stngs", chat=chat_id
                    )
                ),
            )

        elif back_match:
            chat_id = back_match.group(1)
            chat = bot.get_chat(chat_id)
            query.message.reply_text("""Hi there! There are quite a few settings for {} - go ahead and pick what 
                you're interested in.""".format(escape_markdown(chat.title)),
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    paginate_modules(0, CHAT_SETTINGS, "stngs", chat=chat_id)
                ),
            )

        # ensure no spinny white circle
        bot.answer_callback_query(query.id)
        query.message.delete()
    except BadRequest as excp:
        if excp.message not in [
            "Message is not modified",
            "Query_id_invalid",
            "Message can't be deleted",
        ]:
            LOGGER.exception("Exception in settings buttons. %s", str(query.data))


def get_settings(update: Update, context: CallbackContext):
    chat = update.effective_chat  # type: Optional[Chat]
    user = update.effective_user  # type: Optional[User]
    msg = update.effective_message  # type: Optional[Message]

    # ONLY send settings in PM
    if chat.type != chat.PRIVATE:
        if is_user_admin(chat, user.id):
            text = "๏ ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ɢᴇᴛ ᴛʜɪs ᴄʜᴀᴛ's sᴇᴛᴛɪɴɢs ᴀs ᴡᴇʟʟ ᴀs ʏᴏᴜʀs"
            msg.reply_photo(random.choice(ABHI),text,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="sᴇᴛᴛɪɴɢs",
                                url="t.me/{}?start=stngs_{}".format(
                                    context.bot.username, chat.id
                                ),
                            )
                        ]
                    ]
                ),
            )
        else:
            text = "❍ ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ sᴇᴛᴛɪɴɢs"

    else:
        send_settings(chat.id, user.id, True)


def donate(update: Update, context: CallbackContext):
    user = update.effective_message.from_user
    chat = update.effective_chat  # type: Optional[Chat]
    bot = context.bot
    if chat.type == "private":
        update.effective_message.reply_text(
            DONATE_STRING, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True
        )

        if OWNER_ID != 6922271843:
            update.effective_message.reply_text(
                f"๏ ᴛʜᴇ ᴅᴇᴠᴇʟᴏᴩᴇʀ ᴏғ {dispatcher.bot.first_name} sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ɪs [ɢɪᴛʜᴜʙ](https://github.com/noob-mukesh/nothing?)"
                f"\n\n๏ ʙᴜᴛ ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴅᴏɴᴀᴛᴇ ᴛᴏ ᴛʜᴇ ᴩᴇʀsᴏɴ ᴄᴜʀʀᴇɴᴛʟʏ ʀᴜɴɴɪɴɢ ᴍᴇ : [ʜᴇʀᴇ]",
                parse_mode=ParseMode.MARKDOWN,
                
            )

    else:
        try:
            bot.send_message(
                user.id,
                DONATE_STRING,
                parse_mode=ParseMode.MARKDOWN,
                
            )

            update.effective_message.reply_text(
                "❍ ɪᴠᴇ ᴘᴍ'ᴇᴅ ʏᴏᴜ ᴀʙᴏᴜᴛ ᴅᴏɴᴀᴛɪɴɢ ᴛᴏ ᴍʏ ᴄʀᴇᴀᴛᴏʀ!"
            )
        except Unauthorized:
            update.effective_message.reply_text(
                "❍ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ɪɴ ᴘᴍ ғɪʀsᴛ ᴛᴏ ɢᴇᴛ ᴅᴏɴᴀᴛɪᴏɴ ɪɴғᴏʀᴍᴀᴛɪᴏɴ."
            )


def migrate_chats(update: Update, context: CallbackContext):
    msg = update.effective_message  # type: Optional[Message]
    if msg.migrate_to_chat_id:
        old_chat = update.effective_chat.id
        new_chat = msg.migrate_to_chat_id
    elif msg.migrate_from_chat_id:
        old_chat = msg.migrate_from_chat_id
        new_chat = update.effective_chat.id
    else:
        return

    LOGGER.info("Migrating from %s, to %s", str(old_chat), str(new_chat))
    for mod in MIGRATEABLE:
        mod.__migrate__(old_chat, new_chat)

    LOGGER.info("Successfully migrated!")
    raise DispatcherHandlerStop


def main():
    global x
    x=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ",
                            url="https://t.me/avishaxbot?startgroup=true"
                            )
                       ]
                ]
                     )
    if SUPPORT_CHAT is not None and isinstance(SUPPORT_CHAT, str):
        try:
            dispatcher.bot.send_photo(
                f"@{SUPPORT_CHAT}",
                photo=f"{START_IMG}",
                caption=f"""
✦ㅤ{BOT_NAME} ɪs ᴀʟɪᴠᴇ ʙᴀʙʏ ✦
     ━━━━━━━━ 🝮✿🝮 ━━━━━━━━
**❅ ᴍᴀᴅᴇ ʙʏ ➛ [ʀᴏʏ-ᴇᴅɪᴛx](https://t.me/roy_editx)**
**❅ ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ ➛** `{y()}`
**❅ ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ ➛** `{telever}`
**❅ ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ ➛** `{tlhver}`
**❅ ᴩʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ ➛** `{pyrover}`
     ━━━━━━━━ 🝮✿🝮 ━━━━━━━━
""",reply_markup=x,
                parse_mode=ParseMode.MARKDOWN,
            )
        except Unauthorized:
            LOGGER.warning(
                f"Bot isn't able to send message to @{SUPPORT_CHAT}, go and check!"
            )
        except BadRequest as e:
            LOGGER.warning(e.message)
    start_handler = CommandHandler("start", start, run_async=True)

    help_handler = CommandHandler("help", get_help, run_async=True)
    help_callback_handler = CallbackQueryHandler(
        help_button, pattern=r"help_.*", run_async=True
    )

    settings_handler = CommandHandler("settings", get_settings, run_async=True)
    settings_callback_handler = CallbackQueryHandler(
        settings_button, pattern=r"stngs_", run_async=True
    )

    about_callback_handler = CallbackQueryHandler(
        Mukesh_about_callback, pattern=r"mukesh_", run_async=True
    )
    source_callback_handler = CallbackQueryHandler(
        Source_about_callback, pattern=r"source_", run_async=True
    )
    music_callback_handler = CallbackQueryHandler(
        Music_about_callback, pattern=r"Music_",run_async=True
    )
    mukeshrobot_main_handler = CallbackQueryHandler(
        MukeshRobot_Main_Callback, pattern=r".*_help",run_async=True)
    donate_handler = CommandHandler("donate", donate)
    migrate_handler = MessageHandler(Filters.status_update.migrate, migrate_chats)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(about_callback_handler)
    dispatcher.add_handler(music_callback_handler)
    dispatcher.add_handler(settings_handler)
    dispatcher.add_handler(help_callback_handler)
    dispatcher.add_handler(settings_callback_handler)
    dispatcher.add_handler(migrate_handler)
    dispatcher.add_handler(donate_handler)
    dispatcher.add_handler(mukeshrobot_main_handler)
    dispatcher.add_error_handler(error_callback)
    dispatcher.add_handler(source_callback_handler)
    LOGGER.info("Using long polling.")
    updater.start_polling(timeout=15, read_latency=4, drop_pending_updates=True)

    if len(argv) not in (1, 3, 4):
        telethn.disconnect()
    else:
        telethn.run_until_disconnected()

    updater.idle()


if __name__ == "__main__":
    LOGGER.info("Successfully loaded modules: " + str(ALL_MODULES))
    telethn.start(bot_token=TOKEN)
    pbot.start()
    main()
