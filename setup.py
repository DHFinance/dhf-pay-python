import re
from pathlib import Path

from setuptools import setup, find_packages

install_requires = ["marshmallow>=3.14.1", "requests>=2.27.1"]


def read(*parts):
    return Path(__file__).resolve().parent.joinpath(*parts).read_text().strip()


def read_version():
    regexp = re.compile(r"^__version__\W*=\W*\"([\d.abrc]+)\"")
    for line in read("dhf_wrapper", "__init__.py").splitlines():
        match = regexp.match(line)
        if match is not None:
            return match.group(1)

    raise RuntimeError("Cannot find version in dhf_wrapper/__init__.py")


classifiers = [
    "License :: OSI Approved :: BSD License",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Operating System :: POSIX",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: Microsoft :: Windows",
    "Environment :: Web Environment",
    "Development Status :: 5 - Production/Stable",
    "Topic :: SDK",
]

setup(
    name="dhf-sdk",
    version=read_version(),
    description="API wrapper for DHFinance.",
    long_description="\n\n".join((read("README.md"))),
    long_description_content_type="text/markdown",
    classifiers=classifiers,
    platforms=["macOS", "POSIX", "Windows"],
    author="Andrew Svetlov",
    python_requires=">=3.6",
    project_urls={
        "GitHub": "https://github.com/DHFinance",
    },
    license="MIT",
    packages=find_packages(),
    install_requires=install_requires,
    include_package_data=True,
)
