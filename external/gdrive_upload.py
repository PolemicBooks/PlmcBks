import os
import lzma
import gc

import pyrogram
from pyrogram.errors import UnknownError
import orjson
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

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

print(f"Go to {gauth.GetAuthUrl()}")

gauth.Auth(input("Type the authentication code: "))
drive = GoogleDrive(gauth)

client = pyrogram.Client(**PYROGRAM_OPTIONS)
client.start()

for index, book in enumerate(books):
	if gdrive.get(book["cover"]["file_unique_id"]) is None:
		
		upload_file = None
		
		# Baixo a imagem do Telegram e salvo localmente
		while not upload_file:
			try:
				message = client.get_messages(BOOKS_CHAT, book["cover"]["message_id"])
				upload_file = client.download_media(message)
			except UnknownError:
				pass
		
		# Envio a imagem local para o Google Drive
		photo = drive.CreateFile({'title': str(book["title"])})
		photo.SetContentFile(upload_file)
		photo.Upload()
		
		# Torno público o arquivo que foi enviado
		photo.InsertPermission({
			'type': 'anyone',
			'value': 'anyone',
			'role': 'reader'})
		
		# Salvo o ID do arquivo enviado
		gdrive.update({book["cover"]["file_unique_id"]: photo["id"]})
		
		# Excluo o arquivo salvo localmente
		os.remove(upload_file)
		
		print(photo['alternateLink'])
		
		with lzma.open(filename=gdrive_file, **LZMA_COMPRESSION) as file:
			file.write(orjson.dumps(gdrive))
		
		gc.collect()

client.log_out()
