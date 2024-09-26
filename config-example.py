from hydrogram import Client

games = {}
player_game = {}

timeout = 120
minimum_players = 2

sudoers = [7242000752]

API_ID = "3939406"
API_HASH = "e11d0eaec136b1047974ab098041e9f2"

# --- Telegram config ---
BOT_TOKEN = "7504787456:AAFzHc2CcmFIUTla6AIjdJAu2nJZCkfIUHI"

bot = Client("bot", api_id=API_ID, api_hash=API_HASH, plugins={"root": "unu.plugins"})
