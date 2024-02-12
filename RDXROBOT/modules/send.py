"""
STATUS: Code is working. ✅
"""

"""
BSD 2-Clause License

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from RDXROBOT import dispatcher
from RDXROBOT.modules.disable import DisableAbleCommandHandler

from RDXROBOT.modules.helper_funcs.alternate import send_message


def send(update, context):
	args = update.effective_message.text.split(None, 1)
	creply = args[1]
	send_message(update.effective_message, creply)

__help__ = """❍ ᴛʜᴇ sᴇɴᴅ ᴍᴏᴅᴜʟᴇ ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ sᴇɴᴅ ᴀ ᴄᴜsᴛᴏᴍ ᴍᴇssᴀɢᴇ ᴛᴏ ᴜsᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ.

❍ `/snd` ➛ sᴇɴᴅ ᴛʜᴇ ɢɪᴠᴇɴ ᴍᴇssᴀɢᴇ

❍ ɴᴏᴛᴇ ➛ /snd ʜɪ ᴡɪʟʟ sᴇɴᴅ ᴛʜᴇ ᴍᴇssᴀɢᴇ ʜɪ ᴛᴏ ᴛʜᴇ ᴄʜᴀᴛ"""

__mod_name__ = "sᴇɴᴅ"


ADD_CCHAT_HANDLER = DisableAbleCommandHandler("snd", send, run_async = True)
dispatcher.add_handler(ADD_CCHAT_HANDLER)
__command_list__ = ["snd"]
__handlers__ = [
    ADD_CCHAT_HANDLER
]
