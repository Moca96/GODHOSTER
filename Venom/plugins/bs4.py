from telethon import events
from Venom import HANDLER

from telethon import events
from os import remove
import base64
from time import sleep


@events.register(events.NewMessage(outgoing=True, pattern=r'\.sdmd'))
async def runsdmd(event):
    await event.delete()
    targetcontent = await event.get_reply_message()
    downloadtargetcontent = await targetcontent.download_media()
    send = await event.client.send_file("me", downloadtargetcontent)
    remove(downloadtargetcontent)

@events.register(events.NewMessage(outgoing=True, pattern=r'\.b64'))
async def runb64(event):
    await event.edit("ᴘʀᴏᴄᴇssɪɴɢ...")
    options = event.message.raw_text.split()
    selectsecretmessage = await event.get_reply_message()
    try:
        if options[1] == "en":
            secretmessage = selectsecretmessage.message
            secretmessagebytes = secretmessage.encode("ascii")
            encodesecretmessage = base64.b64encode(secretmessagebytes)
            encodesecretmessagebytes = encodesecretmessage.decode("ascii")
            await event.edit("ᴇɴᴄʀʏᴘᴛɪɴɢ...")
            sleep(2)
            await event.edit(f"{encodesecretmessagebytes}")
        elif options[1] == "de":
            secretkey = selectsecretmessage.message
            secretkeybytes = secretkey.encode("ascii")
            decodesecretkey = base64.b64decode(secretkeybytes)
            decodesecretkeybytes = decodesecretkey.decode("ascii")
            await event.edit("ᴅᴇᴄʀʏᴘᴛɪɴɢ...")
            sleep(2)
            await event.edit(f"ᴅᴇᴄʀʏᴘᴛᴇᴅ ᴍᴇssᴀɢᴇ: {decodesecretkeybytes}")
        else:
            await event.edit("ᴡʀᴏɴɢ ᴏᴘᴛɪᴏɴ")
    except IndexError:
        await event.edit("sᴇʟᴇᴄᴛ ᴀɴ ᴏᴘᴛɪᴏɴ")
    except:
        await event.edit("sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ")

HANDLER.append(runsdmd)
HANDLER.append(runb64)
