import random

from ..utils.strings import to_query
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
	
	
	def get_many(self, items):
		
		results = Entities()
		
		for entity in self.iter():
			if entity.id in items or entity.name in items:
				results.append(entity)
		
		return results
	
	
	def get_random(self, choices=1):
		"""Este método irá retornar uma ou mais entidades aleatórias da lista."""
		
		choices = random.choices(self.list(), k=choices)
		
		return Entities(choices)
	
	
	def __getitem__(self, item):
		if isinstance(item, int):
			for entity in self.iter():
				if entity.id == entity:
					return entity
		elif isinstance(item, str):
			for entity in self.iter():
				if entity.name == item:
					return entity
		else:
			raise TypeError(f"expecting str or int, got {item.__class__.__name__}")
		
		raise KeyError(item)
	
	
	# Este método é usado para pesquisar por entidades com base no nome.
	def slow_search(self, query):
		"""
		O método de pesquisa lenta exclui algumas palavras consideradas irrelevantes e
		também desconsidera a posição em que as palavras na pesquisa original aparecem.
		
		O propósito disso é obter resultados menos exatos, só que possivelmente mais
		relevantes.
		"""
		
		results = Entities()
		
		# Aqui convertemos todos os caracteres para minúsculo e também removemos os acentos e as
		# pontuações.
		query = to_query(query)
		
		# Aqui separamos cada palavra com mais de 2 caracteres em uma lista.
		splited_query = [
			word for word in query.split() if len(word) > 2
		]
		
		if not splited_query:
			return results
		
		for entity in self.iter():
			
			# Pesquisa por correspondências no nome da entidade.
			if entity is not None:
				if (query in entity.name.query or
					all(word in entity.name.query for word in splited_query)):
					results.append(entity)
		
		return results
	
	
	# Este método também é usado para pesquisar por entidades.
	def fast_search(self, query):
		"""
		O método de pesquisa rápida, ao contrário do método de pesquisa lenta,
		não exclui palavras consideradas irrelevantes e também leva em conta a posição
		original de cada palavra.
		
		Isso lhe trará resultados mais exatos, só que possivelmente menos relevantes.
		"""
		
		results = Entities()
		
		# Aqui convertemos todos os caracteres para minúsculo e também removemos os acentos e as
		# pontuações.
		query = to_query(query)
		
		for entity in self.iter():
			
			# Pesquisa por correspondências no nome da entidade.
			if entity is not None:
				if (query in entity.name.query):
					results.append(entity)
		
		return results

