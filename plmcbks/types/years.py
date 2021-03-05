from .entities import Entity, Entities


class Year(Entity):
	pass


class Years(Entities):
	
	
	def __getitem__(self, item):
		if isinstance(item, int):
			return self.list()[item]
		elif isinstance(item, str):
			item = int(item)
			for entity in self.iter():
				if entity.name == item:
					return entity
		else:
			raise TypeError(f"expecting str or int, got {item.__class__.__name__}")
		
		raise KeyError(item)


