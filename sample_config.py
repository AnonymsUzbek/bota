import os

class Config(object):
    # get a token from https://chatbase.com
    CHAT_BASE_TOKEN = os.environ.get("c31ef9bd-80da-4877-bb7c-2e60e75eca06", "")
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("756408643:AAF128988cK4ElVfTEgHsryEacZo--NwUQ0", "")
    # your domain to show when download file is greater than MAX_FILE_SIZE
    HTTP_DOMAIN = os.environ.get("HTTP_DOMAIN", "https://example.com/")
    # for running on Heroku.com
    PORT = int(os.environ.get('PORT', 5000))
    # The Telegram API things
    APP_ID = int(os.environ.get("732865", 12345))
    API_HASH = os.environ.get("3d0472c91f2718ab64d53a66d20af3b6")
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(str(x) for x in os.environ.get("AUTH_USERS", "").split())
    # reg: Procedures
    UTUBE_BOT_USERS = AUTH_USERS
    SUPER_DLBOT_USERS = AUTH_USERS
    SUPER3X_DLBOT_USERS = AUTH_USERS
    SUPER7X_DLBOT_USERS = AUTH_USERS
    BANNED_USERS = 7351948
    # Wat was I thinking? :\
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 1572864000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    # https://t.me/hevcbay/951
    OUO_IO_API_KEY = ""
