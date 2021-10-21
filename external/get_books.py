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
	"message_views": message.views,
	"file_name": "unk.jpg",
	"file_extension": "jpg",
	"file_size": message.photo.file_size,
	"file_id": message.photo.file_id,
	"file_unique_id": message.photo.file_unique_id,
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
thumbnail_id = 0

start = 1
end = start + 100

while True:
	print(start)
	
	messages = client.get_messages(
		chat_id=BOOKS_CHAT,
		message_ids=range(start, end)
	)
	
	if not messages:
		break
	
	if messages[0].message_id > MAX_MESSAGES:
		break
	
	start = end
	end = end + 100
	
	for message in messages:
		if message.message_id in IGNORED_MESSAGES:
			continue
		
		if message.empty or message.service:
			continue
			
		if message.photo and message.caption:
			if book:
				books.append(book)
			
			scraper.set_text(message.caption.markdown)
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
				"duration": None if extrctd["type"] != "Audiobook" else duration_to_seconds(message.caption.markdown),
				"total_size": 0,
				"author": extrctd["author"],
				"artist": extrctd["artist"],
				"narrator": extrctd["narrator"],
				"publisher": extrctd["publisher"],
				"year": extrctd["year"],
				"total_volumes": extrctd["volumes"],
				"total_chapters": extrctd["chapters"],
				"message_views": message.views,
				"cover": fallback if message.photo.file_unique_id == "AQAD4vP0KF0AA78lAwAB" else {
					"id": cover_id,
					"message_id": message.message_id,
					"date": message.photo.date,
					"file_name": "unk.jpg" if extrctd["title"] is None else extrctd["title"].replace("/", "+").replace("\\", "+") + "." + "jpg",
					"file_extension": "jpg",
					"file_size": message.photo.file_size,
					"file_id": message.photo.file_id,
					"file_unique_id": message.photo.file_unique_id,
					"mime_type": "image/jpeg",
					"resolution": {
						"height": message.photo.height,
						"width": message.photo.width
					}
				},
				"flags": extrctd["flags"],
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
				"total_volumes": extrctd["volumes"],
				"total_chapters": extrctd["chapters"],
				"message_views": message.views,
				"cover": fallback,
				"flags": extrctd["flags"],
				"documents": []
			}
			
			book_id += 1
			cover_id += 1
			
			continue
		
		if message.document:
			if message.document.thumbs:
				thumb = message.document.thumbs.pop(0)
			else:
				thumb = None
			
			document = {
				"id": document_id,
				"message_id": message.message_id,
				"date": message.document.date,
				"file_name": message.document.file_name,
				"file_extension": message.document.file_name.split(".")[-1],
				"file_size": message.document.file_size,
				"file_id": message.document.file_id,
				"file_unique_id": message.document.file_unique_id,
				"mime_type": message.document.mime_type,
				"thumbnail": None if not thumbnail else {
					"id": thumbnail_id,
					"message_id": message.message_id,
					"date": message.document.date,
					"file_name": "unk.jpg" if extrctd["title"] is None else extrctd["title"].replace("/", "+").replace("\\", "+") + "." + "jpg",
					"file_extension": "jpg",
					"file_size": thumbnail.file_size,
					"file_id": thumbnail.file_id,
					"file_unique_id": thumbnail.file_unique_id,
					"mime_type": "image/jpeg",
					"resolution": {
						"height": thumbnail.height,
						"width": thumbnail.width
					}
				},
				"message_views": message.views
			}
			
			document_id += 1
			
			if thumbnail:
				thumbnail_id += 1
			
			book["total_size"] += message.document.file_size
			
			book["documents"].append(document)

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
	(categories, os.path.join(PACKAGE_DATA, "categories.json.xz")),
	(types, os.path.join(PACKAGE_DATA, "types.json.xz")),
	(authors, os.path.join(PACKAGE_DATA, "authors.json.xz")),
	(artists, os.path.join(PACKAGE_DATA, "artists.json.xz")),
	(narrators, os.path.join(PACKAGE_DATA, "narrators.json.xz")),
	(publishers, os.path.join(PACKAGE_DATA, "publishers.json.xz")),
	(years, os.path.join(PACKAGE_DATA, "years.json.xz")),
	(books, os.path.join(PACKAGE_DATA, "books.json.xz"))
]

for data, filename in files:
	with lzma.open(filename=filename, **LZMA_COMPRESSION) as file:
		file.write(orjson.dumps(data))

client.log_out()
