from Venom.database import db_x

blacklist_chatdb = db_x["BL"]

collection = blacklist_chatdb


async def blacklist_chat(ramdi, chat):
    doc = {"ramdi": ramdi, "users": [chat]}
    r = await collection.find_one({"ramdi": ramdi})
    if r:
        await collection.update_one({"ramdi": ramdi}, {"$push": {"users": chat}})
    else:
        await collection.insert_one(doc)


async def blacklisted_chats(ramdi):
    results = await collection.find_one({"ramdi": ramdi})
    if results:
        return results["users"]
    else:
        return []


async def whitelist_chat(ramdi, chat):
    await collection.update_one({"ramdi": ramdi}, {"$pull": {"users": chat}})
