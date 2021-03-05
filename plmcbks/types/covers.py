from .objects import Dict


class Cover(Dict):
	
	
	def __init__(
		self,
		date,
		file_extension,
		file_id,
		file_name,
		file_size,
		mime_type,
		resolution
	):
		self.date = date
		self.file_extension = file_extension
		self.file_id = file_id
		self.file_name = file_name
		self.file_size = file_size
		self.mime_type = mime_type
		self.resolution = resolution
