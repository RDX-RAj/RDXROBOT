import requests
from RDXROBOT import telethn as tbot
from RDXROBOT.events import register

YOUTUBE_API_URL = "https://ytvideo.apinepdev.workers.dev/"

@register(pattern="^/yt(?: |$)(.*)")
async def search_and_send_youtube_video(event):
    if event.fwd_from:
        return

    # Extract the YouTube video URL from the user's message
    yt_video_url = event.pattern_match.group(1).strip()

    if not yt_video_url:
        await event.reply("๏ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴀ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ, ᴜsᴇ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ ʟɪᴋᴇ ᴛʜɪs.\n\n๏ `/yt [ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ᴜʀʟ]`\n\n๏ ғᴏʀ ᴇxᴀᴍᴘʟᴇ : `/yt https://www.youtube.com/watch?v=example_video_id`")
        return

    # Send a "Please wait" message while processing
    processing_message = await event.reply("🧨")

    # Make a request to the YouTube Video Downloader API
    response = requests.get(f"{YOUTUBE_API_URL}?url={yt_video_url}")

    if response.status_code == 200:
        # Extract audio and video URLs from the API response
        audio_url = response.json().get("audio_url", "")
        video_url = response.json().get("video_url", "")

        # Format the reply with clickable links
        reply_message = (
            f"๏ ʜᴇʀᴇ ɪs ʏᴏᴜʀ ʏᴛ-ǫᴜᴇʀʏ ɪɴ ᴀᴜᴅɪᴏ ➠ [ᴅᴏᴡɴʟᴏᴀᴅ ɴᴏᴡ]({audio_url})\n\n"
            f"๏ ʜᴇʀᴇ ɪs ʏᴏᴜʀ ʏᴛ-ǫᴜᴇʀʏ ɪɴ ᴠɪᴅᴇᴏ ➠ [ᴅᴏᴡɴʟᴏᴀᴅ ɴᴏᴡ]({video_url})\n\n\n"
            f"๏ ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ᴠɪᴀ ➠ [๛ᴀ  ʟ  ᴇ  x  ᴀ ༗](https://t.me/alexarobot)"
        )

        # Edit the "Please wait" message with the final answer
        await processing_message.edit(reply_message)
    else:
        error_message = "๏ ᴇʀʀᴏʀ ғᴇᴛᴄʜɪɴɢ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ғʀᴏᴍ ᴛʜᴇ ᴀᴘɪ."

        # Edit the "Please wait" message with the error response
        await processing_message.edit(error_message)

mod_name = "ʏᴛ-ᴅʟ"

