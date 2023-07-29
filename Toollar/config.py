import telethon
from telethon import TelegramClient

API_ID = 10300036
API_HASH = "79c295e05c970ddd724f0762ba275104"
bot_token = "5732856915:AAHLDpBpTFsky1vYR-8ph7G4mAJ6GF48GwI"

SUDO_USERS = "5324143657"

Sevinc = TelegramClient('Sevinc', API_ID, API_HASH).start(bot_token=bot_token)

print("Sevinc Modulu Yüklendi")