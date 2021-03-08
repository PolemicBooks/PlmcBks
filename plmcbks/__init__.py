import json
import lzma

from .config.files import BOOKS_DATA
from .types import (
	Author,
	Authors,
	Artist,
	Artists,
	Category,
	Categories,
	Type,
	Types,
	Narrator,
	Narrators,
	Publisher,
	Publishers,
	Year,
	Years,
	Book,
	Books,
	String,
	Cover,
	Resolution,
	Document,
	Documents
)
from .__version__ import (
	__description__,
	__title__,
	__version__
)


(
	categories, types, authors, artists,
	narrators, publishers, years, books
) = BOOKS_DATA

# Categorias
with lzma.open(filename=categories, mode="r") as xzfile:
	content = xzfile.read().decode()

categories = Categories()

for index, category in enumerate(json.loads(content)):
	categories.append(
		Category(id=index, name=String(category))
	)

# Tipos
with lzma.open(filename=types, mode="r") as xzfile:
	content = xzfile.read().decode()

types = Types()

for index, type in enumerate(json.loads(content)):
	types.append(
		Type(id=index, name=String(type))
	)

# Autores
with lzma.open(filename=authors, mode="r") as xzfile:
	content = xzfile.read().decode()

authors = Authors()

for index, author in enumerate(json.loads(content)):
	authors.append(
		Author(id=index, name=String(author))
	)

# Artistas
with lzma.open(filename=artists, mode="r") as xzfile:
	content = xzfile.read().decode()

artists = Artists()

for index, artist in enumerate(json.loads(content)):
	artists.append(
		Artist(id=index, name=String(artist))
	)

# Narradores
with lzma.open(filename=narrators, mode="r") as xzfile:
	content = xzfile.read().decode()

narrators = Narrators()

for index, narrator in enumerate(json.loads(content)):
	narrators.append(
		Narrator(id=index, name=String(narrator))
	)

# Editoras
with lzma.open(filename=publishers, mode="r") as xzfile:
	content = xzfile.read().decode()

publishers = Publishers()

for index, publisher in enumerate(json.loads(content)):
	publishers.append(
		Publisher(id=index, name=String(publisher))
	)

# Anos
with lzma.open(filename=years, mode="r") as xzfile:
	content = xzfile.read().decode()

years = Years()

for index, year in enumerate(json.loads(content)):
	years.append(
		Year(id=index, name=year)
	)

# Livros
with lzma.open(filename=books, mode="r") as xzfile:
	content = xzfile.read().decode()

books = Books()

for index, book in enumerate(json.loads(content)):
	
	if book["title"] is not None:
		title = String(book["title"])
	else:
		title = None
	
	if book["type"] is not None:
		book_type = types[book["type"]]
		book_type.total_books += 1
	else:
		book_type = None
	
	if book["category"] is not None:
		category = categories[book["category"]]
		category.total_books += 1
	else:
		category = None
	
	if book["author"] is not None:
		author = authors[book["author"]]
		author.total_books += 1
	else:
		author = None
	
	if book["artist"] is not None:
		artist = artists[book["artist"]]
		artist.total_books += 1
	else:
		artist = None
	
	if book["narrator"] is not None:
		narrator = narrators[book["narrator"]]
		narrator.total_books += 1
	else:
		narrator = None
	
	if book["publisher"] is not None:
		publisher = publishers[book["publisher"]]
		publisher.total_books += 1
	else:
		publisher = None
	
	if book["year"] is not None:
		year = years[str(book["year"])]
		year.total_books += 1
	else:
		year = None
	
	documents = Documents()
	
	for document in book["documents"]:
		documents.append(
			Document(
				message_id=document["message_id"],
				date=document["date"],
				file_extension=document["file_extension"],
				file_id=document["file_id"],
				file_name=document["file_name"],
				file_size=document["file_size"],
				mime_type=document["mime_type"]
			)
		)
	
	books.append(
		Book(
			id=index,
			message_id=book["message_id"],
			date=book["date"],
			title=title,
			type=book_type,
			category=category,
			genre=book["genre"],
			duration=book["duration"],
			total_size=book["total_size"],
			author=author,
			artist=artist,
			narrator=narrator,
			publisher=publisher,
			year=year,
			volumes=book["volumes"],
			chapters=book["chapters"],
			language=book["language"],
			views=book["views"],
			cover=Cover(
				date=book["photo"]["date"],
				file_extension=book["photo"]["file_extension"],
				file_id=book["photo"]["file_id"],
				file_name=book["photo"]["file_name"],
				file_size=book["photo"]["file_size"],
				mime_type=book["photo"]["mime_type"],
				resolution=Resolution(
					height=book["photo"]["resolution"]["height"],
					width=book["photo"]["resolution"]["width"]
				)
			),
			documents=documents
		)
	)

__all__ = [
    "__description__",
    "__title__",
    "__version__",
	"authors",
	"artists",
	"narrators",
	"publishers",
	"categories",
	"types",
	"years",
	"books"

]

for __name in dict(locals()):
	if __name.startswith("__") or __name in __all__:
		continue
	del locals()[__name]

__locals = locals()

for __name in __all__:
    if not __name.startswith("__"):
        setattr(__locals[__name], "__module__", "plmcbks")

del __name