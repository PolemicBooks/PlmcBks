import lzma
import os

import orjson

from _config import LZMA_COMPRESSION, PACKAGE_DATA

gdrive_file = os.path.join(PACKAGE_DATA, "gdrive.json.xz")
books_file = os.path.join(PACKAGE_DATA, "books.json.xz")

if os.path.exists(gdrive_file):
	with lzma.open(filename=gdrive_file, mode="r") as file:
		gdrive = orjson.loads(file.read())
else:
	gdrive = {}

with lzma.open(filename=books_file, mode="r") as file:
	books = orjson.loads(file.read())

for index, book in enumerate(list(books)):
	
	gdrive_id = gdrive.get(book["cover"]["file_unique_id"])
	
	if gdrive_id is not None:
		books[index]["cover"]["file_gdrive_id"] = gdrive_id
		continue
	
	for dindex, document in enumerate(book["documents"]):
		gdrive_id = gdrive.get(document["file_unique_id"])
		if gdrive_id is not None:
			books[index]["documents"][dindex]["file_gdrive_id"] = gdrive_id


with lzma.open(filename=books_file, **LZMA_COMPRESSION) as file:
	file.write(orjson.dumps(books))
