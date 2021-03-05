from .books import Books
from .objects import Dict, List


class Entity(Dict):
	
	
	def __init__(self, id, name, total_books=0):
		self.id = id
		self.name = name
		self.total_books = total_books
	
	
	def get_books(self, books):
		
		results = Books()
		
		attribute = self.__class__.__name__.lower()
		
		for book in books.iter():
			if getattr(book, attribute) is self:
				results.append(book)
		
		return results
			


class Entities(List):
	
	
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
		elif isinstance(item, str):
			for entity in self.iter():
				if entity.name == item:
					return entity
		else:
			raise TypeError(f"expecting str or int, got {item.__class__.__name__}")
		
		raise KeyError(item)
