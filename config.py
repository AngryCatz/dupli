import os
import logging


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6316uqcvwY")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "129"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "ce73cf7")

    # Authorized users to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1939").split())

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "APSe4ck_3SnPkgaij

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
