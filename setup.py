from os import path
from setuptools import setup

VERSION = "0.0.1"

HERE = path.abspath(path.dirname(__file__))

setup(
    name="todoapp",
    version=VERSION,
    description="simple test ap",
    url="https://github.com/BillyLiggins/DRF-TDD-example",
    author="Billy Liggins",
    email="billy@gmail.com",
    license="UNLICENSED",
    packages=["todoapp"]
)
