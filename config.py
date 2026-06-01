# Main configuration file

# Mandatory Variables
API_ID = "22349465" # Replace with your actual Telegram API ID
API_HASH = "3732e079c4125690226d8e7b4e028ca4"  # Replace with your actual Telegram API Hash
BOT_TOKEN = "8532135669:AAH2uizTRL59WDwZpOGLDLxFTiFy3TAxJvA"  # Replace with your actual Bot Token
OWNER_ID = "5469498838"  # Replace with your actual Owner ID
# Database
DATABASE_URL = "mongodb+srv://testweb:testweb@cluster0.dm460xd.mongodb.net/?appName=Cluster0"  # Replace with your actual database URL

AUTH_CHAT = "-1003354253974" # Replace with your actual auth chat ID. You can use multiple IDs separated by ( space ).
LOGS_CHAT = "-1001786924542" # Replace with your actual logs chat ID
POST_CHAT = "-1003354253974" # Replace with your actual post chat ID

ADMIN_USERNAME = "admin" # Replace with your admin username
ADMIN_PASSWORD = "admin@" # Replace with your admin password


SITE_SECRET = "A9F3K7X2M8Q1Z4B6" # Replace with your site secret key
TMDB_API_KEY = "0a88081143284fa351c9deec774e1438" # Replace with your TMDB API key

# Optional Variables

# If you want to use multiple bot tokens, uncomment the MULTI_TOKENS dictionary and add your tokens. this aditional bots will speed up the process of downloading and streaming files.
MULTI_TOKENS = {
    # 1: "BOT_TOKEN_1_HERE",
    # 2: "BOT_TOKEN_2_HERE",
    # Add more tokens as needed
}
DELETE_AFTER_MINUTES = 10 # Set the number of minutes after which files will be deleted from user message
POST_UPDATES = True # Set to True if you want to post updates in the post chat
USE_CAPTION = False # Set to True if you want to use captions for posts instead of file names.

# Port configuration
import os
PORT = int(os.environ.get("PORT", 6519))
















# (Don't touch this unless you know what you're doing)
SUDO_USERS = [int(x) for x in (OWNER_ID).split()]
AUTH_CHATS = [int(x) for x in (AUTH_CHAT).split()]
