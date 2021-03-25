import os
import lzma

import pyrogram
import orjson
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from _config import (
	PACKAGE_DATA,
	PYROGRAM_OPTIONS,
	BOOKS_CHAT,
	LZMA_COMPRESSION
)

gdrive_file = os.path.join(PACKAGE_DATA, "gdrive.json.xz")
books_file = os.path.join(PACKAGE_DATA, "books.json.xz")

if os.path.exists(gdrive_file):
	with lzma.open(filename=gdrive_file, mode="r") as file:
		gdrive = orjson.loads(file.read())
else:
	gdrive = {}

with lzma.open(filename=books_file, mode="r") as file:
	books = orjson.loads(file.read())

# Create GoogleDrive instance with authenticated GoogleAuth instance.
gauth = GoogleAuth()
drive = GoogleDrive(gauth)

client = pyrogram.Client(**PYROGRAM_OPTIONS)
client.start()

for index, book in enumerate(books):
	if gdrive.get(book["cover"]["file_unique_id"]) is None:
		message = client.get_messages(BOOKS_CHAT, book["cover"]["message_id"])
		upload_file = client.download_media(message)
		
		photo = drive.CreateFile({'title': str(book["title"])})
		photo.SetContentFile(upload_file)
		photo.Upload()
		
		os.remove(upload_file)
		
		photo.InsertPermission(
			{
				'type': 'anyone',
				'value': 'anyone',
				'role': 'reader'}
		)
		
		gdrive.update({book["cover"]["file_unique_id"]: photo["id"]})
		
		print(photo['alternateLink'])
		
		with lzma.open(filename=gdrive_file, **LZMA_COMPRESSION) as file:
			file.write(orjson.dumps(gdrive))

client.log_out()