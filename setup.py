try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Arnaud Chen-yen-su',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'arnaud.chenyensu@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)