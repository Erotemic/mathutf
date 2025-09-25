# PYTHON_ARGCOMPLETE_OK
#!/usr/bin/env python3
import scriptconfig as scfg
import ubelt as ub


class MathUTFCLI(scfg.DataConfig):
    query = scfg.Value(None, type=str, help=ub.paragraph(
        '''
        if specified search for a symbol related to the query
        '''), position=1)

    edit = scfg.Value(False, isflag=True, help=ub.paragraph(
        '''
        if true, then edit the definition file.
        '''))

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

        import mathutf

        if config.edit:
            import xdev
            xdev.editfile(mathutf.symbols)

        if config.query is None:
            from mathutf.symbols import USEFUL_SYMBOLS
            print(ub.highlight_code(USEFUL_SYMBOLS, 'reStructuredText'))
        else:
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
