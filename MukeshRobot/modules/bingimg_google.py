# MODULE BY https://t.me/O_okarma
# API BY https://www.github.com/SOME-1HING
# PROVIDED BY https://t.me/NovaXMod

import json

import requests
from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto, Message

# REPO => Your Bots File Name
from MukeshRobot import pbot as app


# Command handler for the '/bingimg' command
@app.on_message(filters.command("bingimg"))
def bingimg_search(client: Client, message: Message):
    try:
        text = message.text.split(None, 1)[
            1
        ]  # Extract the query from command arguments
    except IndexError:
        return message.reply_text(
            "Provide me a query to search!"
        )  # Return error if no query is provided

    search_message = message.reply_text(
        "Searching image using Bing search 🔎"
    )  # Display searching message

    # Send request to Bing image search API
    url = "https://sugoi-api.vercel.app/bingimg?keyword=" + text
    resp = requests.get(url)
    images = json.loads(resp.text)  # Parse the response JSON into a list of image URLs

    media = []
    count = 0
    for img in images:
        if count == 7:
            break

        # Create InputMediaPhoto object for each image URL
        media.append(InputMediaPhoto(media=img))
        count += 1

    # Send the media group as a reply to the user
    message.reply_media_group(media=media)

    # Delete the searching message and the original command message
    search_message.delete()
    message.delete()


# Command handler for the '/googleimg' command
@app.on_message(filters.command("googleimg"))
def googleimg_search(client: Client, message: Message):
    try:
        text = message.text.split(None, 1)[
            1
        ]  # Extract the query from command arguments
    except IndexError:
        return message.reply_text(
            "Provide me a query to search!"
        )  # Return error if no query is provided

    search_message = message.reply_text(
        "Searching image using Google search 🔎"
    )  # Display searching message

    # Send request to Google image search API
    url = "https://sugoi-api.vercel.app/googleimg?keyword=" + text
    resp = requests.get(url)
    images = json.loads(resp.text)  # Parse the response JSON into a list of image URLs

    media = []
    count = 0
    for img in images:
        if count == 7:
            break

        # Create InputMediaPhoto object for each image URL
        media.append(InputMediaPhoto(media=img))
        count += 1

    # Send the media group as a reply to the user
    message.reply_media_group(media=media)

    # Delete the searching message and the original command message
    search_message.delete()
    message.delete()
