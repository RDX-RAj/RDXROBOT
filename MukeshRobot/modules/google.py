import glob
import io
import os
import re
import urllib
import urllib.request

import bs4
import requests
from bing_image_downloader import downloader
from bs4 import BeautifulSoup
from PIL import Image
from search_engine_parser import GoogleSearch

from MukeshRobot import telethn as tbot
from MukeshRobot.events import register

opener = urllib.request.build_opener()
useragent = "Mozilla/5.0 (Linux; Android 11; SM-M017F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36"
opener.addheaders = [("User-agent", useragent)]


@register(pattern="^/google (.*)")
async def _(event):
    if event.fwd_from:
        return

    webevent = await event.reply("❍ sᴇᴀʀᴄʜɪɴɢ...")
    match = event.pattern_match.group(1)
    page = re.findall(r"page=\d+", match)
    try:
        page = page[0]
        page = page.replace("page=", "")
        match = match.replace("page=" + page[0], "")
    except IndexError:
        page = 1
    search_args = (str(match), int(page))
    gsearch = GoogleSearch()
    gresults = await gsearch.async_search(*search_args)
    msg = ""
    for i in range(len(gresults["links"])):
        try:
            title = gresults["titles"][i]
            link = gresults["links"][i]
            desc = gresults["descriptions"][i]
            msg += f"❍ [{title}]({link})\n❍ **{desc}**\n\n"
        except IndexError:
            break
    await webevent.edit(
        "**❍ sᴇᴀʀᴄʜ ǫᴜᴇʀʏ ➛**\n`" + match + "`\n\n**❍ ʀᴇsᴜʟᴛs ➛**\n" + msg, link_preview=False
    )


@register(pattern="^/img (.*)")
async def img_sampler(event):
    if event.fwd_from:
        return

    query = event.pattern_match.group(1)
    jit = f'"{query}"'
    downloader.download(
        jit,
        limit=4,
        output_dir="store",
        adult_filter_off=False,
        force_replace=False,
        timeout=60,
    )
    os.chdir(f'./store/"{query}"')
    types = ("*.png", "*.jpeg", "*.jpg")  # the tuple of file types
    files_grabbed = []
    for files in types:
        files_grabbed.extend(glob.glob(files))
    await tbot.send_file(event.chat_id, files_grabbed, reply_to=event.id)
    os.chdir("/app")
    os.system("rm -rf store")


opener = urllib.request.build_opener()
useragent = "Mozilla/5.0 (Linux; Android 11; SM-M017F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36"
opener.addheaders = [("User-agent", useragent)]


@register(pattern=r"^/reverse|^/pp|^/grs(?: |$)(\d*)")
async def okgoogle(img):
    """For .reverse command, Google search images and stickers."""
    if os.path.isfile("okgoogle.png"):
        os.remove("okgoogle.png")

    message = await img.get_reply_message()
    if message and message.media:
        photo = io.BytesIO()
        await tbot.download_media(message, photo)
    else:
        await img.reply("`❍ ʀᴇᴘʟʏ ᴛᴏ ᴘʜᴏᴛᴏ or sᴛɪᴄᴋᴇʀ`")
        return

    if photo:
        dev = await img.reply("`❍ ᴘʀᴏᴄᴇssɪɴɢ...`")
        try:
            image = Image.open(photo)
        except OSError:
            await dev.edit("`❍ ᴜɴsᴜᴘᴘᴏʀᴛᴇᴅ sᴇxᴜᴀʟɪᴛʏ, ᴍᴏsᴛ ʟɪᴋᴇʟʏ.`")
            return
        name = "okgoogle.png"
        image.save(name, "PNG")
        image.close()
        # https://stackoverflow.com/questions/23270175/google-reverse-image-search-using-post-request#28792943
        searchUrl = "https://www.google.com/searchbyimage/upload"
        multipart = {"encoded_image": (name, open(name, "rb")), "image_content": ""}
        response = requests.post(searchUrl, files=multipart, allow_redirects=False)
        fetchUrl = response.headers["Location"]

        if response != 400:
            await dev.edit(
                "❍ `ɪᴍᴀɢᴇ sᴜᴄᴄᴇssғᴜʟʟʏ ᴜᴘʟᴏᴀᴅᴇᴅ to ɢᴏᴏɢʟᴇ. ᴍᴀʏʙᴇ.`"
                "\n`❍ ᴘᴀʀsɪɴɢ sᴏᴜʀᴄᴇ ɴᴏᴡ. ᴍᴀʏʙᴇ.`"
            )
        else:
            await dev.edit("`❍ ɢᴏᴏɢʟᴇ ᴛᴏʟᴅ ᴍᴇ ᴛᴏ ғᴜ*ᴋ ᴏғғ.`")
            return

        os.remove(name)
        match = await ParseSauce(fetchUrl + "&preferences?hl=en&fg=1#languages")
        guess = match["best_guess"]
        imgspage = match["similar_images"]

        if guess and imgspage:
            await dev.edit(f"❍ [{guess}]({fetchUrl})\n\n`❍ ʟᴏᴏᴋɪɴɢ ғᴏʀ ᴛʜɪs ɪᴍᴀɢᴇ...`")
        else:
            await dev.edit("`❍ ᴄᴀɴ'ᴛ ғɪɴᴅ ᴛʜɪs ᴘɪᴇᴄᴇ ᴏғ sʜɪᴛ.`")
            return

        if img.pattern_match.group(1):
            lim = img.pattern_match.group(1)
        else:
            lim = 3
        images = await scam(match, lim)
        yeet = []
        for i in images:
            k = requests.get(i)
            yeet.append(k.content)
        try:
            await tbot.send_file(
                entity=await tbot.get_input_entity(img.chat_id),
                file=yeet,
                reply_to=img,
            )
        except TypeError:
            pass
        await dev.edit(
            f"❍ [{guess}]({fetchUrl})\n\n❍ [ᴠɪsᴜᴀʟʟʏ sɪᴍɪʟᴀʀ ɪᴍᴀɢᴇs]({imgspage})"
        )


async def ParseSauce(googleurl):
    """Parse/Scrape the HTML code for the info we want."""

    source = opener.open(googleurl).read()
    soup = BeautifulSoup(source, "html.parser")

    results = {"similar_images": "", "best_guess": ""}

    try:
        for similar_image in soup.findAll("input", {"class": "gLFyf"}):
            url = "https://www.google.com/search?tbm=isch&q=" + urllib.parse.quote_plus(
                similar_image.get("value")
            )
            results["similar_images"] = url
    except BaseException:
        pass

    for best_guess in soup.findAll("div", attrs={"class": "r5a77d"}):
        results["best_guess"] = best_guess.get_text()

    return results


async def scam(results, lim):

    single = opener.open(results["similar_images"]).read()
    decoded = single.decode("utf-8")

    imglinks = []
    counter = 0

    pattern = r"^,\[\"(.*[.png|.jpg|.jpeg])\",[0-9]+,[0-9]+\]$"
    oboi = re.findall(pattern, decoded, re.I | re.M)

    for imglink in oboi:
        counter += 1
        if counter < int(lim):
            imglinks.append(imglink)
        else:
            break

    return imglinks


@register(pattern="^/app (.*)")
async def apk(e):

    try:
        app_name = e.pattern_match.group(1)
        remove_space = app_name.split(" ")
        final_name = "+".join(remove_space)
        page = requests.get(
            "https://play.google.com/store/search?q=" + final_name + "&c=apps"
        )
        str(page.status_code)
        soup = bs4.BeautifulSoup(page.content, "lxml", from_encoding="utf-8")
        results = soup.findAll("div", "ZmHEEd")
        app_name = (
            results[0].findNext("div", "Vpfmgd").findNext("div", "WsMG1c nnK0zc").text
        )
        app_dev = results[0].findNext("div", "Vpfmgd").findNext("div", "KoLSrc").text
        app_dev_link = (
            "https://play.google.com"
            + results[0].findNext("div", "Vpfmgd").findNext("a", "mnKHRc")["href"]
        )
        app_rating = (
            results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "pf5lIe")
            .find("div")["aria-label"]
        )
        app_link = (
            "https://play.google.com"
            + results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "vU6FJ p63iDd")
            .a["href"]
        )
        app_icon = (
            results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "uzcko")
            .img["data-src"]
        )
        app_details = "<a href='" + app_icon + "'>📲&#8203;</a>"
        app_details += " <b>" + app_name + "</b>"
        app_details += (
            "\n\n❍ <code>ᴅᴇᴠᴇʟᴏᴘᴇʀ ➛ </code> <a href='"
            + app_dev_link
            + "'>"
            + app_dev
            + "</a>"
        )
        app_details += "\n❍ <code>ʀᴀᴛɪɴɢ ➛</code> " + app_rating.replace(
            "ʀᴀᴛᴇᴅ ", "✰ "
        ).replace(" ᴏᴜᴛ ᴏғ ", "/").replace(" sᴛᴀʀs", "", 1).replace(
            " stars", "✰ "
        ).replace(
            "five", "5"
        )
        app_details += (
            "\n❍ <code>ғᴇᴀᴛᴜʀᴇs ➛ </code> <a href='"
            + app_link
            + "'❍ >ᴠɪᴇᴡ ɪɴ ᴘʟᴀʏ sᴛᴏʀᴇ</a>"
        )
        app_details += "\n\n✦ ===> ɢʀᴏᴜᴘ ᴄᴏɴᴛʀᴏʟʟᴇʀ<=== ✦"
        await e.reply(app_details, link_preview=True, parse_mode="HTML")
    except IndexError:
        await e.reply("❍ ɴᴏ ʀᴇsᴜʟᴛ ғᴏᴜɴᴅ ɪɴ sᴇᴀʀᴄʜ. ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ **ᴠᴀʟɪᴅ ᴀᴘᴘ ɴᴀᴍᴇ**")
    except Exception as err:
        await e.reply("❍ ᴇxᴄᴇᴘᴛɪᴏɴ ᴏᴄᴄᴜʀᴇᴅ ➛ " + str(err))


__mod_name__ = "ɢᴏᴏɢʟᴇ"

__help__ = """
 ❍ /google <text>* ➛* ᴘᴇʀғᴏʀᴍ ᴀ ɢᴏᴏɢʟᴇ sᴇᴀʀᴄʜ
 ❍ /img <text>* ➛* sᴇᴀʀᴄʜ ɢᴏᴏɢʟᴇ ғᴏʀ ɪᴍᴀɢᴇs ᴀɴᴅ returns ᴛʜᴇᴍ/ғᴏʀ ɢʀᴇᴀᴛᴇʀ ɴᴏ. ᴏғ ʀᴇsᴜʟᴛs sᴘᴇᴄɪғʏ ʟɪᴍ, ғᴏʀ ᴇɢ: `/img ʜᴇʟʟᴏ lim=10`
 ❍ /app <appname>* ➛* sᴇᴀʀᴄʜᴇs ғᴏʀ ᴀɴ ᴀᴘᴘ ɪɴ ᴘʟᴀʏ sᴛᴏʀᴇ ᴀɴᴅ ʀᴇᴛᴜʀɴs ɪᴛs ᴅᴇᴛᴀɪʟs.
 ❍ /reverse |pp |grs ➛ ᴅᴏᴇs ᴀ ʀᴇᴠᴇʀsᴇ ɪᴍᴀɢᴇ sᴇᴀʀᴄʜ ᴏғ ᴛʜᴇ ᴍᴇᴅɪᴀ ᴡʜɪᴄʜ ɪᴛ ᴡᴀs ʀᴇᴘʟɪᴇᴅ ᴛᴏ.

"""
    
