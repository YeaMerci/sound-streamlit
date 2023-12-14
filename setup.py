from pathlib import Path
from setuptools import find_packages, setup


with open("requirements.txt") as f:
    requirements = [
        line.strip()
        for line in f.readlines()
        if not line.startswith("-f")
    ]

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="streamlit-audio-widgets",
    version="0.1.0",
    author="Kotov Daniil",
    author_email="entertomerci@gmail.com",
    description="The package contains a ready-to-use streamlit widget for downloading or recording audio. There is support for most audio formats.",
    long_description=long_description,
    install_requires=requirements.
    long_description_content_type="text/markdown",
    url="https://github.com/YeaMerci/streamlit-audio-widgets",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=[
        "streamlit>=0.63",
    ],
)
