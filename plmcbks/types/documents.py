from .objects import Dict, List


class Document(Dict):
	
	
	def __init__(
		self,
		message_id,
		date,
		file_extension,
		file_id,
		file_name,
		file_size,
		mime_type,
		views
	):
		self.message_id = message_id
		self.date = date
		self.file_extension = file_extension
		self.file_id = file_id
		self.file_name = file_name
		self.file_size = file_size
		self.mime_type = mime_type
		self.views = views



class Documents(List):
	pass

