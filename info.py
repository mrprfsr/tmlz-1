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
API_ID = int(environ.get('API_ID', '21818317'))
API_HASH = environ.get('API_HASH', 'bc6ab154300cc41fe127ca4d658dc75d')
BOT_TOKEN = environ.get('BOT_TOKEN', '5407827904:AAGrFnYi78l-Pu3rDm-wpRFeaZB4czzKb4c')
# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS', 'https://telegra.ph/file/35a68f3cd477a6776e089.jpg https://telegra.ph/file/0d6568ea04e079ad7e6bf.jpg https://telegra.ph/file/f9e1e7b34cbd8baff7b10.jpg https://telegra.ph/file/b582f7311d72ed3e60075.jpg https://telegra.ph/file/ad5e8b295f4c69891cd17.jpg https://telegra.ph/file/9014ba7fe89a4dfebf89e.jpg https://telegra.ph/file/90a8b06e67a5e8ae93aca.jpg https://telegra.ph/file/ed704674eb76bf97a64cf.jpg https://telegra.ph/file/c36b9df778b041b98a9b1.jpg https://telegra.ph/file/74faee934590af2d8df9d.jpg https://telegra.ph/file/88648e41b8328021e442b.jpg https://telegra.ph/file/b8d748278778376189873.jpg https://telegra.ph/file/0b3e50f8bcf30afb26cad.jpg https://telegra.ph/file/750035e745a5dd52198b3.jpg https://telegra.ph/file/6e6693e244d5fc958e322.jpg https://telegra.ph/file/85d8846b4e08fafb62a2e.jpg https://telegra.ph/file/976c9475eae78bbd03d96.jpg https://telegra.ph/file/4cc6147bec045873cac7a.jpg https://telegra.ph/file/6f8cc82170d704ad40ee9.jpg https://telegra.ph/file/06eaa902bffd79209658e.jpg https://telegra.ph/file/14f3c00387f6b3c16d425.jpg https://telegra.ph/file/7d5264428089f785d3d35.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5650200786 5681376068').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://bat:bat@cluster0.3lkpcix.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1001594651224))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Mx_Support_Bot')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<b>{file_caption}</i>\n\n<b>🍿 Ꭾօաɛʀɛɖ Ɓꪗ: @iPopkarn</b>")
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
SHORTNER_SITE = "mdiskshortner.link"
SHORTNER_API = "7aeadf631fe48fce0ed4b480300ee24c89a1b8ae"

