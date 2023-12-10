# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6020240248:AAG35b4X1-43zPmkOIgB7p6DzSX85sqIl9o")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "7414019"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "d463ed3d695f5cd4164029405ad8388e")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001826832437"))

#NAME OF THE OWNER
OWNER = os.environ.get("OWNER", "KaRma_Xz")

# Protect Content
PROTECT_CONTENT = strtobool(os.environ.get("PROTECT_CONTENT", "False"))

# Heroku Credentials for updater.
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", "")
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")

# Custom Repo for updater.
UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", "master")

# Database
DB_URI = os.environ.get("DB_URI", "")

# ID of the Channel or Group for which you must subscribe
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001270386911"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1001942518325"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "Hello {first}\n\nI'm here to help! I keep private files in a special channel and share links so others can access them effortlessly.",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")
ADMINS.extend(1350488685)

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hold on, {first}!\n\nYou're missing out on some serious action.\n\nTo unleash my full power and access all the files, you've got to join both of our electrifying channels below:</b>",
)

# Set Your Custom Text here, Save (None) to Disable Custom Text
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Set True if you want to Disable the Share Your Channel Posts button
DISABLE_CHANNEL_BUTTON = strtobool(os.environ.get("DISABLE_CHANNEL_BUTTON", "True"))

LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
