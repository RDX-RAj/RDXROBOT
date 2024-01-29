import requests
from MukeshRobot import telethn as tbot
from MukeshRobot.events import register

JOKES_API_URL = "https://hindijokes.apinepdev.workers.dev/"

@register(pattern="^/(joke|jokes)$")
async def fetch_joke(event):
    if event.fwd_from:
        return

    # Send "Generating a joke" message
    processing_message = await event.reply("GENERATING A JOKE FOR YOU BABY...")

    try:
        # Make a request to the Jokes API
        response = requests.get(JOKES_API_URL)

        if response.status_code == 200:
            # Extract the joke from the API response
            joke_data = response.json()
            joke = joke_data.get("hindi_Jokes", "No joke received from the API")

            # Add signature below the joke
            signature = "\n\nᴊᴏᴋᴇ ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ [𝐐𝐔𝐄𝐄𝐍](https://t.me/TheQueenRobot)"
            reply_message = f"🤣 {joke}{signature}"
        else:
            reply_message = "Error fetching joke from the API."
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        reply_message = f"Error: {str(e)}. Please try again later."
    except Exception as e:
        # Handle unexpected errors
        reply_message = f"Unexpected error: {str(e)}. Please try again later."

    # Edit the "Generating a joke" message with the final reply
    await processing_message.edit(reply_message)

__mod_name__ = "Jokes"
