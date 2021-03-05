from setuptools import setup

package_data = {
	"plmcbks": [
		"package_data/artists.json.xz",
		"package_data/authors.json.xz",
		"package_data/books.json.xz",
		"package_data/categories.json.xz",
		"package_data/narrators.json.xz",
		"package_data/publishers.json.xz",
		"package_data/types.json.xz",
		"package_data/years.json.xz"
	]
}

classifiers = [
	"License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
	"Operating System :: Unix",
	"Topic :: Internet",
	"Development Status :: 5 - Production/Stable",
	"Intended Audience :: Developers",
	"Programming Language :: Python :: 3.6",
	"Programming Language :: Python :: 3.7",
	"Programming Language :: Python :: 3.8",
	"Programming Language :: Python :: 3.9"
]

packages = [
	"plmcbks",
	"plmcbks/config",
	"plmcbks/utils",
	"plmcbks/types"
]

setup(
	name="PlmcBks",
	version="0.1",
	author="SnwMds",
	author_email="snwmds@tutanota.com",
	description="API interna do Polemic Books.",
	license="LGPL-3.0",
	url="https://github.com/PolemicBooks/PlmcBks",
	packages=packages,
	include_package_data=True,
	package_data=package_data,
	classifiers=classifiers,
	python_requires=">=3.6",
)
