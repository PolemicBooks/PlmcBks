import time
import os

import orjson
import pyrogram

from _config import *
from _core import Scraper
from _utils import *

message_id = 0

scraper = Scraper()

books = []

client = pyrogram.Client(**PYROGRAM_OPTIONS)
client.start()

message = client.get_messages(
	FALLBACK_COVER["chat_id"], FALLBACK_COVER["message_id"])

fallback_photo = {
	"id": None,
	"message_id": message.message_id,
	"date": message.photo.date,
	"file_extension": "jpeg",
	"file_size": message.photo.file_size,
	"file_unique_id": message.photo.file_unique_id,
	"file_gdrive_id": None,
	"mime_type": "image/jpeg",
	"resolution": {
		"height": message.photo.height,
		"width": message.photo.width
	}
}

book = {}

book_id = 0
cover_id = 0
document_id = 0

if os.path.exists(INVALID_MESSAGES_FILE):
	with lzma.open(filename=INVALID_MESSAGES_FILE, mode="r") as file:
		invalid_messages = orjson.loads(file.read())
else:
	invalid_messages = []

while message_id < MAX_MESSAGES:
	
	message_id += 1
	
	# Essas mensagens não são publicações de livros
	if message_id in IGNORED_MESSAGES:
		continue
	
	if message_id in invalid_messages:
		continue
	
	message = client.get_messages(BOOKS_CHAT, message_id)
	
	if message.empty or message.service:
		invalid_messages.append(message_id)
		continue
	
	if message.photo and message.caption:
		if book:
			books.append(book)
		
		scraper.set_text(message.caption.markdown)
		extrctd = scraper.extract()
		
		book = {
			"id": book_id,
			"message_id": message.message_id,
			"date": message.date,
			"title": extrctd["title"],
			"type": extrctd["type"],
			"category": extrctd["category"],
			"genre": extrctd["genre"],
			"duration": None if extrctd["type"] != "Audiobook" else duration_to_seconds(message.caption.markdown),
			"total_size": 0,
			"author": extrctd["author"],
			"artist": extrctd["artist"],
			"narrator": extrctd["narrator"],
			"publisher": extrctd["publisher"],
			"year": extrctd["year"],
			"volumes": extrctd["volumes"],
			"chapters": extrctd["chapters"],
			"language": extrctd["language"],
			"cover": {
				"id": cover_id,
				"message_id": message.message_id,
				"date": message.photo.date,
				"file_extension": "jpeg",
				"file_size": message.photo.file_size,
				"file_unique_id": message.photo.file_unique_id,
				"file_gdrive_id": None,
				"mime_type": "image/jpeg",
				"resolution": {
					"height": message.photo.height,
					"width": message.photo.width
				}
			},
			"documents": [],
		}
		
		book_id += 1
		cover_id += 1
		
		continue
		
	if message.text:
		if book:
			books.append(book)
		
		scraper.set_text(message.text.markdown)
		extrctd = scraper.extract()
		
		fallback = dict(fallback_photo)
		fallback["id"] = cover_id
		
		book = {
			"id": book_id,
			"message_id": message.message_id,
			"date": message.date,
			"title": extrctd["title"],
			"type": extrctd["type"],
			"category": extrctd["category"],
			"genre": extrctd["genre"],
			"duration": None if extrctd["type"] != "Audiobook" else duration_to_seconds(message.text.markdown),
			"total_size": 0,
			"author": extrctd["author"],
			"artist": extrctd["artist"],
			"narrator": extrctd["narrator"],
			"publisher": extrctd["publisher"],
			"year": extrctd["year"],
			"volumes": extrctd["volumes"],
			"chapters": extrctd["chapters"],
			"language": extrctd["language"],
			"cover": fallback,
			"documents": []
		}
		
		book_id += 1
		cover_id += 1
		
		continue
	
	if message.document:
		document = {
			"id": document_id,
			"message_id": message.message_id,
			"date": message.document.date,
			"file_extension": message.document.file_name.split(".")[-1],
			"file_size": message.document.file_size,
			"file_unique_id": message.document.file_unique_id,
			"file_gdrive_id": None,
			"mime_type": message.document.mime_type
		}
		
		document_id += 1
		
		book["total_size"] += message.document.file_size
		
		book["documents"].append(document)
		
		print(message_id)
		

books.append(book)

categories, types, authors, artists, narrators, publishers, years = (
	[], [], [], [], [], [], []
)

for book in books:
	category, book_type, author, artist, year, narrator, publisher = (
		book.get("category"), book.get("type"), book.get("author"),
		book.get("artist"), book.get("year"), book.get("narrator"),
		book.get("publisher")
	)
	
	if category is not None and category not in categories:
		categories.append(category)
	
	if book_type is not None and book_type not in types:
		types.append(book_type)
	
	if author is not None and author not in authors:
		authors.append(author)
	
	if artist is not None and artist not in artists:
		artists.append(artist)
	
	if year is not None and year not in years:
		years.append(year)
	
	if narrator is not None and narrator not in narrators:
		narrators.append(narrator)

	if publisher is not None and publisher not in publishers:
		publishers.append(publisher)

categories.sort()
types.sort()
authors.sort()
artists.sort()
years.sort()
narrators.sort()
publishers.sort()

files = [
	(categories, os.path.join(PACKAGE_DATA, "categories.orjson.xz")),
	(types, os.path.join(PACKAGE_DATA, "types.orjson.xz")),
	(authors, os.path.join(PACKAGE_DATA, "authors.orjson.xz")),
	(artists, os.path.join(PACKAGE_DATA, "artists.orjson.xz")),
	(narrators, os.path.join(PACKAGE_DATA, "narrators.orjson.xz")),
	(publishers, os.path.join(PACKAGE_DATA, "publishers.orjson.xz")),
	(years, os.path.join(PACKAGE_DATA, "years.orjson.xz")),
	(books, os.path.join(PACKAGE_DATA, "books.orjson.xz"))
]

for data, filename in files:
	with lzma.open(filename=filename, **LZMA_COMPRESSION) as file:
		file.write(orjson.dumps(data))

with lzma.open(filename=INVALID_MESSAGES_FILE, **LZMA_COMPRESSION) as file:
	file.write(orjson.dumps([message_id for message_id in invalid_messages if message_id <= book["message_id"]]))

client.log_out()
