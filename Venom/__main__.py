import asyncio
from Venom import Venom, HANDLER
import glob
from pathlib import Path
from Venom.utils import load_plugins
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.errors import AuthKeyUnregisteredError
from Venom.database import get_all_session, rmsession
from Venom.db.blacklist_gcast_db import blacklist_chat, blacklisted_chats
path = "Venom/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

async def main(): 
    print("🔥ᴄᴏɴɢʀᴀᴛs!! sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ!🎉") 
    return


if __name__ == "__main__":
    print("[ɪɴғᴏ]:💝 ᴀᴅᴅɪɴɢ ʜᴀɴᴅʟᴇʀs!🚀")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print("[ɪɴғᴏ]:🚀 sᴜᴄᴄᴇssғᴜʟʟʏ sᴛᴀʀᴛᴇᴅ ʙᴏᴛ!🇮🇳")
    Venom.run_until_disconnected()
