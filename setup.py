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
    name="sound-streamlit",
    version="0.1.3",
    author="YeaMerci",
    author_email="entertomerci@gmail.com",
    description="The package contains a ready-to-use streamlit widget for downloading or recording audio. There is support for most audio formats.",
    long_description=long_description,
    install_requires=requirements,
    long_description_content_type="text/markdown",
    url="https://github.com/YeaMerci/sound-streamlit",
    packages=find_packages(),
    include_package_data=True,
    keywords=[
        "waveform", "converting",
        "streamlit-audio-recorder",
        "recorder", "audio",
        "streamlit", "streamlit-component"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10"
)
