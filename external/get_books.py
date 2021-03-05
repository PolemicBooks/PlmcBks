import json
import time
import os

from pyrogram import Client

from _config import *
from _core import Scraper
from _utils import *

message_id = 0

scraper = Scraper()

books = []

client = Client(**PYROGRAM_OPTIONS)
client.start()

message = client.get_messages(
	FALLBACK_COVER["chat_id"], FALLBACK_COVER["message_id"])

fallback_photo = {
	"message_id": message.message_id,
	"date": message.photo.date,
	"file_extension": "jpeg",
	"file_id": message.photo.file_id,
	"file_name": "no_cover" + ".jpeg",
	"file_size": message.photo.file_size,
	"mime_type": "image/jpeg",
	"resolution": {
		"height": message.photo.height,
		"width": message.photo.width
	}
}

book = {}

while message_id < MAX_MESSAGES:
	
	message_id += 1
	
	# Essas mensagens não são publicações de livros
	if message_id in IGNORED_MESSAGES:
		continue
	
	message = client.get_messages(BOOKS_CHAT, message_id)
	
	if message.empty or message.service:
		continue
	
	if message.photo and message.caption:
		if book:
			books.append(book)
		
		scraper.set_text(message.caption.markdown)
		extrctd = scraper.extract()
		
		book = {
			"message_id": message.message_id,
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
			"views": message.views,
			"photo": {
				"date": message.photo.date,
				"file_extension": "jpeg",
				"file_id": message.photo.file_id,
				"file_name": extrctd["title"] + ".jpeg" if extrctd["title"] is not None else "cover.jpeg",
				"file_size": message.photo.file_size,
				"mime_type": "image/jpeg",
				"resolution": {
					"height": message.photo.height,
					"width": message.photo.width
				}
			},
			"documents": [],
		}
		
		continue
		
	if message.text:
		if book:
			books.append(book)
		
		scraper.set_text(message.text.markdown)
		extrctd = scraper.extract()
		
		book = {
			"message_id": message.message_id,
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
			"views": message.views,
			"photo": fallback_photo,
			"documents": []
		}
		
		continue
	
	if message.document:
		document = {
			"message_id": message.message_id,
			"date": message.document.date,
			"file_extension": message.document.file_name.split(".")[-1],
			"file_id": message.document.file_id,
			"file_name": message.document.file_name,
			"file_size": message.document.file_size,
			"mime_type": message.document.mime_type,
			"views": message.views
		}
		
		book["total_size"] += message.document.file_size
		
		book["documents"].append(document)
		
		print(json.dumps(book, indent=4))
		

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
	(categories, os.path.join(BOOKS_DIRECTORY, "categories.json.xz")),
	(types, os.path.join(BOOKS_DIRECTORY, "types.json.xz")),
	(authors, os.path.join(BOOKS_DIRECTORY, "authors.json.xz")),
	(artists, os.path.join(BOOKS_DIRECTORY, "artists.json.xz")),
	(narrators, os.path.join(BOOKS_DIRECTORY, "narrators.json.xz")),
	(publishers, os.path.join(BOOKS_DIRECTORY, "publishers.json.xz")),
	(years, os.path.join(BOOKS_DIRECTORY, "years.json.xz")),
	(books, os.path.join(BOOKS_DIRECTORY, "books.json.xz"))
]

for data, filename in files:
	data_bytes = bytes(json.dumps(data), encoding="utf-8")
	with lzma.open(filename=filename, **LZMA_COMPRESSION) as file:
		file.write(data_bytes)
