from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in bairesort_app/__init__.py
from bairesort_app import __version__ as version

setup(
	name="bairesort_app",
	version=version,
	description="Beni Repo",
	author="Raya Solutions",
	author_email="ranz.manalo@rayasolutionsph.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
