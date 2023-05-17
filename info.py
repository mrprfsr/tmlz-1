import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', 21818317))
API_HASH = environ.get('API_HASH', 'bc6ab154300cc41fe127ca4d658dc75d')
BOT_TOKEN = environ.get('BOT_TOKEN', '5329268513:AAGfnPBjpIbxqAqulOgXTyME_zNwJ-71k9k')
# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://graph.org/file/1ff163ad22f8b9dd4b2b4.jpg https://graph.org/file/5a35d2371dbe5b9067ce5.jpg https://graph.org/file/5f0812e5de29bbb0f335e.jpg https://graph.org/file/da0aa976fc4f6e7c1e3d1.jpg https://graph.org/file/213d1ba3604ae15926ff8.jpg https://graph.org/file/1640c62b3a1ea05c74855.jpg https://graph.org/file/2ee648ec64cfb17f385f3.jpg https://graph.org/file/0d4bdb3a789388ec79f8d.jpg https://graph.org/file/b730f1b51690a5ad6d210.jpg https://graph.org/file/c76d09ed2567a09832162.jpg https://graph.org/file/f5fda371f75961fc4f55f.jpg https://graph.org/file/c1841a9727eae32933eb8.jpg https://graph.org/file/01985d5ddd0af3801fb2d.jpg https://graph.org/file/e7f26539726494f95ae60.jpg https://graph.org/file/ef7cfd68e88242fa8bdd5.jpg https://graph.org/file/3f1e9bd96cb7470c56411.jpg https://graph.org/file/80218bb4714853738edae.jpg https://graph.org/file/97d9bb14f449d07888a16.jpg https://graph.org/file/5e9efb6a39d4b7cd3d9ce.jpg https://graph.org/file/58fc75d36b89a2842ef5f.jpg https://graph.org/file/dc9345074429391bdce7e.jpg https://graph.org/file/137156bd5c2aa3cfdbb02.jpg https://graph.org/file/44d17769d7cdcf61f29f0.jpg https://graph.org/file/4f2dc6494c259a8d4f172.jpg https://graph.org/file/168ceddd3c6d790a8d8e1.jpg')).split()# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5650200786 5681376068').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://cat:cat@cluster0.qptrdyv.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1001594651224))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Mx_Support_Bot')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<b>{file_name}</i>\n\n<b>🍿 Ꭾօաɛʀɛɖ Ɓꪗ: @iPopkarn</b>")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "False"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

UPSTREAM_REPO = environ.get('UPSTREAM_REPO', 'https://github.com/TamilanBotsZ/AwesomeFilterPro')

AUTO_DELETE_SECONDS = int(environ.get('AUTO_DELETE_SECONDS', 500))
AUTO_DELETE = environ.get('AUTO_DELETE', True)
if AUTO_DELETE == "True":
    AUTO_DELETE = True

#Sample
SHORTNER_SITE = "Teraboxshortner.com"
SHORTNER_API = "ce3983adff187917b6c147cd7f9ed77214580a0b"

