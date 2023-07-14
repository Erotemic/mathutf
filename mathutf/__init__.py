__version__ = '0.0.1'

from mathutf import symbols


def __getattr__(key):
    return symbols.SYMBOLS[key]


def __dir__():
    return ['symbols'] + list(symbols.SYMBOLS)
