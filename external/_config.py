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

MAX_MESSAGES = 250000

IGNORED_MESSAGES = (
	2,
	10596,
	10597,
	13337,
	131117,
	134378,
	134379,
	181062,
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
	181061,
	181063,
	181064,
	181066,
	181067,
	201101,
	201099,
	201098,
	201097,
	201096,
	200995,
	200994,
	200993,
	200987,
	200988,
	200989,
	200990,
	200991,
	200992,
	200993,
	199087,
	199086,
	199085,
	199084,
	186747,
	186746,
	186747,
	199084,
	199085,
	199086,
	199087,
	200987,
	200988,
	200989,
	200990,
	200991,
	200992,
	200993,
	200994,
	200995,
	201096,
	201097,
	201098,
	201099,
	201101,
	223038,
	223039,
	223040,
	223041,
	223042,
	223044,
	223423,
	223424
)
