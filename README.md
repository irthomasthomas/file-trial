# file-trial

[![PyPI](https://img.shields.io/pypi/v/file-trial.svg)](https://pypi.org/project/file-trial/)
[![Changelog](https://img.shields.io/github/v/release/irthomasthomas/file-trial?include_prereleases&label=changelog)](https://github.com/irthomasthomas/file-trial/releases)
[![Tests](https://github.com/irthomasthomas/file-trial/workflows/Test/badge.svg)](https://github.com/irthomasthomas/file-trial/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/irthomasthomas/file-trial/blob/master/LICENSE)

Put your wayward files and obstinate directories on trial for their lives.

## Installation

Install this tool using `pip`:

    pip install file-trial

## Usage

For help, run:

    file-trial --help

You can also use:

    python -m file_trial --help

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd file-trial
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
