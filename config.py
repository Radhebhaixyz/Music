"""
from os import getenv


API_ID = int(getenv("API_ID", "20346550"))
API_HASH = getenv("API_HASH", "bc79c3bea7a626887bdc0871eecf0327")
BOT_TOKEN = getenv("BOT_TOKEN", "7358697038:AAGJBd7zlkB66QnP_4XHD3Ww17ymxIUonq8")
OWNER_ID = int(getenv("OWNER_ID", "6999625105"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6999625105 7731407856").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://daxxop:daxxop@daxxop.dg3umlc.mongodb.net/?retryWrites=true&w=majority")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002638405121"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002501818785"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS"))

