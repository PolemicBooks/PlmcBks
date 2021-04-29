import re


class Scraper:
	
	
	def __init__(self):
		self.title = re.compile(r"\*\*(.+)\*\*")
		self.author = re.compile(r"\n\*\*Autor\*\*:\s__(.+)__")
		self.artist = re.compile(r"\n\*\*Arte\*\*:\s__(.+)__")
		self.year = re.compile(r"\n\*\*Ano\*\*:\s__(.+)__")
		self.publisher = re.compile(r"\n\*\*Editora\*\*:\s__(.+)__")
		self.book_type = re.compile(r"\n\*\*Tipo\*\*:\s__(.+)__")
		self.category = re.compile(r"\n\*\*Categoria\*\*:\s__(.+)__")
		self.narrator = re.compile(r"\n\*\*Narrador\*\*:\s__(.+)__")
		self.duration = re.compile(r"\n\*\*Duração\*\*:\s__(.+)__")
		self.genre = re.compile(r"\n\*\*Gênero\*\*:\s__(.+)__")
		self.volumes = re.compile(r"\n\*\*Volumes\*\*:\s__(.+)__")
		self.chapters = re.compile(r"\n\*\*Capítulos\*\*:\s__(.+)__")
	
	
	def get_title(self):
		
		result = self.title.findall(
			self.text.split(sep="\n")[0])
		
		if result:
			return result[0].strip()
	
	
	def get_author(self):
		
		result = self.author.findall(self.text)
		
		if result:
			return result[0].strip()
	
	
	def get_artist(self):
		
		result = self.artist.findall(self.text)
		
		if result:
			return result[0].strip()
	
	
	def get_year(self):
		
		result = self.year.findall(self.text)
		
		if result:
			return int(result[0].strip())
	
	
	def get_publisher(self):
		
		result = self.publisher.findall(self.text)
		
		if result:
			return result[0].strip()
	
	
	def get_type(self):
		
		result = self.book_type.findall(self.text)
		
		if result:
			return result[0].strip()
	
	
	def get_category(self):
		
		result = self.category.findall(self.text)
		
		if result:
			return result[0].strip()
	
	
	def get_narrator(self):
		
		result = self.narrator.findall(self.text)
		
		if result:
			return result[0].strip()
	
	
	def get_duration(self):
		
		result = self.duration.findall(self.text)
		
		if result:
			return result[0].strip()
	
	
	def get_genre(self):
		
		result = self.genre.findall(self.text)
		
		if result:
			return [
				genre.strip() for genre in result[0].split(sep=",")
			]
	
	
	def get_volumes(self):
		
		result = self.volumes.findall(self.text)
		
		if result:
			try:
				_float = float(result[0].strip())
			except ValueError:
				return
			else:
				if _float.is_integer():
					return int(_float)
				else:
					return _float
	
	
	def get_chapters(self):
		
		result = self.chapters.findall(self.text)
		
		if result:
			try:
				_float = float(result[0].strip())
			except ValueError:
				return
			else:
				if _float.is_integer():
					return int(_float)
				else:
					return _float
	
	
	def get_flags(self):
		
		flags = []
		
		if "__O material apresentado pode ser de baixa qualidade.__" in self.text:
			flags.append("poor_quality")
	
		if "__Capítulos ou páginas podem estar faltando.__" in self.text:
			flags.append("missing_content")
		
		return flags
	
	
	def set_text(self, text):
		self.text = text
	
	
	def extract(self):
		
		return {
			"title": self.get_title(),
			"author": self.get_author(),
			"artist": self.get_artist(),
			"year": self.get_year(),
			"publisher": self.get_publisher(),
			"type": self.get_type(),
			"category": self.get_category(),
			"narrator": self.get_narrator(),
			"duration": self.get_duration(),
			"genre": self.get_genre(),
			"volumes": self.get_volumes(),
			"chapters": self.get_chapters(),
			"flags": self.get_flags()
		}

