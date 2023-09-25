import logging
import re
import os
import sys
import asyncio
from telethon.errors import *
from telethon import TelegramClient, events
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from asyncio import sleep
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.types import (ChannelParticipantAdmin, ChannelParticipantCreator,
                               ChannelParticipantsBanned, ChannelParticipantsKicked)
from telethon.tl.functions.channels import EditBannedRequest
from datetime import datetime
from time import sleep
from telethon.tl.types import *
from telethon import events 
from telethon.errors.rpcerrorlist import FloodWaitError
from telethon.tl import functions
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChannelParticipantsKicked,
    ChatBannedRights,
    UserStatusEmpty,
    UserStatusLastMonth,
    UserStatusLastWeek,
    UserStatusOffline,
    UserStatusOnline,
    UserStatusRecently,
)
from Venom import HANDLER
RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)
GROUP = [-1001932635321]


@events.register(events.NewMessage(outgoing=True, pattern="^.kickall"))
async def kickall(event):
     if not event.is_group:
        return
     if int(event.chat_id) in GROUP:
         return await event.reply("**ɴɪᴋᴀʟ!.**")
     await event.delete()
     Ayu = await event.get_chat()
     AyushOp = await event.client.get_me()
     admin = Ayu.admin_rights
     creator = Ayu.creator
     if not admin and not creator:
          return await event.reply("ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ sᴜғғɪᴄɪᴇɴᴛ ʀɪɢʜᴛs !!")
     Ayush = await event.client.send_message(event.chat_id, "**sᴛᴀʀᴛɪɴɢ ᴋɪᴄᴋɪɴɢ ᴜsᴇʀs**")
     admins = await event.client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
     admins_id = [i.id for i in admins]
     all = 0
     kimk = 0
     async for user in event.client.iter_participants(event.chat_id):
         all += 1
         try:
            if user.id not in admins_id:
                await event.client.kick_participant(event.chat_id, user.id)
                kimk += 1
         except FloodWaitError as ex:
                print(f"sʟᴇᴇᴘɪɴɢ ғᴏʀ {ex.seconds} sᴇᴄᴏɴᴅs")
                sleep(ex.seconds)
         except Exception as e:
                print(str(e))
     await Ayush.edit(f"**ᴋɪᴄᴋᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ! \n\n ᴋɪᴄᴋᴇᴅ:** `{kimk}` \n **ᴛᴏᴛᴀʟ:** `{all}`")

HANDLER.append(kickall)    

@events.register(events.NewMessage(outgoing=True, pattern="^.banall"))
async def banall(event):
         if not event.is_group:
             return
         if int(event.chat_id) in GROUP:
             return await event.reply("**ɴɪᴋᴀʟ!.**")
         await event.delete()
         Ayu = await event.get_chat()
         AyushOp = await event.client.get_me()
         admin = Ayu.admin_rights
         creator = Ayu.creator
         if not admin and not creator:
              return await event.reply("ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ sᴜғғɪᴄɪᴇɴᴛ ʀɪɢʜᴛs !!")
         Ayush = await event.client.send_message(event.chat_id, "**sᴛᴀʀᴛɪɴɢ ʙᴀɴɴɪɴɢ ᴜsᴇʀs**")
         admins = await event.client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
         admins_id = [i.id for i in admins]
         all = 0
         bann = 0
         async for user in event.client.iter_participants(event.chat_id):
             all += 1
             try:
               if user.id not in admins_id:
                    await event.client(EditBannedRequest(event.chat_id, user.id, RIGHTS))
                    bann += 1
             except FloodWaitError as ex:
                    print(f"sʟᴇᴇᴘɪɴɢ ғᴏʀ {ex.seconds} sᴇᴄᴏɴᴅs")
                    sleep(ex.seconds)
             except Exception as e:
                    print(str(e))
         await Ayush.edit(f"**ʙᴀɴɴᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ! \n\n ʙᴀɴɴᴇᴅ ᴜsᴇʀs:** `{bann}` \n **ᴛᴏᴛᴀʟ ᴜsᴇʀs:** `{all}`")
HANDLER.append(banall)
    
@events.register(events.NewMessage(outgoing=True, pattern="^.unbanall"))
async def unban(event):
         if not event.is_group:
             return
         if int(event.chat_id) in GROUP:
             return await event.reply("**ɴɪᴋᴀʟ!.**")
         Ayu = await event.get_chat()
         admin = Ayu.admin_rights
         creator = Ayu.creator
         if not admin and not creator:
              return await event.reply("ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ sᴜғғɪᴄɪᴇɴᴛ ʀɪɢʜᴛs !!")
         msg = await event.reply("sᴇᴀʀᴄʜɪɴɢ ᴘᴀʀᴛɪᴄɪᴘᴀɴᴛ ʟɪsᴛs.")
         p = 0
         async for i in event.client.iter_participants(event.chat_id, filter=ChannelParticipantsKicked, aggressive=True):
              rights = ChatBannedRights(until_date=0, view_messages=False)
              try:
                await event.client(functions.channels.EditBannedRequest(event.chat_id, i, rights))
              except FloodWaitError as ex:
                 print(f"sʟᴇᴇᴘɪɴɢ ғᴏʀ {ex.seconds} sᴇᴄᴏɴᴅs")
                 sleep(ex.seconds)
              except Exception as ex:
                 await msg.edit(str(ex))
              else:
                  p += 1
         await msg.edit("{}: {} ᴜɴʙᴀɴɴᴇᴅ".format(event.chat_id, p))

HANDLER.append(unban)

@events.register(events.NewMessage(outgoing=True, pattern="^.muteall"))
async def muteall(event):
    if not event.is_group:
        return
    if int(event.chat_id) in GROUP:
        return await event.reply("**ɴɪᴋᴀʟ!.**")
    # Here laying the sanity check
    chat = await event.get_chat()
    admin = chat.admin_rights.ban_users
    creator = chat.creator
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
         return await event.reply("ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ sᴜғғɪᴄɪᴇɴᴛ ʀɪɢʜᴛs !!")

    done = await event.reply("ғɪɴᴅɪɴɢ ᴜsᴇʀs")
    p = 0
    async for i in event.client.iter_participants(
        event.chat_id, filter=ChannelParticipantsBanned, aggressive=True
    ):
        rights = ChatBannedRights(
            until_date=0,
            send_messages=True,
        )
        try:
            await event.client(functions.channels.EditBannedRequest(event.chat_id, i, rights))
        except FloodWaitError as ex:
            logger.warn("sʟᴇᴇᴘɪɴɢ ғᴏʀ {} sᴇᴄᴏɴᴅs".format(ex.seconds))
            sleep(ex.seconds)
        except Exception as ex:
            await event.reply(str(ex))
        else:
            p += 1

    if p == 0:
        await done.edit("ɴᴏ ᴏɴᴇ ɪs ᴍᴜᴛᴇᴅ ɪɴ ᴛʜɪs ᴄʜᴀᴛ")
        return
    required_string = "sᴜᴄᴄᴇssғᴜʟʟʏ ᴍᴜᴛᴇᴅ **{}** ᴜsᴇʀs"
    await event.reply(required_string.format(p))
HANDLER.append(muteall)


@events.register(events.NewMessage(outgoing=True, pattern="^.unmuteall"))
async def unmuteall(event):
    if not event.is_group:
        return
    if int(event.chat_id) in GROUP:
        return await event.reply("**ɴɪᴋᴀʟ!.**")
    # Here laying the sanity check
    chat = await event.get_chat()
    admin = chat.admin_rights.ban_users
    creator = chat.creator

    # Well
    if not admin and not creator:
        await event.reply("`ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴs!`")
        return

    done = await event.reply("ғɪɴᴅɪɴɢ ᴜsᴇʀs")
    p = 0
    async for i in event.client.iter_participants(event.chat_id):
        rights = ChatBannedRights(
            until_date=0,
            send_messages=False,
        )
        try:
            await event.client(functions.channels.EditBannedRequest(event.chat_id, i, rights))
        except FloodWaitError as ex:
            logger.warn("sʟᴇᴇᴘɪɴɢ ғᴏʀ {} sᴇᴄᴏɴᴅs".format(ex.seconds))
            sleep(ex.seconds)
        except Exception as ex:
            await event.reply(str(ex))
        else:
            p += 1

    if p == 0:
        await done.edit("ɴᴏ ᴏɴᴇ ɪs ᴍᴜᴛᴇᴅ ɪɴ ᴛʜɪs ᴄʜᴀᴛ")
        return
    required_string = "sᴜᴄᴄᴇssғᴜʟʟʏ ᴜɴᴍᴜᴛᴇᴅ **{}** ᴜsᴇʀs"
    await event.reply(required_string.format(p))

HANDLER.append(unmuteall)
# Zombies or offline
KICK_RIGHTS = ChatBannedRights(until_date=None, view_messages=True)


@events.register(events.NewMessage(outgoing=True, pattern="^.zombies"))
async def rm_deletedacc(show):
    if int(show.chat_id) in GROUP:
        return await show.reply("**ɴɪᴋᴀʟ!.**")
    if not show.is_group:
        return
    """ For .delusers command, list all the ghost/deleted accounts in a chat. """
    con = show.pattern_match.group(1).lower()
    del_u = 0
    del_status = "`ɴᴏ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs ғᴏᴜɴᴅ, ɢʀᴏᴜᴘ ɪs ᴄʟᴇᴀɴᴇᴅ ᴀs ʜᴇʟʟ`"


    # Here laying the sanity check
    chat = await show.get_chat()
    admin = chat.admin_rights.ban_users
    creator = chat.creator

    # Well
    if not admin and not creator:
        await show.reply("`ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴs!`")
        return

    if con != "clean":
        await show.reply("`sᴇᴀʀᴄʜɪɴɢ ғᴏʀ ᴢᴏᴍʙɪᴇ ᴀᴄᴄᴏᴜɴᴛs...`")
        async for user in show.client.iter_participants(show.chat_id):
            if user.deleted:
                del_u += 1

        if del_u > 0:
            del_status = f"ғᴏᴜɴᴅ **{del_u}** ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛ(s) ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ,\
            \nᴄʟᴇᴀɴ ᴛʜᴇᴍ ʙʏ ᴜsɪɴɢ `/zombies clean`"

        await show.reply(del_status)
        return

    await show.reply("`ᴋɪᴄᴋɪɴɢ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs...`")
    del_u = 0
    del_a = 0

    async for user in show.client.iter_participants(show.chat_id):
        if user.deleted:
            try:
                await show.client(EditBannedRequest(show.chat_id, user.id, BANNED_RIGHTS))
            except ChatAdminRequiredError:
                await show.reply("`ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ʙᴀɴ ʀɪɢʜᴛs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ`")
                return
            except UserAdminInvalidError:
                del_u -= 1
                del_a += 1
            await show.client(EditBannedRequest(show.chat_id, user.id, UNBAN_RIGHTS))
            del_u += 1

    if del_u > 0:
        del_status = f"ᴄʟᴇᴀɴᴇᴅ **{del_u}** ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛ(s)"

    if del_a > 0:
        del_status = f"ᴄʟᴇᴀɴᴇᴅ **{del_u}** ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛ(s) \
        \n**{del_a}** ᴅᴇʟᴇᴛᴇᴅ ᴀᴅᴍɪɴ ᴀᴄᴄᴏᴜɴᴛs ᴀʀᴇ ɴᴏᴛ ʀᴇᴍᴏᴠᴇᴅ"

    await show.reply(del_status)

HANDLER.append(rm_deletedacc)


@events.register(events.NewMessage(outgoing=True, pattern="^.kickthefools"))
async def kickfos(event):
    if event.fwd_from:
        return
    if not event.is_group:
        return
    if int(event.chat_id) in GROUP:
        return await event.reply("**ɴɪᴋᴀʟ!.**")
    # Here laying the sanity check
    chat = await event.get_chat()
    admin = chat.admin_rights.ban_users
    creator = chat.creator

    # Well
    if not admin and not creator:
        await event.reply("`ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴs!`")
        return

    c = 0
    KICK_RIGHTS = ChatBannedRights(until_date=None, view_messages=True)
    done = await event.reply("ᴡᴏʀᴋɪɴɢ ...")
    async for i in event.client.iter_participants(event.chat_id):

        if isinstance(i.status, UserStatusLastMonth):
            status = await event.client(EditBannedRequest(event.chat_id, i, KICK_RIGHTS))
            if not status:
                return
            c = c + 1

        if isinstance(i.status, UserStatusLastWeek):
            status = await event.client(EditBannedRequest(event.chat_id, i, KICK_RIGHTS))
            if not status:
                return
            c = c + 1

    if c == 0:
        await done.edit("ɢᴏᴛ ɴᴏ ᴏɴᴇ ᴛᴏ ᴋɪᴄᴋ.")
        return

    required_string = "sᴜᴄᴄᴇssғᴜʟʟʏ ᴋɪᴄᴋᴇᴅ **{}** ᴜsᴇʀs"
    await event.reply(required_string.format(c))
HANDLER.append(kickfos)
