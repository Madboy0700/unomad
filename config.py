from hydrogram import Client

games = {}
player_game = {}

timeout = 120
minimum_players = 2

sudoers = [5901320319]

API_ID = "28121536"
API_HASH = "57d552d05f2a76244291d9eb330294c2"

# --- Telegram config ---
BOT_TOKEN = "8030899275:AAGZQlpJqth6cc37FWrustudh5OGyBftA64"

bot = Client("bot", api_id=API_ID, api_hash=API_HASH, plugins={"root": "unu.plugins"})
