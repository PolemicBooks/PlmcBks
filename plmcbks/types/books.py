import random

from ..utils.strings import to_query
from .objects import Dict, List


class Book(Dict):
	
	
	def __init__(
		self,
		id,
		message_id,
		date,
		title,
		type,
		category,
		genre,
		duration,
		total_size,
		author,
		artist,
		narrator,
		publisher,
		year,
		volumes,
		chapters,
		language,
		cover,
		flags,
		documents
	):
		self.id = id
		self.message_id = message_id
		self.date = date
		self.title = title
		self.type = type
		self.category = category
		self.genre = genre
		self.duration = duration
		self.total_size = total_size
		self.author = author
		self.artist = artist
		self.narrator = narrator
		self.publisher = publisher
		self.year = year
		self.volumes = volumes
		self.chapters = chapters
		self.language = language
		self.cover = cover
		self.flags = flags
		self.documents = documents


class Books(List):
	
	
	# Este método é usado para pesquisar por livros.
	def slow_search(self, query):
		"""
		O método de pesquisa lenta exclui algumas palavras consideradas irrelevantes e
		também desconsidera a posição em que as palavras na pesquisa original aparecem.
		
		O propósito disso é obter resultados menos exatos, só que possivelmente mais
		relevantes.
		"""
		
		results = Books()
		
		# Aqui convertemos todos os caracteres para minúsculo e também removemos os acentos e as
		# pontuações.
		query = to_query(query)
		
		# Aqui separamos cada palavra com mais de 2 caracteres em uma lista.
		splited_query = [
			word for word in query.split() if len(word) > 2
		]
		
		if not splited_query:
			return results
		
		for book in self.iter():
			
			# Pesquisa por correspondências no título do livro.
			if book.title is not None:
				if (query in book.title.query or
					all(word in book.title.query for word in splited_query)):
					results.append(book)
					continue
			
			# Pesquisa por correspondências na categoria do livro.
			if book.category is not None:
				if (query in book.category.name.query or
					all(word in book.category.name.query for word in splited_query)):
					results.append(book)
					continue
			
			# Pesquisa por correspondências no nome do autor do livro.
			if book.author is not None:
				if (query in book.author.name.query or
					all(word in book.author.name.query for word in splited_query)):
					results.append(book)
					continue
			
			# Pesquisa por correspondências encontradas no nome do artista do livro.
			if book.artist is not None:
				if (query in book.artist.name.query or
					all(word in book.artist.name.query for word in splited_query)):
					results.append(book)
					continue
			
			# Pesquisa por correspondências encontradas no nome do narrador do livro.
			if book.narrator is not None:
				if (query in book.narrator.name.query or
					all(word in book.narrator.name.query for word in splited_query)):
					results.append(book)
					continue
			
			# Pesquisa por correspondências encontradas no nome da editora do livro.
			if book.publisher is not None:
				if (query in book.publisher.name.query or
					all(word in book.publisher.name.query for word in splited_query)):
					results.append(book)
					continue
		
		return results
	
	
	# Este método também é usado para pesquisar por livros.
	def fast_search(self, query):
		"""
		O método de pesquisa rápida, ao contrário do método de pesquisa lenta,
		não exclui palavras consideradas irrelevantes e também leva em conta a posição
		original de cada palavra.
		
		Isso lhe trará resultados mais exatos, só que possivelmente menos relevantes.
		"""
		
		results = Books()
		
		# Aqui convertemos todos os caracteres para minúsculo e também removemos os acentos e as
		# pontuações.
		query = to_query(query)
		
		for book in self.iter():
			
			# Pesquisa por correspondências no título do livro.
			if book.title is not None:
				if (query in book.title.query):
					results.append(book)
					continue
			
			# Pesquisa por correspondências na categoria do livro.
			if book.category is not None:
				if (query in book.category.name.query):
					results.append(book)
					continue
			
			# Pesquisa por correspondências no nome do autor do livro.
			if book.author is not None:
				if (query in book.author.name.query):
					results.append(book)
					continue
			
			# Pesquisa por correspondências encontradas no nome do artista do livro.
			if book.artist is not None:
				if (query in book.artist.name.query):
					results.append(book)
					continue
			
			# Pesquisa por correspondências encontradas no nome do narrador do livro.
			if book.narrator is not None:
				if (query in book.narrator.name.query):
					results.append(book)
					continue
			
			# Pesquisa por correspondências encontradas no nome da editora do livro.
			if book.publisher is not None:
				if (query in book.publisher.name.query):
					results.append(book)
					continue
		
		return results
	
	
	def get_random(self, choices=1):
		"""Este método irá retornar um ou mais livro aleatório da lista."""
		
		choices = random.choices(self.list(), k=choices)
		
		return Books(choices)
	
	
	def get(self, item):
		"""
		Este método é usado para obter um livro através do seu ID.
		"""
	
		try:
			entity = self[item]
		except (KeyError, IndexError):
			return
		else:
			return entity
	
	
	def get_many(self, items):
		
		results = Books()
		
		for book in self.iter():
			if book.id in items:
				results.append(entity)
		
		return results
	
	
	def __getitem__(self, item):
		if isinstance(item, int):
			return self.list()[item]
		else:
			raise TypeError(f"expecting int, got {item.__class__.__name__}")
	


