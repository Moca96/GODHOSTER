import os
from os import getenv

API_ID = int(os.environ.get("APP_ID", "24124040"))
API_HASH = os.environ.get("API_HASH", "5929bf41994375da3582c5e865b5c9b2")
BOT_TOKEN = "6570457592:AAG7PROkNmscilNLA3_JqxWnUF72ilDpf8Y"
SUDO_USER = list(map(int, getenv("SUDO_USER", "5842773519").split()))
