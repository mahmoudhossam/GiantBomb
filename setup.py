#!/usr/bin/env python

from setuptools import setup
from GiantBomb import giantbomb

def read(fname):
        return open(os.path.join(os.path.dirname(__file__), fname)).read()

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name = "an_example_pypi_project",
    version = giantbomb.__version__,
    author = giantbomb.__author__,
    author_email = "xupisco@gmail.com",
    description = ("A Python wrapper for the Giantbomb API."),
    license = "BSD",
    keywords = "giantbomb api wrapper",
    url = "https://github.com/xupisco/GiantBomb",
    packages=['GiantBomb'],
    long_description=read('README.md'),
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: BSD License",
    ],
)