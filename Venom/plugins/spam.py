import asyncio
import os
from os import execl
import sys
import requests
import time
from datetime import datetime
from telethon import events, Button
from telethon import utils
import random
hn = "."
from telethon.tl import functions
from telethon.tl.custom import button
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.contacts import GetContactsRequest
from telethon.tl.functions.messages import ImportChatInviteRequest, GetStickerSetRequest 
from telethon.tl.types import InputStickerSetID, InputStickerSetShortName
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
StartTime = time.time()
crew = [6194877007]
ALIVE_MEDIA = "https://telegra.ph/file/14f572ecd32b058af1696.jpg"
from Venom import HANDLER, SUDO_USERS
from helpmenu import spam_menu, con_menu, acc_menu, help_menu, alive_temxt, start_caption, start_caption1, devusage, sudousage, spamusage, accusage
from Utils import RAID, RRAID
from Venom.db.blacklist_gcast_db import blacklisted_chats, blacklist_chat, whitelist_chat
from Venom.db.rraid import rraid_user, get_rraid_users, unrraid_user
glad_logo = "https://telegra.ph/file/14f572ecd32b058af1696.jpg"
que = {}
buttons = [
    [
        (Button.url("Cʜᴀɴɴᴇʟ", url="https://t.me/network_zadkiel")),
        (Button.url("Sᴜᴘᴘᴏʀᴛ", url="https://t.me/Zombie_area"))
    ]
]


def TeamArsenic_time(milliseconds: int) -> str:
    """Inputs time in milliseconds, to get beautified time,
    as string"""
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    TeamArsenic_ret = (
        ((str(weeks) + "ᴡ:") if weeks else "")
        + ((str(days) + "ᴅ:") if days else "")
        + ((str(hours) + "ʜ:") if hours else "")
        + ((str(minutes) + "ᴍ:") if minutes else "")
        + ((str(seconds) + "s:") if seconds else "")
    )
    if TeamArsenic_ret.endswith(":"):
        return TeamArsenic_ret[:-1]
    else:
        return TeamArsenic_ret




async def ifgif(e, gif):
  try:
    await e.client(
      functions.messages.SaveGifRequest(
        id=types.InputDocument(
          id=sandy.media.document.id,
          access_hash=bitxh.media.document.access_hash,
          file_reference=bitxh.media.document.file_reference,
        ),
        unsave=True,
      )
    )
  except:
    pass


@events.register(events.NewMessage(pattern="^.help"))
async def bot_help(e):
    contacts = await blacklisted_chats(await e.client.get_peer_id('me'))
    if e.sender_id in contacts:
        await e.reply(help_menu)

@events.register(events.NewMessage(pattern="^.spam"))
async def spam(e):
    contacts = await blacklisted_chats(await e.client.get_peer_id('me'))
    usage = f"**🚫Wʀᴏɴɢ Usᴀɢᴇ🚫**\n\nUsᴇ: ```{hn}help spamcmds``` Tᴏ ᴋɴᴏᴡ ᴜsᴀɢᴇ ᴏғ ᴀʟʟ sᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅs."
    error = "Use .spam for range less than or equal to 100. For bigger spams use {hn}bigspam."
    if e.sender_id in contacts:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        gladbot = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(gladbot) == 2:
            message = str(gladbot[1])
            counter = int(gladbot[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            async with e.client.action(e.chat_id, "typing"):
                await asyncio.wait([e.respond(message, reply_to=e.reply_to_msg_id) for i in range(counter)])
        elif e.reply_to_msg_id and bitxh.media:  
            counter = int(gladbot[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    bitxh = await e.client.send_file(e.chat_id, bitxh, caption=bitxh.text)
                    await ifgif(e, bitxh)  
        elif e.reply_to_msg_id and bitxh.text:
            message = bitxh.text
            counter = int(gladbot[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            async with e.client.action(e.chat_id, "typing"):
                await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage)



@events.register(events.NewMessage(pattern="^.bigspam"))
async def bigspam(e):
    contacts = await blacklisted_chats(await e.client.get_peer_id('me'))
    usage = f"**🚫Wʀᴏɴɢ Usᴀɢᴇ🚫**\n\nUsᴇ: ```.help spamcmds``` Tᴏ ᴋɴᴏᴡ ᴜsᴀɢᴇ ᴏғ ᴀʟʟ sᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅs."
    if e.sender_id in contacts:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        gladbot = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(gladbot) == 2:
            msg = str(gladbot[1])
            counter = int(gladbot[0])
            for i in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.respond(msg, reply_to=e.reply_to_msg_id)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and bitxh.media:  
            counter = int(gladbot[0])
            for i in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    bitxh = await e.client.send_file(e.chat_id, bitxh, caption=bitxh.text)
                    await ifgif(e, bitxh) 
                await asyncio.sleep(0.3)  
        elif e.reply_to_msg_id and bitxh.text:
            message = bitxh.text
            counter = int(gladbot[0])
            for i in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    try:
                        await e.client.send_message(e.chat_id, message)
                    except:
                        pass
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage)

@events.register(events.NewMessage(pattern="^.uspam"))
async def uspam(e):
    contacts = await blacklisted_chats(await e.client.get_peer_id('me'))
    usage = f"**🚫Wʀᴏɴɢ Usᴀɢᴇ🚫**\n\nUsᴇ: ```.help spamcmds``` Tᴏ ᴋɴᴏᴡ ᴜsᴀɢᴇ ᴏғ ᴀʟʟ sᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅs."
    if e.sender_id in contacts:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        gladbot = e.text.split(" ", 1)
        bitxh = await e.get_reply_message()
        x = 0
        if len(gladbot) == 2:
            msg = str(gladbot[1])
            while x == 0:
                async with e.client.action(e.chat_id, "typing"):
                    await e.respond(msg, reply_to=e.reply_to_msg_id)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and bitxh.media:  
            while x == 0:
                async with e.client.action(e.chat_id, "document"):
                    bitxh = await e.client.send_file(e.chat_id, bitxh, caption=bitxh.text)
                    await ifgif(e, bitxh) 
                await asyncio.sleep(0.3)  
        elif e.reply_to_msg_id and bitxh.text:
            message = bitxh.text
            while x == 0:
                async with e.client.action(e.chat_id, "typing"):
                    try:
                        await e.client.send_message(e.chat_id, message)
                    except:
                        pass
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage)


@events.register(events.NewMessage(pattern="^.packspam"))
async def packspam(e):
    contacts = await blacklisted_chats(await e.client.get_peer_id('me'))
    if e.sender_id in contacts:
        try:
            x = await e.get_reply_message()
            if not (x and x.media and hasattr(x.media, "document")):
                return await e.reply("`Reply To Sticker Only.`")
            set = x.document.attributes[1]
            sset = await e.client(
                GetStickerSetRequest(
                InputStickerSetID(
                    id=set.stickerset.id,
                    access_hash=set.stickerset.access_hash,
                )
                )
            )
            pack = sset.set.short_name
            docs = [
                utils.get_input_document(x)
                for x in (
                await e.client(GetStickerSetRequest(InputStickerSetShortName(pack)))
                ).documents
            ]
            for xx in docs:
                async with e.client.action(e.chat_id, "document"):
                    await e.client.send_file(e.chat_id, file=(xx))
                    await asyncio.sleep(0.3)
        except Exception as xy:
            print(str(xy))
            await e.reply(f"**🚫Wʀᴏɴɢ Usᴀɢᴇ🚫**\n\nUsᴇ: ```.help spamcmds``` Tᴏ ᴋɴᴏᴡ ᴜsᴀɢᴇ ᴏғ ᴀʟʟ sᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅs.")

@events.register(events.NewMessage(pattern="^.dspam"))
async def dspam(e):
    contacts = await blacklisted_chats(await e.client.get_peer_id('me'))
    usage = f"**🚫Wʀᴏɴɢ Usᴀɢᴇ🚫**\n\nUsᴇ: ```.help spamcmds``` Tᴏ ᴋɴᴏᴡ ᴜsᴀɢᴇ ᴏғ ᴀʟʟ sᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅs."
    if e.sender_id in contacts:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        bitxh = await e.get_reply_message()
        gladbot = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        gladbotisop = gladbot[1:]
        if len(gladbotisop) == 2:
            message = str(gladbotisop[1])
            counter = int(gladbotisop[0])
            sleeptime = float(gladbot[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await bitxh.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and bitxh.media:  
            counter = int(gladbotisop[0])
            sleeptime = float(gladbot[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    bitxh = await e.client.send_file(e.chat_id, bitxh, caption=bitxh.text)
                    await ifgif(e, bitxh) 
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and bitxh.text:
            message = bitxh.text
            counter = int(gladbotisop[0])
            sleeptime = float(gladbot[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

@events.register(events.NewMessage(pattern="^.hang"))
async def hang(e):
    contacts = await blacklisted_chats(await e.client.get_peer_id('me'))
    usage = f"**🚫Wʀᴏɴɢ Usᴀɢᴇ🚫**\n\nUsᴇ: ```{hn}help spamcmds``` Tᴏ ᴋɴᴏᴡ ᴜsᴀɢᴇ ᴏғ ᴀʟʟ sᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅs."
    if e.sender_id in contacts:
        gladbot = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(gladbot) == 1:
            counter = int(gladbot[0])
            hangmsg = f"😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟"
            await asyncio.wait([e.respond(hangmsg, reply_to=e.reply_to_msg_id) for i in range(counter)])
        else:
            await e.reply(usage)

@events.register(events.NewMessage(pattern="^.ping"))
async def gtping(e):
  contacts = await blacklisted_chats(await e.client.get_peer_id('me'))
  if e.sender_id in contacts:
        if e.reply_to_msg_id:
            v = await e.respond("Pᴏɴɢ!", reply_to=e.reply_to_msg_id)
        else:
            v = await e.reply("Pᴏɴɢ!")
        ping_start = datetime.now()
        ping_end = datetime.now()
        ms = (ping_end-ping_start).microseconds / 1000
        uptime = TeamArsenic_time((time.time() - StartTime) * 1000)
        ping_msg = f"•• Pᴏɴɢ . ••\n⏱ Pɪɴɢ sᴘᴇᴇᴅ : {ms}ᴍs\n⏳ Uᴘᴛɪᴍᴇ - {uptime}"
        await v.edit(ping_msg)

@events.register(events.NewMessage(pattern="^.alive"))
async def alive(e):
    contacts = await blacklisted_chats(await e.client.get_peer_id('me'))
    if e.sender_id in contacts:
        try:
            await e.client.send_file(e.chat_id, ALIVE_MEDIA, caption = alive_temxt, reply_to=e.message.id, link_preview=None)
        except:
            await e.reply(alive_temxt, link_preview=None)

@events.register(events.NewMessage(pattern="^.leave"))
async def leave(e):
    contacts = await blacklisted_chats(await e.client.get_peer_id('me'))
    if e.sender_id in contacts:
        chamt = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            chamt_id = int(chamt[0])
            await e.reply("*Moves to door...*")
            try:
                await e.client(LeaveChannelRequest(chamt_id))
                await e.edit("*Silently left...*")
            except Exception as eror:
                await e.edit(str(eror))
        else:
            chamt_id = e.chat_id
            await e.reply("*Moves to door...*")
            try:
                await e.client(LeaveChannelRequest(chamt_id))
                await e.edit("*Silently left!*")
            except Exception as eror:
                await e.edit(str(eror))

@events.register(events.NewMessage(pattern="^.bio"))
async def bio(e):
    contacts = await blacklisted_chats(await e.client.get_peer_id('me'))
    usage = f"**🚫Wʀᴏɴɢ Usᴀɢᴇ🚫**\n\nUsᴇ: ```.help profile``` Tᴏ ᴋɴᴏᴡ ᴜsᴀɢᴇ ᴏғ ᴀʟʟ ᴀᴄᴄᴏᴜɴᴛ ᴄᴏᴍᴍᴀɴᴅs."
    if e.sender_id in contacts:
        chckpnt = e.text.split(" ", 1)
        message = chckpnt[1]
        if len(e.text) > 5:
            bio = message
            text = "Changing Bio..."
            try:
                await e.client(functions.account.UpdateProfileRequest(about=bio))
                event = await e.reply(text, parse_mode=None, link_preview=None )
                await asyncio.sleep(0.7)
                await event.edit("Changed bio successfully!")
            except Exception as e:
                await print(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

@events.register(events.NewMessage(pattern="^.name"))
async def name(e):
    contacts = await blacklisted_chats(await e.client.get_peer_id('me'))
    usage = f"**🚫Wʀᴏɴɢ Usᴀɢᴇ🚫**\n\nUsᴇ: ```.help profile``` Tᴏ ᴋɴᴏᴡ ᴜsᴀɢᴇ ᴏғ ᴀʟʟ ᴀᴄᴄᴏᴜɴᴛ ᴄᴏᴍᴍᴀɴᴅs."
    if e.sender_id in contacts:
        chckpnt = e.text.split(" ", 1)
        message = chckpnt[1]
        if len(e.text) > 5:
            bio = message
            text = "Changing Name..."
            try:
                await e.client(functions.account.UpdateProfileRequest(first_name=bio))
                event = await e.reply(text, parse_mode=None, link_preview=None )
                await asyncio.sleep(0.7)
                await event.edit("Changed name successfully!")
            except Exception as e:
                await print(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@events.register(events.NewMessage(pattern="^.profilepic"))
async def pprofile(event):
    contacts = await blacklisted_chats(await e.client.get_peer_id('me'))
    if e.sender_id in contacts:
        try:
            glad = await event.get_reply_message()
            try:
                media = await glad.download_media( "spammerbots/downloads/")
            except:
                pass
            await client(UploadProfilePhotoRequest(
                await client.upload_file(media)
            ))
            await event.reply("**Changed profile picture successfully!!**")
            try:
                os.remove(media)
            except Excepion as e:
                print(str(e))
        except:
            pass

@events.register(events.NewMessage(pattern="^.join"))
async def join(e):
    contacts = await blacklisted_chats(await e.client.get_peer_id('me'))
    if e.sender_id in contacts:
        dattext = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            chash = dattext[0]
            text = "Roger that...\nI'm on it."
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=chash))
                event = await e.reply(text, parse_mode=None, link_preview=None )
                await asyncio.sleep(0.7)
                await event.edit("Joined the chat successfully\nOver!")
            except Exception as e:
                await print(str(e))   
        else:
            await e.reply(accusage, parse_mode=None, link_preview=None )




@events.register(events.NewMessage(pattern="^.pjoin"))
async def pjoin(e):
    contacts = await blacklisted_chats(await e.client.get_peer_id('me'))
    if e.sender_id in contacts:
        dattext = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            chash = dattext[0]
            text = "Roger that...\nI'm on it."
            try:
                await e.client(ImportChatInviteRequest(chash))
                event = await e.reply(text, parse_mode=None, link_preview=None )
                await asyncio.sleep(0.7)
                await event.edit("Joined the chat successfully\nOver!")
            except Exception as e:
                await print(str(e))   
        else:
            await e.reply(accusage, parse_mode=None, link_preview=None )

@events.register(events.NewMessage(pattern="^.restart"))
async def restart(e):
    contacts = await blacklisted_chats(await e.client.get_peer_id('me'))
    if e.sender_id in contacts:
        reboot_text = """
Rᴇʙᴏᴏᴛɪɴɢ ʙᴏᴛ...

Wᴀɪᴛ ғᴏʀ ᴀ ᴡʜɪʟᴇ ᴛᴏ ᴜsᴇ ɪᴛ ᴀɢᴀɪɴ.
        """
        await e.reply(reboot_text)
        try:
            e.client.disconnect()
        except Exception as e:
            pass
        try:
            e.client.connect()
        except Exception as e:
            pass


@events.register(events.NewMessage(pattern="^.raid"))
async def raid(e):
    contacts = await blacklisted_chats(await e.client.get_peer_id('me'))
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in contacts:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            if g in crew:
                await e.reply("Baap Se Masti Nhi")
            username = f"[{c}](tg://user?id={g})"
            counter = int(yukki[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if g in crew:
                await e.reply("Baap Se Masti Nhi")
            c = b.first_name
            counter = int(yukki[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@events.register(events.NewMessage(incoming=True))
async def check(event):
    queue = await get_rraid_users(await event.client.get_peer_id('me'))
    if event.sender_id in queue:
      async with event.client.action(event.chat_id, "typing"):
          await asyncio.sleep(0.3)
      async with event.client.action(event.chat_id, "typing"):
          await event.client.send_message(
              entity=event.chat_id,
              message="""{}""".format(random.choice(RRAID)),
              reply_to=event.message.id,
          ) 

@events.register(events.NewMessage(outgoing=True, pattern="^.sudolist"))
async def addsudo(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = Add Sudo\n\nCommand:\n\n.addsudo <Username of User>\n\n.addsudo <reply to a User>"
    if e.sender_id:
        list = await blacklisted_chats(e.sender_id)
        text = f"Successfully Added\n\n {list}"
        await e.reply(text, parse_mode=None, link_preview=None )

@events.register(events.NewMessage(outgoing=True, pattern="^.addsudo"))
async def addsudo(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = Add Sudo\n\nCommand:\n\n.addsudo <Username of User>\n\n.addsudo <reply to a User>"
    if e.sender_id:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(yukki[0])
            a = await e.client.get_entity(message)
            g = a.id
            if g in (await blacklisted_chats(e.sender_id)):
                await e.reply("This User already in Sudo")
                return
            await blacklist_chat(e.sender_id, g)
            text = "Successfully Added"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if g in (await blacklisted_chats(e.sender_id)):
                await e.reply("This User already in Sudo")
                return
            text = "Successfully Added"
            await blacklist_chat(e.sender_id, g)
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@events.register(events.NewMessage(outgoing=True, pattern="^.rmsudo"))
async def rmsudo(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = Remove Sudo\n\nCommand:\n\n.rmsudo <Username of User>\n\n.rmsudo <reply to a User>"
    if e.sender_id:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(yukki[0])
            a = await e.client.get_entity(message)
            g = a.id
            if g in (await blacklisted_chats(e.sender_id)):
                await whitelist_chat(e.sender_id, g)
                text = "Successfully Removed"
                await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if g in (await blacklisted_chats(e.sender_id)):
                await whitelist_chat(e.sender_id, g)
                text = "Successfully Removed"
                await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

            
          
            
@events.register(events.NewMessage(pattern="^.replyraid"))
async def replyraid(e):
    contacts = await blacklisted_chats(await e.client.get_peer_id('me'))
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.replyraid <Username of User>\n\n.replyraid <reply to a User>"
    if e.sender_id in contacts:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(yukki[0])
            a = await e.client.get_entity(message)
            g = a.id
            if g in crew:
                await e.reply("Baap Se Masti Nhi")
                return
            if g in (await get_rraid_users(await e.client.get_peer_id('me'))):
                await e.reply("Already Active")
                return
            await rraid_user(await e.client.get_peer_id('me'), g)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if g in crew:
                await e.reply("Baap Se Masti Nhi")
                return
            if g in (await get_rraid_users(await e.client.get_peer_id('me'))):
                await e.reply("Already Active")
                return
            await rraid_user(await e.client.get_peer_id('me'), g)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

            
@events.register(events.NewMessage(pattern="^.dreplyraid"))
async def dreplyraid(e):
    contacts = await blacklisted_chats(await e.client.get_peer_id('me'))
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
    if e.sender_id in contacts:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(yukki[0])
            a = await e.client.get_entity(message)
            g = a.id
            if g in crew:
                await e.reply("Baap Se Masti Nhi")
                return
            if not g in (await get_rraid_users(await e.client.get_peer_id('me'))):
                await e.reply("User Already in His Aukaat")
                return 
            await unrraid_user(await e.client.get_peer_id('me'), g)
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if g in crew:
                await e.reply("Baap Se Masti Nhi")
                return
            if not g in (await get_rraid_users(await e.client.get_peer_id('me'))):
                await e.reply("User Already in His Aukaat")
                return
            await unrraid_user(await e.client.get_peer_id('me'), g)
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

HANDLER.append(bot_help)
HANDLER.append(spam)
HANDLER.append(bigspam)
HANDLER.append(uspam)
HANDLER.append(dspam)
HANDLER.append(hang)
HANDLER.append(alive)
HANDLER.append(gtping)
HANDLER.append(leave)
HANDLER.append(name)
HANDLER.append(bio)
HANDLER.append(pprofile)
HANDLER.append(pjoin)
HANDLER.append(join)
HANDLER.append(raid)
HANDLER.append(check)
HANDLER.append(restart)
HANDLER.append(replyraid)
HANDLER.append(dreplyraid)
HANDLER.append(addsudo)
HANDLER.append(rmsudo)
