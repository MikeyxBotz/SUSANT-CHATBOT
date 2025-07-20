import random
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli

CHAT_STORAGE = [
    "mongodb+srv://susantxbotz:vGmf4pFy1MEijuZF@cluster0.viyjnvi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
   
]

BADMUNDA = MongoCli(random.choice(CHAT_STORAGE))
chatdb = BADMUNDA.Anonymous
chatai = chatdb.Word.WordDb
storeai = BADMUNDA.Anonymous.Word.NewWordDb  
