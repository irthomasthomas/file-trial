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
    name="file-trial",
    description="Put your wayward files and obstinate directories on trial for their lives.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="THOMAS_THOMAS",
    url="https://github.com/irthomasthomas/file-trial",
    project_urls={
        "Issues": "https://github.com/irthomasthomas/file-trial/issues",
        "CI": "https://github.com/irthomasthomas/file-trial/actions",
        "Changelog": "https://github.com/irthomasthomas/file-trial/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["file_trial"],
    entry_points="""
        [console_scripts]
        file-trial=file_trial.cli:cli
    """,
    install_requires=["click"],
    extras_require={
        "test": ["pytest"]
    },
    python_requires=">=3.7",
)
