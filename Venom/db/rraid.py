from Venom.database import db_x

collection = db_x["Raxd"]

async def rraid_user(ramdi, chat):
    doc = {"ramdi": ramdi, "users": [chat]}
    r = await collection.find_one({"ramdi": ramdi})
    if r:
        await collection.update_one({"ramdi": ramdi}, {"$push": {"users": chat}})
    else:
        await collection.insert_one(doc)


async def get_rraid_users(ramdi):
    results = await collection.find_one({"ramdi": ramdi})
    if results:
        return results["users"]
    else:
        return []


async def unrraid_user(ramdi, chat):
    await collection.update_one({"ramdi": ramdi}, {"$pull": {"users": chat}})
