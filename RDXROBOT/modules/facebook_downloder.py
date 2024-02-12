import os
import re
import requests

from datetime import datetime
from telethon import events

from RDXROBOT.utils.pluginhelpers import is_admin
from RDXROBOT import telethn, BOT_USERNAME, SUPPORT_CHAT


def main(url, filename):
    try:
        download_video("HD", url, filename)
    except (KeyboardInterrupt):
        download_video("SD", url, filename)


def download_video(quality, url, filename):
    html = requests.get(url).content.decode("utf-8")
    video_url = re.search(rf'{quality.lower()}_src:"(.+?)"', html).group(1)
    file_size_request = requests.get(video_url, stream=True)
    int(file_size_request.headers["Content-Length"])
    block_size = 1024
    with open(filename + ".mp4", "wb") as f:
        for data in file_size_request.iter_content(block_size):
            f.write(data)
    print("\nVideo downloaded successfully.")


@telethn.on(events.NewMessage(pattern="^/fbdl (.*)"))
async def _(event):
    if event.fwd_from:
        return
    if await is_admin(event, event.message.sender_id):
        url = event.pattern_match.group(1)
        x = re.match(r"^(https:|)[/][/]www.([^/]+[.])*facebook.com", url)

        if x:
            html = requests.get(url).content.decode("utf-8")
            await event.reply(
                "Starting Video download... \n Please note: FBDL is not for big files."
            )
        else:
            await event.reply(
                "This Video Is Either Private Or URL Is Invalid. Exiting... "
            )
            return

        _qualityhd = re.search('hd_src:"https', html)
        _qualitysd = re.search('sd_src:"https', html)
        _hd = re.search("hd_src:null", html)
        _sd = re.search("sd_src:null", html)

        _thelist = [_qualityhd, _qualitysd, _hd, _sd]
        list = [id for id, val in enumerate(_thelist) if val is not None]
        filename = datetime.strftime(datetime.now(), "%Y-%m-%d-%H-%M-%S")

        main(url, filename)
        await event.reply("Video Downloaded Successfully. Starting To Upload.")

        kk = f"{filename}.mp4"
        caption = f"Facebook Video downloaded Successfully by @{BOT_USERNAME}.\nSay hi to devs @{SUPPORT_CHAT}."

        await telethn.send_file(
            event.chat_id,
            kk,
            caption = f"Facebook Video downloaded Successfully by @{BOT_USERNAME}.\nSay hi to devs @{SUPPORT_CHAT}.",
        )
        os.system(f"rm {kk}")
    else:
        await event.reply("You Should Be Admin To Do This!")
        return
