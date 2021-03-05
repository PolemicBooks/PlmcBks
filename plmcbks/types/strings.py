from ..utils.strings import to_query


class String(str):
	
	
	def __init__(self, string):
		self.query = to_query(string)

