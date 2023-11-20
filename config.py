import os
from dotenv import load_dotenv

load_dotenv()

# Notion
NOTION_TOKEN = os.getenv('NOTION_TOKEN')

# Telegram
API_link = os.getenv('API_link')
BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')
debug_mode = os.getenv('DEBUG')