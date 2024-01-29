import requests
from MukeshRobot import telethn as tbot
from MukeshRobot.events import register

YOUTUBE_API_URL = "https://ytvideo.apinepdev.workers.dev/"

@register(pattern="^/yt(?: |$)(.*)")
async def search_and_send_youtube_video(event):
    if event.fwd_from:
        return

    # Extract the YouTube video URL from the user's message
    yt_video_url = event.pattern_match.group(1).strip()

    if not yt_video_url:
        await event.reply("To download a YouTube video, use the command like this:\n\n`/yt [YouTube Video URL]`\n\nFor example: `/yt https://www.youtube.com/watch?v=example_video_id`")
        return

    # Send a "Please wait" message while processing
    processing_message = await event.reply("Please wait while fetching your video...")

    # Make a request to the YouTube Video Downloader API
    response = requests.get(f"{YOUTUBE_API_URL}?url={yt_video_url}")

    if response.status_code == 200:
        # Extract audio and video URLs from the API response
        audio_url = response.json().get("audio_url", "")
        video_url = response.json().get("video_url", "")

        # Format the reply with clickable links
        reply_message = (
            f"[𝗖𝗟𝗜𝗖𝗞 𝗛𝗘𝗥𝗘 𝗧𝗢 𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗 𝗜𝗡 𝗔𝗨𝗗𝗜𝗢 🎵]({audio_url})\n\n"
            f"[𝗖𝗟𝗜𝗖𝗞 𝗛𝗘𝗥𝗘 𝗧𝗢 𝗗𝗢𝗪𝗡𝗟𝗢𝗔𝗗 𝗜𝗡 𝗩𝗜𝗗𝗘𝗢 🎞]({video_url})\n\n\n"
            f"ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ᴠɪᴀ [𝐐𝐔𝐄𝐄𝐍](https://t.me/TheQueenRobot)"
        )

        # Edit the "Please wait" message with the final answer
        await processing_message.edit(reply_message)
    else:
        error_message = "Error fetching YouTube video from the API."

        # Edit the "Please wait" message with the error response
        await processing_message.edit(error_message)

mod_name = "YouTubeDownloader"

__help__ = """
command : `/yt` video url
"""
