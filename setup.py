import re

import setuptools
from setuptools import find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

# we are using the packages in `requirements.txt` for now,
# not 100% ideal but will do
with open("requirements.txt", "r") as fh:
    install_requires = fh.read().split("\n")

setuptools.setup(
    name="yolov11",
    version="0.0.1",
    author="Me",
    author_email="francesco.zuppichini@gmail.com",
    description="To the moon!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FrancescoSaverioZuppichini/yolov11",
    install_requires=install_requires,
    packages=find_packages(exclude=("tests",)),
    extras_require={
        "dev": ["flake8", "black==22.3.0", "isort", "twine", "wheel"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
