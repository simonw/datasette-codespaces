from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-codespaces",
    description=" Conveniences for running Datasette on GitHub Codespaces",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-codespaces",
    project_urls={
        "Issues": "https://github.com/simonw/datasette-codespaces/issues",
        "CI": "https://github.com/simonw/datasette-codespaces/actions",
        "Changelog": "https://github.com/simonw/datasette-codespaces/releases",
    },
    license="Apache License, Version 2.0",
    classifiers=[
        "Framework :: Datasette",
        "License :: OSI Approved :: Apache Software License"
    ],
    version=VERSION,
    packages=["datasette_codespaces"],
    entry_points={"datasette": ["codespaces = datasette_codespaces"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio"]},
    python_requires=">=3.7",
)
