import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7216459849:AAE6RvRrvlo7CfAMl-LecHETww6QT7KA8DU")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "23714373"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "9db8e51f22a1e87f3a1bcaf5f46f079d")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "1123687339"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://velezvelezjoan12:Iq8IYROAqIAijow0@cluster0.3wqh5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
