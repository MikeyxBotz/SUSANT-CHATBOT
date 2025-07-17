import random
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli

CHAT_STORAGE = [
    "",
]

BADMUNDA = MongoCli(random.choice(CHAT_STORAGE))
chatdb = BADMUNDA.Anonymous
chatai = chatdb.Word.WordDb
storeai = BADMUNDA.Anonymous.Word.NewWordDb  
