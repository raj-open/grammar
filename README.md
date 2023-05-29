# Grammar #

This repository provides a meta-parser.
Its specific purpose is to provide methods to parse descriptions of formal languages commonly used in theoretical fields.

## Vision ##

We aim to provide the following:

- General methods, which build on existing lexers/parsers, to more easily create the bridge between descriptions of parsers and the tokenisers.
- The ability to import the methods used in this repository.
- Automated testing for quality assurance (this may however be developed after the existence of prototypes).
- Extendibility to other descriptions of formal languages.

## Dependencies ##

The methods in this repository build on the powerful [Lark](https://github.com/lark-parser/lark) parser,
which is a general purpose tool.
We will develop (and release) this for the moment in **python >=3.10**,
as that seems to be currently the most widely used version of python.

## Quick guide to usage ##

You need at least `python 3.10`. Install the package via

```bash
python3 -m pip install git+https://github.com/raj-open/grammar.git@main
```

Use the package as follows:

```py
from r_open_grammar import *;
# further explanation pending
```

See [examples/README.md](examples/README.md) for more information.
