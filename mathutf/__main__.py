# PYTHON_ARGCOMPLETE_OK
#!/usr/bin/env python3
import scriptconfig as scfg
import ubelt as ub


class MathUTFCLI(scfg.DataConfig):
    query = scfg.Value(None, help=ub.paragraph(
        '''
        if specified search for a symbol related to the query
        '''), position=1)

    @classmethod
    def main(cls, cmdline=1, **kwargs):
        """
        Example:
            >>> # xdoctest: +SKIP
            >>> from mathutf.__main__ import *  # NOQA
            >>> cmdline = 0
            >>> kwargs = dict()
            >>> cls = MainCLI
            >>> cls.main(cmdline=cmdline, **kwargs)
        """
        import rich
        config = cls.cli(cmdline=cmdline, data=kwargs, strict=True)
        rich.print('config = ' + ub.urepr(config, nl=1))

        if config.query is None:
            from mathutf.symbols import USEFUL_SYMBOLS
            print(ub.highlight_code(USEFUL_SYMBOLS, 'reStructuredText'))
        else:
            import mathutf
            results = list(mathutf.search(config.query))
            import pandas as pd
            import rich
            import rich.markup
            rich.print(rich.markup.escape(pd.DataFrame(results).to_string()))


__cli__ = MathUTFCLI
main = __cli__.main

if __name__ == '__main__':
    """

    CommandLine:
        python ~/code/mathutf/mathutf/__main__.py
        python -m mathutf.__main__
    """
    main()
