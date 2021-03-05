import pathlib
import os

MODULE_PATH = pathlib.Path(__file__)

PACKAGE_PATH = os.path.join(
	MODULE_PATH.parent.parent, "package_data")

BOOKS_DATA = (
	os.path.join(PACKAGE_PATH, "categories.json.xz"),
	os.path.join(PACKAGE_PATH, "types.json.xz"),
	os.path.join(PACKAGE_PATH, "authors.json.xz"),
	os.path.join(PACKAGE_PATH, "artists.json.xz"),
	os.path.join(PACKAGE_PATH, "narrators.json.xz"),
	os.path.join(PACKAGE_PATH, "publishers.json.xz"),
	os.path.join(PACKAGE_PATH, "years.json.xz"),
	os.path.join(PACKAGE_PATH, "books.json.xz")
)
