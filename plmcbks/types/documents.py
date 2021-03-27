from .objects import Dict, List


class Document(Dict):
	
	
	def __init__(
		self,
		id,
		message_id,
		date,
		file_extension,
		file_size,
		file_unique_id,
		file_gdrive_id,
		mime_type
	):
		self.id = id
		self.message_id = message_id
		self.date = date
		self.file_extension = file_extension
		self.file_size = file_size
		self.file_unique_id = file_unique_id
		self.file_gdrive_id = file_gdrive_id
		self.mime_type = mime_type


	def get_book(self, books):
		
		for book in books.iter():
			for document in book.documents.iter():
				if document is self:
					return book


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
	
	