from Venom import HANDLER, Venom
from telethon import TelegramClient, events, Button
from config import API_ID, API_HASH
from Venom.database import is_session_in_db, add_session
from telethon.sessions import StringSession
from telethon.tl import functions
import sys
import telethon
from telethon.errors.rpcerrorlist import UserNotParticipantError
from Venom.db.blacklist_gcast_db import blacklist_chat, blacklisted_chats
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
gandler = f"**˹ɢᴏᴅ ✘ ᴜsᴇʀʙᴏᴛ˼**\n\n"
gandler += f"━───────╯•╰───────━\n"
gandler += f"➠ **Loaded Plugin** : `ping.py`\n"
gandler += f"➠ **Loaded Plugin** : `spam.py`\n"
gandler += f"➠ **Loaded Plugin**  : `private.py`\n"
gandler += f"━───────╮•╭───────━\n\n"

@Venom.on(events.NewMessage(pattern="^[?!/]host"))
async def clone(msg):
  async with msg.client.conversation(msg.chat_id) as conv:
    await conv.send_message("Ok, Now Give Meh Your Phone Number")
    strses = await conv.get_response()
    phone_number = strses.text
    client = TelegramClient(StringSession(), API_ID, API_HASH)
    await client.connect()
    try:
        code = await client.send_code_request(phone_number)
    except ApiIdInvalidError:
        await msg.reply('`API_ID` and `API_HASH` combination is invalid. Please start generating session again.')
        return
    except PhoneNumberInvalidError:
        await msg.reply('`PHONE_NUMBER` is invalid. Please start generating session again.')
        return
    try:
        await conv.send_message("Please check for an OTP in official telegram account. If you got it, send OTP here after reading the below format. If OTP is `12345`,\nplease send it as `1 2 3 4 5`.")
        strses = await conv.get_response(timeout=600)
        phone_code_msg = strses.text
    except TimeoutError:
        await msg.reply('Time limit reached of 10 minutes. Please start generating session again.')
        return
    phone_code = phone_code_msg.replace(" ", "")
    try:
        await client.sign_in(phone_number, phone_code, password=None)
    except PhoneCodeInvalidError:
        await msg.reply('OTP is invalid. Please start hosting again.')
        return
    except PhoneCodeExpiredError:
        await msg.reply('OTP is expired. Please start hosting again.')
        return
    except SessionPasswordNeededError:
        try:
            await conv.send_message("Your account has enabled two-step verification. Please provide the password.")
            strses = await conv.get_response(timeout=300)
            two_step_msg = strses.text
        except TimeoutError:
            await msg.reply('Time limit reached of 5 minutes. Please start hosting again.')
            return
        try:
            password = two_step_msg
            await client.sign_in(password=password)
        except PasswordHashInvalidError:
            await msg.reply('Invalid Password Provided. Please start hosting again.')
            return
    phone = client.session.save()
    chat = msg.chat_id
    text = await msg.reply("Please Wait.. Starting Booting Process..")
    try:
        await text.edit("Booting Your Client")
        cli = TelegramClient(StringSession(phone), API_ID, API_HASH)
        await cli.start()
        await text.edit("Please Wait.. Loading Handlers.")
        for cmd in HANDLER:
            cli.add_event_handler(cmd)
        await cli(functions.channels.JoinChannelRequest(channel="@network_zadkiel"))
        user = await cli.get_me()
        userid = telethon.utils.get_peer_id(user)
        ok = await cli.get_peer_id('me')
        contacts = await blacklisted_chats(ok)
        if not (ok) in contacts:
           await blacklist_chat(ok, ok)
        cs = len(cli.list_event_handlers())
        await msg.reply(f"Your Client Has Been Successfully Started ✅\n\nUserid: {userid}\nUsername: @{user.username}\nName: {user.first_name}\n\nTotal Commands {cs}")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")

PM_START_TEXT = """
**Nᴏᴡ ᴍᴇ ᴛᴏ ɪɴᴛʀᴏᴅᴜᴄᴇ ᴍʏsᴇʟғ {}.
I ᴀᴍ ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟʟ sᴘᴀᴍ-ʙᴏᴛ ʜᴏꜱᴛᴇʀ ᴇᴠᴇʀ ᴍᴀᴅᴇ!
I'ᴍ ʜᴇʀᴇ ᴛᴏ ᴅᴇsᴛʀᴏʏ ʏᴏᴜʀ ᴏᴘᴘᴏɴᴇɴᴛ 🔥🔥🔥
I ᴄᴀɴ sᴘᴀᴍ ᴄᴏɴᴛɪɴᴜᴏsʟʏ ᴡɪᴛʜ ʟᴇss ғʟᴏᴏᴅ-ᴡᴀɪᴛ ᴇʀʀᴏʀ ᴀɴᴅ ᴡɪᴛʜ ᴍᴏʀᴇ ᴀᴄᴄᴜʀᴀᴄʏ!
Hᴏꜱᴛ ʏᴏᴜʀ ʙᴏᴛ ᴡɪᴛʜɪɴ ꜱᴇᴄᴏɴᴅꜱ. 🔥
ɴᴏᴛ ᴏɴʟʏ ꜱᴘᴀᴍʙᴏᴛ ɪᴛꜱ ᴀɴ ᴍɪɴɪ ᴜꜱᴇʀʙᴏᴛ**

╔═════════════════╗
║
╠═Bᴏᴛ Vᴇʀsɪᴏɴ ➪ 0.0.1
║
╠═Cʜᴀɴɴᴇʟ ➪ [»Rᴇᴅɪʀᴇᴄᴛ«](https://t.me/network_zadkiel)
║
╠═Sᴜᴘᴘᴏʀᴛ ➪ [»Rᴇᴅɪʀᴇᴄᴛ«](https://t.me/Zombie_area)
║
╠═Oᴡɴᴇʀ ➪ [»Rᴇᴅɪʀᴇᴄᴛ«](https://t.me/Zadkiel_x)
║
╚═════════════════╝

**ɢɪᴠᴇ /host ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ʜᴏꜱᴛ ʏᴏᴜʀ ᴜꜱᴇʀʙᴏᴛ**
"""

START_IMG = "https://telegra.ph/file/14f572ecd32b058af1696.jpg"

@Venom.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):
    if event.is_private:
       try:
          await event.client.get_permissions(int(-1001487945760), int(event.sender_id))
       except UserNotParticipantError:
          return
       await event.client.send_file(event.chat_id,
             START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url("🗣️ ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/Zombie_area"), Button.url("📣 ᴜᴘᴅᴀᴛᴇꜱ", "https://t.me/network_zadkiel")],
        [Button.url("ᴅᴏᴄᴜᴍᴇɴᴛᴀᴛɪᴏɴ 📃", "https://graph.org/zaidUserbot-Cmds-02-04")]])
       return
