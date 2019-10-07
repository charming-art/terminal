from setuptools import setup, find_packages

PACKAGEDATA = {
	'name': 'p3',
	'packages': find_packages(include=['p3']),
}

setup(**PACKAGEDATA)