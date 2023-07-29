__version__ = '0.1.0'

from mathutf import symbols

from mathutf.symbols import search


def __getattr__(key):
    return symbols.SYMBOLS[key]


def __dir__():
    return __all__


__all__ = ['search', 'symbols']
__all__ += list(symbols.SYMBOLS)
