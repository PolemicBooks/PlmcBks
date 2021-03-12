import re
import unicodedata


WHITESPACES_RE = re.compile(r"\s+")


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


def strip_spaces(string):
	return WHITESPACES_RE.sub(" ", string)


def to_query(string):
	return strip_spaces(strip_accents(strip_punctuation(string.lower())))

