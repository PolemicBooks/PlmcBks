import unicodedata


def strip_accents(string):
	return "".join(
		[
			character for character in unicodedata.normalize("NFKD", string) if (
				not unicodedata.combining(character)
			)
		]
	)


def strip_punctuation(string):
	return "".join(
		[
			character for character in string if (
				character.isalpha() or 
				character.isdigit() or
				character.isspace()
			)
		]
	)


def to_query(string):
	return strip_accents(strip_punctuation(string.lower()))

