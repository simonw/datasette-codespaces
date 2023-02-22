# datasette-codespaces

[![PyPI](https://img.shields.io/pypi/v/datasette-codespaces.svg)](https://pypi.org/project/datasette-codespaces/)
[![Changelog](https://img.shields.io/github/v/release/simonw/datasette-codespaces?include_prereleases&label=changelog)](https://github.com/simonw/datasette-codespaces/releases)
[![Tests](https://github.com/simonw/datasette-codespaces/workflows/Test/badge.svg)](https://github.com/simonw/datasette-codespaces/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/datasette-codespaces/blob/main/LICENSE)

 Conveniences for running Datasette on GitHub Codespaces

## Installation

Install this plugin in the same environment as Datasette.

    datasette install datasette-codespaces

## Usage

Install this when you are using Datasette inside of GitHub Codespaces. It makes the following changes:

- All requests will be treated as the `root` actor provided Datasette is running inside Codespaces (detected through the presence of the `CODESPACE_NAME` environment variable). This should still be secure as GitHub restricts access to servers running in the Codespaces environment based on GitHub authentication.
- The [datasette-x-forwarded-host](https://datasette.io/plugins/datasette-x-forwarded-host) plugin will be installed, ensuring links to other pages within Datasette such as facet navigation work correctly.

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

    cd datasette-codespaces
    python3 -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
