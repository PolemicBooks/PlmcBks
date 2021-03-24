from .documents import Documents
from .objects import Dict


class Cover(Dict):
	
	
	def __init__(
		self,
		id,
		message_id,
		date,
		file_extension,
		file_name,
		file_size,
		file_unique_id,
		file_gdrive_id,
		mime_type,
		resolution
	):
		self.id = id
		self.message_id = message_id
		self.date = date
		self.file_extension = file_extension
		self.file_name = file_name
		self.file_size = file_size
		self.file_unique_id = file_unique_id
		self.file_gdrive_id = file_gdrive_id
		self.mime_type = mime_type
		self.resolution = resolution


class Covers(Documents):
	pass
