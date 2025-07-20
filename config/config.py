from os import getenv

from pyrogram import filters
from dotenv import load_dotenv

load_dotenv()

API_ID = "21134445"
# -------------------------------------------------------------
API_HASH = "231c18ea7273824491d6bf05425ab74e"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING1 = getenv("STRING_SESSION", None)
DB_NAME = "susantxbotz"
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "8156708830"))
BOT_ID = int(getenv("BOT_ID", "7303759050"))
SUPPORT_GRP = "+7WsZh7pyfxZhYmQ1"
UPDATE_CHNL = "SusantxBotz"
OWNER_USERNAME = "IM_SUSANT"
TIME_ZONE = "Asia/Kolkata"
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002267651855")
# --------------------------------------------------------------
SUDOERS = list(map(int, getenv("SUDOERS", "7968389767").split()))
# --------------------------------------------------------------

### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()
 
# For customized or modified Repository
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Silenthrax/AI2",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
