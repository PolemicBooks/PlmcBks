import os
import pathlib
import lzma

CWD = pathlib.Path(os.getcwd())

PACKAGE_DATA = os.path.join(CWD.parent, "plmcbks/package_data")

PYROGRAM_OPTIONS = {
	"session_name": "bot",
	"api_id": None,
	"api_hash": None,
	"bot_token": None,
	"workdir": os.path.join(CWD, ".pyrogram"),
	"no_updates": True
}

LZMA_COMPRESSION = {
	"mode": "w",
	"format": lzma.FORMAT_XZ,
	"check": lzma.CHECK_SHA256,
	"preset": 9
}

BOOKS_CHAT = -1001436494509

FALLBACK_COVER = {
	"chat_id": BOOKS_CHAT,
	"message_id": 146389
}

MAX_MESSAGES = 181061

IGNORED_MESSAGES = (
	2,
	10596,
	10597,
	13337,
	131117,
	146389,
	148442,
	148444,
	148445,
	148446,
	148447,
	148448,
	148449,
	148450,
	148451,
	148452,
	155238,
	160782,
	165727,
	165728,
	177270,
	177271,
	177273,
	181061
)

INVALID_MESSAGES_FILE = os.path.join(PACKAGE_DATA, "invalid_messages.json.xz")
