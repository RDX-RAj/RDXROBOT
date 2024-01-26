import requests
from MukeshRobot import telethn as tbot
from MukeshRobot.events import register

INSTAGRAM_API_URL = "https://instagramdownloader.apinepdev.workers.dev/"

@register(pattern="^/insta(?: |$)(.*)")
async def search_and_send_instagram_video(event):
    if event.fwd_from:
        return

    # Extract the Instagram video URL from the user's message
    insta_video_url = event.pattern_match.group(1).strip()

    if not insta_video_url:
        await event.reply("Please provide a valid Instagram video URL.")
        return

    # Send "Please wait" message
    processing_message = await event.reply("Please wait while fetching your download...")

    try:
        # Make a request to the Instagram Video Downloader API
        response = requests.get(f"{INSTAGRAM_API_URL}?url={insta_video_url}")

        if response.status_code == 200:
            # Downloaded Instagram video URL
            video_url = response.json().get("data")[0].get("url", "No video received from the API")

            # Format the reply with a clickable link
            reply_message = f"✦ ʏᴏᴜʀ ɪɴsᴛᴀ ʀᴇᴇʟs ɪs ʀᴇᴀᴅʏ ʙᴀʙʏ.\n\n✦ [ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ]({video_url})\n\n❍ ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ᴠɪᴀ ➠ [๛ᴀ ᴠ ɪ s ʜ ᴀ ༗](https://t.me/AvishaxBot)"
        else:
            reply_message = "Error fetching Instagram video from the API."
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        reply_message = f"Error: {str(e)}. Please try again later."
    except Exception as e:
        # Handle unexpected errors
        reply_message = f"Unexpected error: {str(e)}. Please try again later."

    # Edit the "Please wait" message with the final reply
    await processing_message.edit(reply_message)

__mod_name__ = "ɪɴsᴛᴀ"

__help__ = "❍ use : /ɪɴsᴛᴀ ᴠɪᴅᴇᴏ / ʀᴇᴇʟ ʟɪɴᴋ"
