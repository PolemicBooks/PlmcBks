import os
import pathlib
import lzma

CWD = pathlib.Path(os.getcwd())

BOOKS_DIRECTORY = os.path.join(CWD.parent, "plmcbks/package_data")

PYROGRAM_OPTIONS = {
	"session_name": "bot",
	"api_id": None,
	"api_hash": None,
	"bot_token": None,
	"workdir": os.path.join(CWD, ".pyrogram"),
	"no_updates": True
}

FALLBACK_COVER = {
	"chat_id": -1001341909754,
	"message_id": 2
}

LZMA_COMPRESSION = {
	"mode": "w",
	"format": lzma.FORMAT_XZ,
	"check": lzma.CHECK_SHA256,
	"preset": 9
}

BOOKS_CHAT = -1001436494509

MAX_MESSAGES = 145000

IGNORED_MESSAGES = (2, 10596, 10597, 13337, 131117)
