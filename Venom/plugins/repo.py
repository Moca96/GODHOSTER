from telethon import events
from Venom import HANDLER
import random
from telethon.errors.rpcerrorlist import YouBlockedUserError

import nekos
from Venom.db.blacklist_gcast_db import blacklisted_chats
msg = f"""
**⚡ ɢᴏᴅ ᴛᴇʟᴇᴛʜᴏɴ ɪs ᴘʀɪᴠᴀᴛᴇ ⚡**
  •        ɪғ ᴡᴀɴᴛ ᴛᴏ ʙᴜʏ ᴛʜɪs ʜᴏsᴛᴇʀ ʀᴇᴘᴏ ᴄᴏɴᴛᴀᴄᴛ @venom_bolti_public
  •        [ᴄʜᴀɴɴᴇʟ](https://t.me/network_zadkiel)
  •  ©️ @Zombie_area ™
"""     

neko_category = [
    'wallpaper',
    'ngif',
    'tickle',
    'feed',
    'gecg',
    'gasm',
    'slap',
    'avatar',
    'lizard',
    'waifu',
    'pat',
    '8ball',
    'kiss',
    'neko',
    'spank',
    'cuddle',
    'fox_girl',
    'hug',
    'smug',
    'goose',
    'woof',
]

async def eor(event, text):
    if event.sender_id == event.client._self_id:
        await event.edit(text)
    else:
        await event.reply(text)
eod = eor
parse_error = eor

@events.register(events.NewMessage(pattern="^.repo"))
async def repo(e):
    contacts = await blacklisted_chats(await e.client.get_peer_id('me'))
    if e.sender_id in contacts:
       await eor(e, msg)

@events.register(events.NewMessage(outgoing=True, pattern="^.nekos"))
async def neko(event):
    x = await event.get_chat()
    y = x.id
    owo = event.text[7:]
    if owo in neko_category:
        hell = await eor(event, f"`Searching {owo} ...`")
        link = nekos.img(owo)
        x = await event.client.send_file(event.chat_id, link, force_document=False)
        await hell.delete()
        if link.endswith((".gif")):
            await unsave_gif(event, x)
    elif owo == "":
        hell = await eor(event, "`Searching randoms...`")
        uwu = random.choice(neko_category)
        link = nekos.img(uwu)
        x = await event.client.send_file(event.chat_id, link, force_document=False)
        await hell.delete()
        if link.endswith((".gif")):
            await unsave_gif(event, x)
    else:
        out = ""
        for x in neko_category:
            out += f"• `{x}` \n"
        await eor(
            event,
            f"**Invalid Argument. Choose from these:**\n\n{out}",
        )


@events.register(events.NewMessage(outgoing=True, pattern="^.gcast"))
async def gcast(event):
    reply_msg = await event.get_reply_message()
    flag = str(event.text.split(" ", 2)[1])
    file = None
    if reply_msg:
        OwO = reply_msg.text
        file = reply_msg.media
    else:
        OwO = str(event.text.split(" ", 2)[2])
        file = None
    if not OwO:
        return await eor(event, "Nothing given to Gcast.")
    hell = await eor(event, "`Gcasting message...`")
    sed = 0
    owo = 0
    async for chats in event.client.iter_dialogs():
        if flag.lower() == "-all":
            chat = chats.id
            try:
                await event.client.send_message(chat, message=OwO, file=file)
                owo += 1
            except Exception as e:
                print(str(e))
                sed += 1
        elif flag.lower() == "-pvt":
            if chats.is_user and not chats.entity.bot:
                chat = chats.id
                try:
                    await event.client.send_message(chat, message=OwO, file=file)
                    owo += 1
                except Exception as e:
                    print(str(e))
                    sed += 1
        elif flag.lower() == "-grp":
            if chats.is_group:
                chat = chats.id
                try:
                    await event.client.send_message(chat, message=OwO, file=file)
                    owo += 1
                except Exception as e:
                    print(str(e))
                    sed += 1
        else:
            return await hell.edit(
                "Please give a flag to Gcast message. \n\n**Available flags are:** \n• -all : To Gcast in all chats. \n• -pvt : To Gcast in private chats. \n• -grp : To Gcast in groups."
            )
    UwU = sed + owo
    if flag.lower() == "-all":
        omk = "Chats"
    elif flag.lower() == "-pvt":
        omk = "PM"
    elif flag.lower() == "-grp":
        omk = "Groups"
        
    text_to_send = f"**📍 Sent in :** `{owo} {omk}`\n**📍 Failed in :** `{sed} {omk}`\n**📍 Total :** `{UwU} {omk}`"
    await hell.edit(f"**Gcast Executed Successfully !!** \n\n{text_to_send}")
    await event.client.send_message(Config.LOGGER_ID, f"#GCAST #{flag[1:].upper()} \n\n{text_to_send}")


@events.register(events.NewMessage(outgoing=True, pattern="^.history"))
@events.register(events.NewMessage(outgoing=True, pattern="^.sg"))
async def sg(hellevent):
    if not hellevent.reply_to_msg_id:
        await parse_error(hellevent, "No user mentioned!")
        return
    in_chat = hellevent.chat_id
    reply_message = await hellevent.get_reply_message()
    chat = "Sangmatainfo_bot"
    victim = reply_message.sender.id
    if reply_message.sender.bot:
        await eor(hellevent, "Need actual users. Not Bots")
        return
    hell = await eor(hellevent, "Checking...")
    success = False
    async with hellevent.client.conversation(chat) as conv:
        try:
            first = await conv.send_message(f"/search_id {victim}")
            try:
                response1 = await conv.get_response()
                if response1 and response1.text.startswith("🔗"):
                    success = False
                else:
                    await hellevent.client.send_message(in_chat, response1.text, reply_to=reply_message)
                    success = True
                await hellevent.client.delete_messages(conv.chat_id, [response1.id])

                response2 = await conv.get_response()
                if response2 and response2.text.startswith("🔗"):
                    success = False
                else:
                    await hellevent.client.send_message(in_chat, response2.text, reply_to=reply_message)
                    success = True
                await hellevent.client.delete_messages(conv.chat_id, [response2.id])

                response3 = await conv.get_response()
                if response3 and response3.text.startswith("🔗"):
                    success = False
                else:
                    await hellevent.client.send_message(in_chat, response3.text, reply_to=reply_message)
                    success = True
                await hellevent.client.delete_messages(conv.chat_id, [response3.id])
            except TimeoutError:
                pass
            if success == False:
                hell = await hellevent.client.send_message(in_chat, "**ERROR**", reply_to=reply_message)
                await parse_error(hell, "Unexpected Error Occured !!")
            await hellevent.client.delete_messages(conv.chat_id, [first.id])
        except YouBlockedUserError:
            return await parse_error(hell, "__Unblock @Sangmatainfo_bot and try again.__", False)

HANDLER.append(repo)
HANDLER.append(neko)
HANDLER.append(sg)
HANDLER.append(gcast)
