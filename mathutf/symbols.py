# -*- coding: utf-8 -*-
"""
References:
    https://en.wikipedia.org/wiki/Mathematical_operators_and_symbols_in_Unicode

    https://www.quora.com/What-do-mathbb-C-mathbb-F-mathbb-H-mathbb-N-mathbb-Q-mathbb-R-mathbb-S-and-mathbb-Z-mean

    https://mathworld.wolfram.com/Doublestruck.html

    https://peterjamesthomas.com/maths-science/a-brief-taxonomy-of-numbers/

    http://xahlee.info/comp/unicode_math_operators.html

    https://www.vim.org/scripts/script.php?script_id=2566

    https://unicode-table.com/en/sets/superscript-and-subscript-letters/

"""
import ubelt as ub

TABLES = {}

TABLES['greek_letters'] = [
    {'chr': 'α', 'key': 'alpha', 'utf_name': 'GREEK SMALL LETTER ALPHA'},
    {'chr': 'β', 'key': 'beta', 'utf_name': 'GREEK SMALL LETTER BETA'},
    {'chr': 'γ', 'key': 'gamma', 'utf_name': 'GREEK SMALL LETTER GAMMA'},
    {'chr': 'δ', 'key': 'delta', 'utf_name': 'GREEK SMALL LETTER DELTA'},
    {'chr': 'ε', 'key': 'epsilon', 'utf_name': 'GREEK SMALL LETTER EPSILON'},
    {'chr': 'ζ', 'key': 'zeta', 'utf_name': 'GREEK SMALL LETTER ZETA'},
    {'chr': 'η', 'key': 'eta', 'utf_name': 'GREEK SMALL LETTER ETA'},
    {'chr': 'θ', 'key': 'theta', 'utf_name': 'GREEK SMALL LETTER THETA'},
    {'chr': 'ι', 'key': 'iota', 'utf_name': 'GREEK SMALL LETTER IOTA'},
    {'chr': 'κ', 'key': 'kappa', 'utf_name': 'GREEK SMALL LETTER KAPPA'},
    {'chr': 'λ', 'key': 'lam', 'utf_name': 'GREEK SMALL LETTER LAMDA'},
    {'chr': 'μ', 'key': 'mu', 'utf_name': 'GREEK SMALL LETTER MU'},
    {'chr': 'ν', 'key': 'nu', 'utf_name': 'GREEK SMALL LETTER NU'},
    {'chr': 'ξ', 'key': 'xi', 'utf_name': 'GREEK SMALL LETTER XI'},
    {'chr': 'ο', 'key': 'omicron', 'utf_name': 'GREEK SMALL LETTER OMICRON'},
    {'chr': 'π', 'key': 'pi', 'utf_name': 'GREEK SMALL LETTER PI'},
    {'chr': 'ρ', 'key': 'rho', 'utf_name': 'GREEK SMALL LETTER RHO'},
    {'chr': 'σ', 'key': 'sigma', 'utf_name': 'GREEK SMALL LETTER SIGMA'},
    {'chr': 'τ', 'key': 'tau', 'utf_name': 'GREEK SMALL LETTER TAU'},
    {'chr': 'υ', 'key': 'upsilon', 'utf_name': 'GREEK SMALL LETTER UPSILON'},
    {'chr': 'φ', 'key': 'phi', 'utf_name': 'GREEK SMALL LETTER PHI'},
    {'chr': 'χ', 'key': 'chip', 'utf_name': 'GREEK SMALL LETTER CHI'},
    {'chr': 'ψ', 'key': 'psi', 'utf_name': 'GREEK SMALL LETTER PSI'},
    {'chr': 'ω', 'key': 'omega', 'utf_name': 'GREEK SMALL LETTER OMEGA'},

    {'chr': 'Α', 'key': 'Alpha', 'utf_name': 'GREEK CAPITAL LETTER ALPHA'},
    {'chr': 'Β', 'key': 'Beta', 'utf_name': 'GREEK CAPITAL LETTER BETA'},
    {'chr': 'Γ', 'key': 'Gamma', 'utf_name': 'GREEK CAPITAL LETTER GAMMA'},
    {'chr': 'Δ', 'key': 'Delta', 'utf_name': 'GREEK CAPITAL LETTER DELTA'},
    {'chr': 'Ε', 'key': 'Epsilon', 'utf_name': 'GREEK CAPITAL LETTER EPSILON'},
    {'chr': 'Ζ', 'key': 'Zeta', 'utf_name': 'GREEK CAPITAL LETTER ZETA'},
    {'chr': 'Η', 'key': 'Eta', 'utf_name': 'GREEK CAPITAL LETTER ETA'},
    {'chr': 'Θ', 'key': 'Theta', 'utf_name': 'GREEK CAPITAL LETTER THETA'},
    {'chr': 'Ι', 'key': 'Iota', 'utf_name': 'GREEK CAPITAL LETTER IOTA'},
    {'chr': 'Κ', 'key': 'Kappa', 'utf_name': 'GREEK CAPITAL LETTER KAPPA'},
    {'chr': 'Λ', 'key': 'Lambda', 'utf_name': 'GREEK CAPITAL LETTER LAMDA'},
    {'chr': 'Μ', 'key': 'Mu', 'utf_name': 'GREEK CAPITAL LETTER MU'},
    {'chr': 'Ν', 'key': 'Nu', 'utf_name': 'GREEK CAPITAL LETTER NU'},
    {'chr': 'Ξ', 'key': 'Xi', 'utf_name': 'GREEK CAPITAL LETTER XI'},
    {'chr': 'Ο', 'key': 'Omicron', 'utf_name': 'GREEK CAPITAL LETTER OMICRON'},
    {'chr': 'Π', 'key': 'Pi', 'utf_name': 'GREEK CAPITAL LETTER PI'},
    {'chr': 'Ρ', 'key': 'Rho', 'utf_name': 'GREEK CAPITAL LETTER RHO'},
    {'chr': 'Σ', 'key': 'Sigma', 'utf_name': 'GREEK CAPITAL LETTER SIGMA'},
    {'chr': 'Τ', 'key': 'Tau', 'utf_name': 'GREEK CAPITAL LETTER TAU'},
    {'chr': 'Υ', 'key': 'Upsilon', 'utf_name': 'GREEK CAPITAL LETTER UPSILON'},
    {'chr': 'Φ', 'key': 'Phi', 'utf_name': 'GREEK CAPITAL LETTER PHI'},
    {'chr': 'Χ', 'key': 'Chi', 'utf_name': 'GREEK CAPITAL LETTER CHI'},
    {'chr': 'Ψ', 'key': 'Psi', 'utf_name': 'GREEK CAPITAL LETTER PSI'},
    {'chr': 'Ω', 'key': 'Omega', 'utf_name': 'GREEK CAPITAL LETTER OMEGA'},

    {'chr': 'ς', 'key': 'alt_sigma', 'utf_name': 'GREEK SMALL LETTER FINAL SIGMA'},
    {'chr': '𝜏', 'key': 'alt_tau', 'utf_name': 'MATHEMATICAL ITALIC SMALL TAU'},
]

TABLES['subscripts'] = [
    {'chr': '₀', 'key': 'sub_0', 'utf_name': 'SUBSCRIPT ZERO'},
    {'chr': '₁', 'key': 'sub_1', 'utf_name': 'SUBSCRIPT ONE'},
    {'chr': '₂', 'key': 'sub_2', 'utf_name': 'SUBSCRIPT TWO'},
    {'chr': '₃', 'key': 'sub_3', 'utf_name': 'SUBSCRIPT THREE'},
    {'chr': '₄', 'key': 'sub_4', 'utf_name': 'SUBSCRIPT FOUR'},
    {'chr': '₅', 'key': 'sub_5', 'utf_name': 'SUBSCRIPT FIVE'},
    {'chr': '₆', 'key': 'sub_6', 'utf_name': 'SUBSCRIPT SIX'},
    {'chr': '₇', 'key': 'sub_7', 'utf_name': 'SUBSCRIPT SEVEN'},
    {'chr': '₈', 'key': 'sub_8', 'utf_name': 'SUBSCRIPT EIGHT'},
    {'chr': '₉', 'key': 'sub_9', 'utf_name': 'SUBSCRIPT NINE'},

    {'chr': '₊', 'key': 'sub_plus', 'utf_name': 'SUBSCRIPT PLUS SIGN'},
    {'chr': '₋', 'key': 'sub_minus', 'utf_name': 'SUBSCRIPT MINUS'},
    {'chr': '₌', 'key': 'sub_eq', 'utf_name': 'SUBSCRIPT EQUALS SIGN'},

    {'chr': '₍', 'key': 'sub_lparen', 'utf_name': 'SUBSCRIPT LEFT PARENTHESIS'},
    {'chr': '₎', 'key': 'sub_rparen', 'utf_name': 'SUBSCRIPT RIGHT PARENTHESIS'},

    {'chr': 'ᵢ', 'key': 'sub_i', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER I'},
    {'chr': 'ᵣ', 'key': 'sub_r', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER R'},
    {'chr': 'ᵤ', 'key': 'sub_u', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER U'},
    {'chr': 'ᵥ', 'key': 'sub_v', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER V'},
    {'chr': 'ₐ', 'key': 'sub_a', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER A'},
    {'chr': 'ₑ', 'key': 'sub_e', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER E'},
    {'chr': 'ₒ', 'key': 'sub_o', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER O'},
    {'chr': 'ₓ', 'key': 'sub_x', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER X'},
    {'chr': 'ₕ', 'key': 'sub_h', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER H'},
    {'chr': 'ₖ', 'key': 'sub_k', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER K'},
    {'chr': 'ₗ', 'key': 'sub_l', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER L'},
    {'chr': 'ₘ', 'key': 'sub_m', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER M'},
    {'chr': 'ₙ', 'key': 'sub_n', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER N'},
    {'chr': 'ₚ', 'key': 'sub_p', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER P'},
    {'chr': 'ₛ', 'key': 'sub_s', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER S'},
    {'chr': 'ₜ', 'key': 'sub_t', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER T'},
    {'chr': 'ⱼ', 'key': 'sub_j', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER J'},

    {'chr': 'ᵦ', 'key': 'sub_beta', 'utf_name': 'GREEK SUBSCRIPT SMALL LETTER BETA'},
    {'chr': 'ᵧ', 'key': 'sub_gamma', 'utf_name': 'GREEK SUBSCRIPT SMALL LETTER GAMMA'},
    {'chr': 'ᵨ', 'key': 'sub_rho', 'utf_name': 'GREEK SUBSCRIPT SMALL LETTER RHO'},
    {'chr': 'ᵩ', 'key': 'sub_phi', 'utf_name': 'GREEK SUBSCRIPT SMALL LETTER PHI'},
    {'chr': 'ᵪ', 'key': 'sub_chi', 'utf_name': 'GREEK SUBSCRIPT SMALL LETTER CHI'},

    {'chr': 'ₔ', 'key': 'sub_schwa', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER SCHWA'},
    {'chr': '⨧', 'key': 'plus_with_sub_2', 'utf_name': 'PLUS SIGN WITH SUBSCRIPT TWO'},
]

TABLES['superscripts'] = [
    {'chr': '²', 'key': 'sup_2', 'utf_name': 'SUPERSCRIPT TWO'},
    {'chr': '³', 'key': 'sup_3', 'utf_name': 'SUPERSCRIPT THREE'},
    {'chr': '¹', 'key': 'sup_1', 'utf_name': 'SUPERSCRIPT ONE'},
    {'chr': '⁰', 'key': 'sup_0', 'utf_name': 'SUPERSCRIPT ZERO'},
    {'chr': '⁴', 'key': 'sup_4', 'utf_name': 'SUPERSCRIPT FOUR'},
    {'chr': '⁵', 'key': 'sup_5', 'utf_name': 'SUPERSCRIPT FIVE'},
    {'chr': '⁶', 'key': 'sup_6', 'utf_name': 'SUPERSCRIPT SIX'},
    {'chr': '⁷', 'key': 'sup_7', 'utf_name': 'SUPERSCRIPT SEVEN'},
    {'chr': '⁸', 'key': 'sup_8', 'utf_name': 'SUPERSCRIPT EIGHT'},
    {'chr': '⁹', 'key': 'sup_9', 'utf_name': 'SUPERSCRIPT NINE'},
    {'chr': '⁺', 'key': 'sup_plus', 'utf_name': 'SUPERSCRIPT PLUS SIGN'},
    {'chr': '⁻', 'key': 'sup_minus', 'utf_name': 'SUPERSCRIPT MINUS'},
    {'chr': '⁼', 'key': 'sup_eq', 'utf_name': 'SUPERSCRIPT EQUALS SIGN'},
    {'chr': '⁽', 'key': 'sup_lparen', 'utf_name': 'SUPERSCRIPT LEFT PARENTHESIS'},
    {'chr': '⁾', 'key': 'sup_rparen', 'utf_name': 'SUPERSCRIPT RIGHT PARENTHESIS'},
    {'chr': 'ⁿ', 'key': 'sup_n', 'utf_name': 'SUPERSCRIPT LATIN SMALL LETTER N'},
    {'chr': 'ⁱ', 'key': 'sup_i', 'utf_name': 'SUPERSCRIPT LATIN SMALL LETTER I'},
]

TABLES['quantifiers'] = [
    {'chr': '∈', 'key': 'elementof', 'utf_name': 'ELEMENT OF'},
    {'chr': '∉', 'key': 'not_elementof', 'utf_name': 'NOT AN ELEMENT OF'},
    # {'chr': '∊', 'key': 'small_element_of', 'utf_name': 'SMALL ELEMENT OF'},
    # {'chr': 'ϵ', 'key': 'lunate_epsilon', 'utf_name': 'GREEK LUNATE EPSILON SYMBOL'},

    {'chr': '∀', 'key': 'forall', 'utf_name': 'FOR ALL'},
    {'chr': '∃', 'key': 'exists', 'utf_name': 'THERE EXISTS'},
    {'chr': '∄', 'key': 'not_exists', 'utf_name': 'THERE DOES NOT EXIST'},
]

TABLES['numeric_sets'] = [
    {'chr': '𝔽', 'key': 'finitefield', 'utf_name': 'MATHEMATICAL DOUBLE-STRUCK CAPITAL F'},
    {'chr': 'ℕ', 'key': 'natural', 'utf_name': 'DOUBLE-STRUCK CAPITAL N'},
    {'chr': '∫', 'key': 'integral', 'utf_name': 'INTEGRAL'},
    {'chr': 'ℚ', 'key': 'rational', 'utf_name': 'DOUBLE-STRUCK CAPITAL Q'},
    {'chr': 'ℂ', 'key': 'complex', 'utf_name': 'DOUBLE-STRUCK CAPITAL C'},
    {'chr': 'ℍ', 'key': 'quaternion', 'utf_name': 'DOUBLE-STRUCK CAPITAL H'},
    {'chr': '𝕆', 'key': 'octernion', 'utf_name': 'MATHEMATICAL DOUBLE-STRUCK CAPITAL O'},
    {'chr': 'ℙ', 'key': 'irrational', 'utf_name': 'DOUBLE-STRUCK CAPITAL P'},
    {'chr': 'ℝ', 'key': 'real', 'utf_name': 'DOUBLE-STRUCK CAPITAL R'},
    {'chr': '𝟙', 'key': 'ones', 'utf_name': 'MATHEMATICAL DOUBLE-STRUCK DIGIT ONE'},
    {'chr': '∅', 'key': 'emptyset', 'utf_name': 'EMPTY SET'},
    # floating    = '𝕃'  # proposed
]

TABLES['set_operators'] = [
    {'chr': '∖', 'key': 'setdiff', 'utf_name': 'SET MINUS'},
    {'chr': '⊂', 'key': 'subset', 'utf_name': 'SUBSET OF'},
    {'chr': '⊃', 'key': 'supset', 'utf_name': 'SUPERSET OF'},
    {'chr': '⊆', 'key': 'subset_eq', 'utf_name': 'SUBSET OF OR EQUAL TO'},
    {'chr': '⊇', 'key': 'supset_eq', 'utf_name': 'SUPERSET OF OR EQUAL TO'},
    {'chr': '⊊', 'key': 'subset_eq', 'utf_name': 'SUBSET OF WITH NOT EQUAL TO'},
    {'chr': '⊋', 'key': 'supset_neq', 'utf_name': 'SUPERSET OF WITH NOT EQUAL TO'},
    {'chr': '∩', 'key': 'isect', 'utf_name': 'INTERSECTION', 'alias': ['cup']},
    {'chr': '∪', 'key': 'union', 'utf_name': 'UNION', 'alias': ['cap']},

    {'chr': '⊉', 'key': 'subset_not_ge', 'utf_name': 'NEITHER A SUPERSET OF NOR EQUAL TO'},
    {'chr': '⊅', 'key': 'subset_not_gt', 'utf_name': 'NOT A SUPERSET OF'},
    {'chr': '⊄', 'key': 'subset_not_lt', 'utf_name': 'NOT A SUBSET OF'},
    {'chr': '⊈', 'key': 'subset_not_le', 'utf_name': 'NEITHER A SUBSET OF NOR EQUAL TO'},

]

TABLES['relational'] = [
    {'chr': '≦', 'key': 'le', 'utf_name': 'LESS-THAN OVER EQUAL TO'},
    {'chr': '≥', 'key': 'ge', 'utf_name': 'GREATER-THAN OR EQUAL TO'},

    {'chr': '<', 'key': 'lt', 'utf_name': 'LESS-THAN SIGN'},
    {'chr': '>', 'key': 'gt', 'utf_name': 'GREATER-THAN SIGN'},

    {'chr': '=', 'key': 'eq', 'utf_name': 'EQUALS SIGN'},
    {'chr': '≠', 'key': 'ne', 'utf_name': 'NOT EQUAL TO'},

    {'chr': '≈', 'key': 'approx_eq', 'utf_name': 'ALMOST EQUAL TO'},
    {'chr': '≇', 'key': 'not_approx', 'utf_name': 'NEITHER APPROXIMATELY NOR ACTUALLY EQUAL TO'},
    {'chr': '≆', 'key': 'approx_ne', 'utf_name': 'APPROXIMATELY BUT NOT ACTUALLY EQUAL TO'},

    {'chr': '∝', 'key': 'propor', 'utf_name': 'PROPORTIONAL TO'},

    {'chr': '≡', 'key': 'equiv', 'utf_name': 'IDENTICAL TO'},
    {'chr': '≢', 'key': 'not_equiv', 'utf_name': 'NOT IDENTICAL TO'},

    {'chr': '≅', 'key': 'cong', 'utf_name': 'APPROXIMATELY EQUAL TO'},
    {'chr': '≔', 'key': 'doteq', 'utf_name': 'COLON EQUALS'},
    {'chr': '≕', 'key': 'eqdot', 'utf_name': 'EQUALS COLON'},
]

TABLES['numeric_operators'] = [
    {'chr': '±', 'key': 'pm', 'utf_name': 'PLUS-MINUS SIGN'},
    {'chr': '√', 'key': 'square_root', 'utf_name': 'SQUARE ROOT'},
    {'chr': '∛', 'key': 'cube_root', 'utf_name': 'CUBE ROOT'},
    {'chr': '∜', 'key': 'quad_root', 'utf_name': 'FOURTH ROOT'},
]

TABLES['other_operators'] = [
    {'chr': '⋅', 'key': 'cdot', 'utf_name': 'DOT OPERATOR'},
    {'chr': '∘', 'key': 'circ', 'utf_name': 'RING OPERATOR'},
    {'chr': '×', 'key': 'times', 'utf_name': 'MULTIPLICATION SIGN'},
    {'chr': '⊕', 'key': 'oplus', 'utf_name': 'CIRCLED PLUS'},
]


TABLES['nary'] = [
    {'chr': '∏', 'key': 'nary_prod', 'utf_name': 'N-ARY PRODUCT'},
    {'chr': '∑', 'key': 'nary_sum', 'utf_name': 'N-ARY SUMMATION'},
    {'chr': '⋂', 'key': 'nary_isect', 'utf_name': 'N-ARY INTERSECTION'},
    {'chr': '⋃', 'key': 'nary_union', 'utf_name': 'N-ARY UNION'},
]


TABLES['arrows'] = [
    {'chr': '→', 'key': 'right_arrow', 'utf_name': 'RIGHTWARDS ARROW'},
    {'chr': '←', 'key': 'left_arrow', 'utf_name': 'LEFTWARDS ARROW'},
    {'chr': '←', 'key': 'bidir_arrow', 'utf_name': 'LEFTWARDS ARROW'},
    {'chr': '⇒', 'key': 'right_darrow', 'utf_name': 'RIGHTWARDS DOUBLE ARROW'},
    {'chr': '⇐', 'key': 'left_darrow', 'utf_name': 'LEFTWARDS DOUBLE ARROW'},
    {'chr': '⇔', 'key': 'bidir_darrow', 'utf_name': 'LEFT RIGHT DOUBLE ARROW'},
]


TABLES['logic'] = [
    {'chr': '∧', 'key': 'and', 'utf_name': 'LOGICAL AND'},
    {'chr': '∨', 'key': 'or', 'utf_name': 'LOGICAL OR'},
    {'chr': '¬', 'key': 'not', 'utf_name': 'NOT SIGN'},
]

TABLES['calclus'] = [
    {'chr': '∫', 'key': 'int', 'utf_name': 'INTEGRAL'},
    {'chr': '∂', 'key': 'partial', 'utf_name': 'PARTIAL DIFFERENTIAL'},
    {'chr': '∆', 'key': 'delta_upper', 'utf_name': 'INCREMENT'},
]

TABLES['proof'] = [
    {'chr': '∴', 'key': 'therefore', 'utf_name': 'THEREFORE'},
    {'chr': '∎', 'key': 'qed', 'utf_name': 'END OF PROOF'},
]

TABLES['nesting'] = [
    {'chr': '⟨', 'key': 'langle', 'utf_name': 'MATHEMATICAL LEFT ANGLE BRACKET'},
    {'chr': '⟩', 'key': 'rangle', 'utf_name': 'MATHEMATICAL RIGHT ANGLE BRACKET'},
]

TABLES['misc'] = [
    {'chr': '⊥', 'key': 'perp', 'utf_name': 'UP TACK'},
    {'chr': '…', 'key': 'ldots', 'utf_name': 'HORIZONTAL ELLIPSIS'},
    {'chr': '⋯', 'key': 'cdots', 'utf_name': 'MIDLINE HORIZONTAL ELLIPSIS'},
    {'chr': '⋈', 'key': 'join', 'utf_name': 'BOWTIE'},
    {'chr': '∞', 'key': 'infinity', 'utf_name': 'INFINITY', 'alias': ['infty']},
]


SYMBOLS = {}


def _populate_class():
    import keyword
    for table_name, subtable in TABLES.items():
        for item in subtable:
            key = item['key']
            if keyword.iskeyword(key):
                key = key + '_'
            SYMBOLS[key] = item['chr']
            # setattr(MathSymbols, key, item['chr'])


_populate_class()


def _query_unicode():
    import unicodedata
    all_items = []
    for table_name, subtable in TABLES.items():
        for item in subtable:
            v = item['chr']
            all_items.append(item)
            utf_name = unicodedata.name(v)
            assert item['utf_name'] == utf_name
            print('{},'.format(ub.repr2(item, nl=0)))

    import pandas as pd
    print(pd.DataFrame(all_items).to_string())

    dups = ub.find_duplicates(all_items, key=lambda x: x['chr'])

    key_to_num = {}
    for chr_ in '0123456789':
        key = unicodedata.name(chr_).replace('DIGIT ', '').lower()
        key_to_num[key] = chr_

    import re
    set_related = re.compile('\\b(SUPERSET|SUBSET|SET)\\b')

    for i in range(1, 100000000):
        try:
            chr_ = chr(i)
            utf_name = unicodedata.name(chr_)
            key = utf_name.replace('-', '_').replace(' ', '_').lower()
            found = False
            # if 'MATHEMATICAL' in name:
            #     print('{}'.format(ub.repr2(item, nl=0)))

            key = key.replace('equal', 'eq')
            if set_related.match(utf_name):
                found = 0
                key = key.replace('_of', '')
                key = key.replace('_to', '')
                key = key.replace('_or', '')

            if 'SUPERSCRIPT' in utf_name:
                found = 0
                key = key.replace('latin_', '')
                key = key.replace('greek_', '')
                key = key.replace('subscript', 'sub')
                key = key.replace('superscript', 'sup')
                key = key.replace('small_letter_', '')
                key = key.replace('_sign', '')
                key = key.replace('parenthesis', 'paren')
                key = key.replace('left_paren', 'lparen')
                key = key.replace('right_paren', 'rparen')
                key = key.replace('plus_with_sub_2', 'plus_sub_2')
                key = key.replace('arabic_sub_alef', 'sub_alef')
                for s, r in key_to_num.items():
                    key = key.replace(s, r)

            if 'SUBSCRIPT' in utf_name:
                found = 0
                key = key.replace('latin_', '')
                key = key.replace('greek_', '')
                key = key.replace('subscript', 'sub')
                key = key.replace('small_letter_', '')
                key = key.replace('_sign', '')
                key = key.replace('parenthesis', 'paren')
                key = key.replace('left_paren', 'lparen')
                key = key.replace('right_paren', 'rparen')
                key = key.replace('plus_with_sub_2', 'plus_sub_2')
                key = key.replace('arabic_sub_alef', 'sub_alef')
                for s, r in key_to_num.items():
                    key = key.replace(s, r)

            if 'ELEMENT OF' in utf_name:
                found = 1
            # if 'LOGICAL' in utf_name:
            #     print('{}'.format(ub.repr2(item, nl=0)))
            if found:
                item = {
                    'chr': chr_,
                    'utf_name': utf_name,
                    'key': key,
                }
                print('{},'.format(ub.repr2(item, nl=0)))
        except Exception:
            pass
