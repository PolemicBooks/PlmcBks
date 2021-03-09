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
		mime_type,
		resolution
	):
		self.id = id
		self.message_id = message_id
		self.date = date
		self.file_extension = file_extension
		self.file_name = file_name
		self.file_size = file_size
		self.mime_type = mime_type
		self.resolution = resolution


class Covers(Documents):
	pass
