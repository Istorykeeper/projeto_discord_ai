import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
HISTORY_FILE = os.getenv("HISTORY_FILE")
SESSION_FILE = os.getenv("SESSION_FILE")
