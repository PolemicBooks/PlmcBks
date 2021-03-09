from .objects import Dict, List


class Document(Dict):
	
	
	def __init__(
		self,
		id,
		message_id,
		date,
		file_extension,
		file_name,
		file_size,
		mime_type
	):
		self.id = id
		self.message_id = message_id
		self.date = date
		self.file_extension = file_extension
		self.file_name = file_name
		self.file_size = file_size
		self.mime_type = mime_type



class Documents(List):
	
	
	def get(self, item):
		try:
			entity = self[item]
		except (KeyError, IndexError):
			return
		else:
			return entity
	
	
	def __getitem__(self, item):
		if isinstance(item, int):
			return self.list()[item]
		else:
			raise TypeError(f"expecting int, got {item.__class__.__name__}")
	
	