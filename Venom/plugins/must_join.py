from telethon.errors.rpcerrorlist import UserNotParticipantError
from Venom import Venom 
from telethon import TelegramClient, events, Button
MUST_JOIN = "network_zadkiel"

@Venom.on(events.NewMessage(incoming=True))
async def must_join_channel(event):
    if not MUST_JOIN:  # Not compulsory
        return
    try:
        try:
            await event.client.get_permissions(int(-1001487945760), int(event.sender_id))
        except UserNotParticipantError:
            link = "https://t.me/" + MUST_JOIN
            try:
                await event.reply(f"You must join [this channel]({link}) to use me. After joining try again !", buttons=[[Button.url("🔥 Join Channel ✨", url=f"{link}")]])
                return
            except Exception:
                pass
    except Exception:
        print(f"I'm not admin in the MUST_JOIN chat : {MUST_JOIN} !")
