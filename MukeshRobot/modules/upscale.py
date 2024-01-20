#CREATED BY @o_OKarma
#API CREDITS: @Qewertyy
#PROVIDED BY https://github.com/Team-ProjectCodeX

#IMPORTS
import httpx, base64
from pyrogram import filters , Client

#BOT FILE IMPORTS
#Name -> Your Bots File Name (Eg. From Liaa import pbot as app)
from Itachi import app


@Client.on_message(filters.command("upscale"))
async def upscale_image(client, message):
    try:
        # Check if the replied message contains a photo
        if message.reply_to_message and message.reply_to_message.photo:
            # Send a message indicating upscaling is in progress
            progress_msg = await message.reply_text(
                "**Upscaling your image, please wait...**"
            )

            # Access the image file_id from the replied message
            image = message.reply_to_message.photo.file_id
            file_path = await client.download_media(image)

            with open(file_path, "rb") as image_file:
                f = image_file.read()

            b = base64.b64encode(f).decode("utf-8")

            async with httpx.AsyncClient() as http_client:
                response = await http_client.post(
                    "https://api.qewertyy.me/upscale",
                    data={"image_data": b},
                    timeout=None,
                )

            # Save the upscaled image
            upscaled_file_path = "upscaled_image.png"
            with open(upscaled_file_path, "wb") as output_file:
                output_file.write(response.content)

            # Delete the progress message
            await progress_msg.delete()

            # Send the upscaled image as a PNG file
            await client.send_document(
                message.chat.id,
                document=upscaled_file_path
            )
        else:
            await message.reply_text("**Please reply to an image to upscale it.**")

    except Exception as e:
        print(f"**Failed to upscale the image**: {e}")
        await message.reply_text("**Failed to upscale the image. Please try again later.**")
        # You may want to handle the error more gracefully here