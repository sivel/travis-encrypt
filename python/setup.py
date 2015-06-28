#!/usr/bin/env python


from setuptools import setup


def parse_requirements(filename="requirements.txt"):
    with open(filename, "r") as f:
        for line in f:
            if line and line[:2] not in ("#", "-e"):
                yield line.strip()


def main():
    setup(
        name="travis-encrypt",
        install_requires=list(parse_requirements()),
        scripts=["travis_encrypt.py"],
    )


if __name__ == "__main__":
    main()
