from os import getenv

from pyrogram import filters
from dotenv import load_dotenv

load_dotenv()

API_ID = "28164938"
# -------------------------------------------------------------
API_HASH = "d53fd90b87686f713f6adc9428bbb6bb"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING1 = getenv("STRING_SESSION", None)
DB_NAME = "iamnobita1"
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "5536473064"))
BOT_ID = int(getenv("BOT_ID", "7943558810"))
SUPPORT_GRP = "+wPjAlUcObehiZDM1"
UPDATE_CHNL = "NOBITA_MUSIC_SUPPORT"
OWNER_USERNAME = "ll_NOBITA_DEFAULTERS_ll"
TIME_ZONE = "Asia/Kolkata"
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002344707828"))
# --------------------------------------------------------------
SUDOERS = list(map(int, getenv("SUDOERS", "5536473064").split()))
# --------------------------------------------------------------

### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()
 
# For customized or modified Repository
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Silenthrax/AI2",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
