from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erp_local/__init__.py
from erp_local import __version__ as version

setup(
	name="erp_local",
	version=version,
	description="for erpdemo",
	author="riddhi",
	author_email="rr@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
