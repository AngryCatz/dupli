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
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6316649627:AAFw3R--P-KL1_fYsHr7jgWJuTLyuuqcvwY")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "12125809"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "ce73c56d4350826a1ea536f147645ef7")

    # Authorized users to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1975881439").split())

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
