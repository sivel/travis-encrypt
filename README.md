# travis-encrypt

Encrypt strings for use in your Travis CI configuration files.

Contained here are 2 versions:

* [Python](python/)
* [Go](go/)

The ideas for this script come from [travis](https://github.com/travis-ci/travis) and [node-travis-encrypt](https://github.com/pwmckenna/node-travis-encrypt).

I didn't want to use either of the above as I don't use ruby and node, so I wrote a python version.  I also realize that some people don't use python either, so to bridge the gap I also wrote a version in Go.

## How to use encrypted data in Travis CI

See http://docs.travis-ci.com/user/encryption-keys/

## Python

```
usage: travis_encrypt.py [-h] [--version] -r REPO string

positional arguments:
  string                String to encrypt

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -r REPO, --repo REPO  Repository slug (:owner/:name)
```

## Go

```
usage: travis_encrypt --repo=owner/name string
    -h, --help            Show this help message and exit
    --version             Show program's version number and exit
    --repo REPO           Repository slug (:owner/:name)
    string                String to encrypt
```
