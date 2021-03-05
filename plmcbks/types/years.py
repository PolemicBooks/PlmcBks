from .entities import Entity, Entities


class Year(Entity):
	pass


class Years(Entities):
	
	
	# Este método é usado para pesquisar por entidades com base no nome.
	def slow_search(self, query):
		"""
		O método de pesquisa lenta exclui algumas palavras consideradas irrelevantes e
		também desconsidera a posição em que as palavras na pesquisa original aparecem.
		
		O propósito disso é obter resultados menos exatos, só que possivelmente mais
		relevantes.
		"""
		
		results = Entities()
		
		# Aqui separamos cada palavra com mais de 2 caracteres em uma lista.
		splited_query = [
			word for word in query.split() if len(word) > 2
		]
		
		if not splited_query:
			return results
		
		for entity in self.iter():
			
			# Pesquisa por correspondências no nome da entidade.
			if entity is not None:
				if (query in str(entity.name) or
					all(word in str(entity.name) for word in splited_query)):
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
		
		for entity in self.iter():
			
			# Pesquisa por correspondências no nome da entidade.
			if entity is not None:
				if (query in str(entity.name)):
					results.append(entity)
		
		return results
	
	
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


