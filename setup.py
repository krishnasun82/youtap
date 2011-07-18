import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "youtap",
    version = "0.1",
    author = "Sundar Srinivasan",
    author_email = "krishna.sun@gmail.com",
    description = ("Program to download YouTube video as flv file"),
    license = "MIT",
    keywords = ["youtube", "download", "http"],
    url = "https://github.com/krishnasun82/youtap",
    packages=['src'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
