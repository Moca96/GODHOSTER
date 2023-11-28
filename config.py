import os
from os import getenv

API_ID = int(os.environ.get("APP_ID", "28074580"))
API_HASH = os.environ.get("API_HASH", "902a80b6c54c4cbd58e240ee241cfcbf")
BOT_TOKEN = "6570457592:AAFVMTIwP-sDoQPfaE8ZYXWBFPWwxmOsPMQ"
SUDO_USER = list(map(int, getenv("SUDO_USER", "5842773519").split()))
