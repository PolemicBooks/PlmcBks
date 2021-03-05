from plmcbks import (
	authors,
	artists,
	narrators,
	publishers,
	categories,
	types,
	books
)
from plmcbks.types import (
	Authors,
	Artists,
	Narrators,
	Publishers,
	Categories,
	Types,
	Books
)


def test_type():
	
	assert isinstance(authors, Authors)
	
	assert isinstance(artists, Artists)
	
	assert isinstance(narrators, Narrators)
	
	assert isinstance(publishers, Publishers)
	
	assert isinstance(categories, Categories)
	
	assert isinstance(types, Types)
	
	assert isinstance(books, Books)

