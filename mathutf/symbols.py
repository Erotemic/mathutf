# -*- coding: utf-8 -*-
"""
References:
    https://en.wikipedia.org/wiki/Mathematical_operators_and_symbols_in_Unicode

    https://en.wikipedia.org/wiki/Glossary_of_mathematical_symbols

    https://www.quora.com/What-do-mathbb-C-mathbb-F-mathbb-H-mathbb-N-mathbb-Q-mathbb-R-mathbb-S-and-mathbb-Z-mean

    https://mathworld.wolfram.com/Doublestruck.html

    https://peterjamesthomas.com/maths-science/a-brief-taxonomy-of-numbers/

    http://xahlee.info/comp/unicode_math_operators.html

    https://www.vim.org/scripts/script.php?script_id=2566

    https://unicode-table.com/en/sets/superscript-and-subscript-letters/

    https://github.com/fKunstner/latex-to-utf8/blob/master/map.js
"""
import ubelt as ub


# From /r/mathmemes Useful Symbol Sidebar
USEFUL_SYMBOLS = """
Basic Math Symbols
------------------

≠ ± ∓ ÷ × ∙ – √ ‰ ⊗ ⊕ ⊖ ⊘ ⊙ ≤ ≥ ≦ ≧ ≨ ≩ ≺ ≻ ≼ ≽ ⊏ ⊐ ⊑ ⊒ ² ³ °


Geometry Symbols
----------------

∠ ∟ ° ≅ ~ ‖ ⟂ ⫛


Algebra Symbols
---------------

≡ ≜ ≈ ∝ ∞ ≪ ≫ ⌊⌋ ⌈⌉ ∘∏ ∐ ∑ ⋀ ⋁ ⋂ ⋃ ⨀ ⨁ ⨂ 𝖕 𝖖 𝖗


Set Theory Symbols
------------------

∅ ∖ ∁ ↦ ↣ ∩ ∪ ⊆ ⊂ ⊄ ⊊ ⊇ ⊃ ⊅ ⊋ ⊖ ∈ ∉ ∋ ∌ ℕ ℤ ℚ ℝ ℂ ℵ ℶ ℷ ℸ 𝓟


Logic Symbols
-------------

¬ ∨ ∧ ⊕ → ← ⇒ ⇐ ↔ ⇔ ∀ ∃ ∄ ∴ ∵ ⊤ ⊥ ⊢ ⊨ ⫤ ⊣


Calculus and Analysis Symbols
-----------------------------

∫ ∬ ∭ ∮ ∯ ∰ ∇ ∆ δ ∂ ℱ ℒ ℓ


Greek Letters
-------------

𝛢𝛼 𝛣𝛽 𝛤𝛾 𝛥𝛿 𝛦𝜀𝜖 𝛧𝜁 𝛨𝜂 𝛩𝜃𝜗 𝛪𝜄 𝛫𝜅 𝛬𝜆 𝛭𝜇 𝛮𝜈 𝛯𝜉 𝛰𝜊 𝛱𝜋 𝛲𝜌 𝛴𝜎 𝛵𝜏 𝛶𝜐 𝛷𝜙𝜑 𝛸𝜒 𝛹𝜓 𝛺𝜔
"""

TABLES = {}

TABLES['greek_letters'] = [
    {'chr': 'α', 'key': 'alpha', 'utf_name': 'GREEK SMALL LETTER ALPHA', 'tex': '\\alpha'},
    {'chr': 'β', 'key': 'beta', 'utf_name': 'GREEK SMALL LETTER BETA', 'tex': '\\beta'},
    {'chr': 'γ', 'key': 'gamma', 'utf_name': 'GREEK SMALL LETTER GAMMA', 'tex': '\\gamma'},
    {'chr': 'δ', 'key': 'delta', 'utf_name': 'GREEK SMALL LETTER DELTA', 'tex': '\\delta'},
    {'chr': 'ε', 'key': 'epsilon', 'utf_name': 'GREEK SMALL LETTER EPSILON', 'tex': '\\epsilon'},
    {'chr': 'ζ', 'key': 'zeta', 'utf_name': 'GREEK SMALL LETTER ZETA', 'tex': '\\zeta'},
    {'chr': 'η', 'key': 'eta', 'utf_name': 'GREEK SMALL LETTER ETA', 'tex': '\\eta'},
    {'chr': 'θ', 'key': 'theta', 'utf_name': 'GREEK SMALL LETTER THETA', 'tex': '\\theta'},
    {'chr': 'ι', 'key': 'iota', 'utf_name': 'GREEK SMALL LETTER IOTA', 'tex': '\\iota'},
    {'chr': 'κ', 'key': 'kappa', 'utf_name': 'GREEK SMALL LETTER KAPPA', 'tex': '\\kappa'},
    {'chr': 'λ', 'key': 'lam', 'utf_name': 'GREEK SMALL LETTER LAMDA', 'tex': '\\lambda'},
    {'chr': 'μ', 'key': 'mu', 'utf_name': 'GREEK SMALL LETTER MU', 'tex': '\\mu'},
    {'chr': 'ν', 'key': 'nu', 'utf_name': 'GREEK SMALL LETTER NU', 'tex': '\\nu'},
    {'chr': 'ξ', 'key': 'xi', 'utf_name': 'GREEK SMALL LETTER XI', 'tex': '\\xi'},
    {'chr': 'ο', 'key': 'omicron', 'utf_name': 'GREEK SMALL LETTER OMICRON', 'tex': '\\omicron'},
    {'chr': 'π', 'key': 'pi', 'utf_name': 'GREEK SMALL LETTER PI', 'tex': '\\pi'},
    {'chr': 'ρ', 'key': 'rho', 'utf_name': 'GREEK SMALL LETTER RHO', 'tex': '\\rho'},
    {'chr': 'σ', 'key': 'sigma', 'utf_name': 'GREEK SMALL LETTER SIGMA', 'tex': '\\sigma'},
    {'chr': 'τ', 'key': 'tau', 'utf_name': 'GREEK SMALL LETTER TAU', 'tex': '\\tau'},
    {'chr': 'υ', 'key': 'upsilon', 'utf_name': 'GREEK SMALL LETTER UPSILON', 'tex': '\\upsilon'},
    {'chr': 'φ', 'key': 'phi', 'utf_name': 'GREEK SMALL LETTER PHI', 'tex': '\\varphi'},
    {'chr': 'χ', 'key': 'chip', 'utf_name': 'GREEK SMALL LETTER CHI', 'tex': '\\chi'},
    {'chr': 'ψ', 'key': 'psi', 'utf_name': 'GREEK SMALL LETTER PSI', 'tex': '\\psi'},
    {'chr': 'ω', 'key': 'omega', 'utf_name': 'GREEK SMALL LETTER OMEGA', 'tex': '\\omega'},

    {'chr': 'Α', 'key': 'Alpha', 'utf_name': 'GREEK CAPITAL LETTER ALPHA', 'tex': '\\Alpha'},
    {'chr': 'Β', 'key': 'Beta', 'utf_name': 'GREEK CAPITAL LETTER BETA', 'tex': '\\Beta'},
    {'chr': 'Γ', 'key': 'Gamma', 'utf_name': 'GREEK CAPITAL LETTER GAMMA', 'tex': '\\Gamma'},
    {'chr': 'Δ', 'key': 'Delta', 'utf_name': 'GREEK CAPITAL LETTER DELTA', 'tex': '\\Delta'},
    {'chr': 'Ε', 'key': 'Epsilon', 'utf_name': 'GREEK CAPITAL LETTER EPSILON', 'tex': '\\Epsilon'},
    {'chr': 'Ζ', 'key': 'Zeta', 'utf_name': 'GREEK CAPITAL LETTER ZETA', 'tex': '\\Zeta'},
    {'chr': 'Η', 'key': 'Eta', 'utf_name': 'GREEK CAPITAL LETTER ETA', 'tex': '\\Eta'},
    {'chr': 'Θ', 'key': 'Theta', 'utf_name': 'GREEK CAPITAL LETTER THETA', 'tex': '\\Theta'},
    {'chr': 'Ι', 'key': 'Iota', 'utf_name': 'GREEK CAPITAL LETTER IOTA', 'tex': '\\Iota'},
    {'chr': 'Κ', 'key': 'Kappa', 'utf_name': 'GREEK CAPITAL LETTER KAPPA', 'tex': '\\Kappa'},
    {'chr': 'Λ', 'key': 'Lambda', 'utf_name': 'GREEK CAPITAL LETTER LAMDA', 'tex': '\\Lambda'},
    {'chr': 'Μ', 'key': 'Mu', 'utf_name': 'GREEK CAPITAL LETTER MU', 'tex': '\\Mu'},
    {'chr': 'Ν', 'key': 'Nu', 'utf_name': 'GREEK CAPITAL LETTER NU', 'tex': '\\Nu'},
    {'chr': 'Ξ', 'key': 'Xi', 'utf_name': 'GREEK CAPITAL LETTER XI', 'tex': '\\Xi'},
    {'chr': 'Ο', 'key': 'Omicron', 'utf_name': 'GREEK CAPITAL LETTER OMICRON', 'tex': '\\Omicron'},
    {'chr': 'Π', 'key': 'Pi', 'utf_name': 'GREEK CAPITAL LETTER PI', 'tex': '\\Pi'},
    {'chr': 'Ρ', 'key': 'Rho', 'utf_name': 'GREEK CAPITAL LETTER RHO', 'tex': '\\Rho'},
    {'chr': 'Σ', 'key': 'Sigma', 'utf_name': 'GREEK CAPITAL LETTER SIGMA', 'tex': '\\Sigma'},
    {'chr': 'Τ', 'key': 'Tau', 'utf_name': 'GREEK CAPITAL LETTER TAU', 'tex': '\\Tau'},
    {'chr': 'Υ', 'key': 'Upsilon', 'utf_name': 'GREEK CAPITAL LETTER UPSILON', 'tex': '\\Upsilon'},
    {'chr': 'Φ', 'key': 'Phi', 'utf_name': 'GREEK CAPITAL LETTER PHI', 'tex': '\\Phi'},
    {'chr': 'Χ', 'key': 'Chi', 'utf_name': 'GREEK CAPITAL LETTER CHI', 'tex': '\\Chi'},
    {'chr': 'Ψ', 'key': 'Psi', 'utf_name': 'GREEK CAPITAL LETTER PSI', 'tex': '\\Psi'},
    {'chr': 'Ω', 'key': 'Omega', 'utf_name': 'GREEK CAPITAL LETTER OMEGA', 'tex': '\\Omega'},

    {'chr': 'ς', 'key': 'alt_sigma', 'utf_name': 'GREEK SMALL LETTER FINAL SIGMA', 'tex': '\\upvarsigma'},
    {'chr': '𝜏', 'key': 'alt_tau', 'utf_name': 'MATHEMATICAL ITALIC SMALL TAU', 'tex': '\\mittau'},
]

TABLES['subscripts'] = [
    {'chr': '₀', 'key': 'sub_0', 'utf_name': 'SUBSCRIPT ZERO', 'tex': '_0'},
    {'chr': '₁', 'key': 'sub_1', 'utf_name': 'SUBSCRIPT ONE', 'tex': '_1'},
    {'chr': '₂', 'key': 'sub_2', 'utf_name': 'SUBSCRIPT TWO', 'tex': '_2'},
    {'chr': '₃', 'key': 'sub_3', 'utf_name': 'SUBSCRIPT THREE', 'tex': '_3'},
    {'chr': '₄', 'key': 'sub_4', 'utf_name': 'SUBSCRIPT FOUR', 'tex': '_4'},
    {'chr': '₅', 'key': 'sub_5', 'utf_name': 'SUBSCRIPT FIVE', 'tex': '_5'},
    {'chr': '₆', 'key': 'sub_6', 'utf_name': 'SUBSCRIPT SIX', 'tex': '_6'},
    {'chr': '₇', 'key': 'sub_7', 'utf_name': 'SUBSCRIPT SEVEN', 'tex': '_7'},
    {'chr': '₈', 'key': 'sub_8', 'utf_name': 'SUBSCRIPT EIGHT', 'tex': '_8'},
    {'chr': '₉', 'key': 'sub_9', 'utf_name': 'SUBSCRIPT NINE', 'tex': '_9'},

    {'chr': '₊', 'key': 'sub_plus', 'utf_name': 'SUBSCRIPT PLUS SIGN', 'tex': '_+'},
    {'chr': '₋', 'key': 'sub_minus', 'utf_name': 'SUBSCRIPT MINUS', 'tex': '_-'},
    {'chr': '₌', 'key': 'sub_eq', 'utf_name': 'SUBSCRIPT EQUALS SIGN', 'tex': '_='},

    {'chr': '₍', 'key': 'sub_lparen', 'utf_name': 'SUBSCRIPT LEFT PARENTHESIS', 'tex': '_('},
    {'chr': '₎', 'key': 'sub_rparen', 'utf_name': 'SUBSCRIPT RIGHT PARENTHESIS', 'tex': '_)'},

    {'chr': 'ᵢ', 'key': 'sub_i', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER I', 'tex': '_i'},
    {'chr': 'ᵣ', 'key': 'sub_r', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER R', 'tex': '_r'},
    {'chr': 'ᵤ', 'key': 'sub_u', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER U', 'tex': '_u'},
    {'chr': 'ᵥ', 'key': 'sub_v', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER V', 'tex': '_v'},

    {'chr': 'ₐ', 'key': 'sub_a', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER A', 'tex': '_a'},
    {'chr': 'ₑ', 'key': 'sub_e', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER E', 'tex': '_e'},
    {'chr': 'ₒ', 'key': 'sub_o', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER O', 'tex': '_o'},
    {'chr': 'ₓ', 'key': 'sub_x', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER X', 'tex': '_x'},
    {'chr': 'ₕ', 'key': 'sub_h', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER H', 'tex': '_h'},
    {'chr': 'ₖ', 'key': 'sub_k', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER K', 'tex': '_k'},
    {'chr': 'ₗ', 'key': 'sub_l', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER L', 'tex': '_l'},
    {'chr': 'ₘ', 'key': 'sub_m', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER M', 'tex': '_m'},
    {'chr': 'ₙ', 'key': 'sub_n', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER N', 'tex': '_n'},
    {'chr': 'ₚ', 'key': 'sub_p', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER P', 'tex': '_p'},
    {'chr': 'ₛ', 'key': 'sub_s', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER S', 'tex': '_s'},
    {'chr': 'ₜ', 'key': 'sub_t', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER T', 'tex': '_t'},
    {'chr': 'ⱼ', 'key': 'sub_j', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER J', 'tex': '_j'},
    {'chr': 'ᵦ', 'key': 'sub_beta', 'utf_name': 'GREEK SUBSCRIPT SMALL LETTER BETA', 'tex': '_\\beta'},
    {'chr': 'ᵧ', 'key': 'sub_gamma', 'utf_name': 'GREEK SUBSCRIPT SMALL LETTER GAMMA', 'tex': '_\\gamma'},
    {'chr': 'ᵨ', 'key': 'sub_rho', 'utf_name': 'GREEK SUBSCRIPT SMALL LETTER RHO', 'tex': '_\\rho'},
    {'chr': 'ᵩ', 'key': 'sub_phi', 'utf_name': 'GREEK SUBSCRIPT SMALL LETTER PHI', 'tex': '_\\phi'},
    {'chr': 'ᵪ', 'key': 'sub_chi', 'utf_name': 'GREEK SUBSCRIPT SMALL LETTER CHI', 'tex': '_\\chi'},

    {'chr': '⨧', 'key': 'plus_with_sub_2', 'utf_name': 'PLUS SIGN WITH SUBSCRIPT TWO', 'tex': '\\plussubtwo'},

]

TABLES['superscripts'] = [
    {'chr': '⁰', 'key': 'sup_0', 'utf_name': 'SUPERSCRIPT ZERO', 'tex': '^0'},
    {'chr': '¹', 'key': 'sup_1', 'utf_name': 'SUPERSCRIPT ONE', 'tex': '^1'},
    {'chr': '²', 'key': 'sup_2', 'utf_name': 'SUPERSCRIPT TWO', 'tex': '^2'},
    {'chr': '³', 'key': 'sup_3', 'utf_name': 'SUPERSCRIPT THREE', 'tex': '^3'},
    {'chr': '⁴', 'key': 'sup_4', 'utf_name': 'SUPERSCRIPT FOUR', 'tex': '^4'},
    {'chr': '⁵', 'key': 'sup_5', 'utf_name': 'SUPERSCRIPT FIVE', 'tex': '^5'},
    {'chr': '⁶', 'key': 'sup_6', 'utf_name': 'SUPERSCRIPT SIX', 'tex': '^6'},
    {'chr': '⁷', 'key': 'sup_7', 'utf_name': 'SUPERSCRIPT SEVEN', 'tex': '^7'},
    {'chr': '⁸', 'key': 'sup_8', 'utf_name': 'SUPERSCRIPT EIGHT', 'tex': '^8'},
    {'chr': '⁹', 'key': 'sup_9', 'utf_name': 'SUPERSCRIPT NINE', 'tex': '^9'},
    {'chr': '⁺', 'key': 'sup_plus', 'utf_name': 'SUPERSCRIPT PLUS SIGN', 'tex': '^+'},
    {'chr': '⁻', 'key': 'sup_minus', 'utf_name': 'SUPERSCRIPT MINUS', 'tex': '^-'},
    {'chr': '⁼', 'key': 'sup_eq', 'utf_name': 'SUPERSCRIPT EQUALS SIGN', 'tex': '^='},
    {'chr': '⁽', 'key': 'sup_lparen', 'utf_name': 'SUPERSCRIPT LEFT PARENTHESIS', 'tex': '^('},
    {'chr': '⁾', 'key': 'sup_rparen', 'utf_name': 'SUPERSCRIPT RIGHT PARENTHESIS', 'tex': '^)'},
    {'chr': 'ⁿ', 'key': 'sup_n', 'utf_name': 'SUPERSCRIPT LATIN SMALL LETTER N', 'tex': '^n'},
    {'chr': 'ⁱ', 'key': 'sup_i', 'utf_name': 'SUPERSCRIPT LATIN SMALL LETTER I', 'tex': '^i'},
]

TABLES['quantifiers'] = [
    # {'chr': '∊', 'key': 'small_element_of', 'utf_name': 'SMALL ELEMENT OF'},
    # {'chr': 'ϵ', 'key': 'lunate_epsilon', 'utf_name': 'GREEK LUNATE EPSILON SYMBOL'},
    {'chr': '∈', 'key': 'elementof', 'utf_name': 'ELEMENT OF', 'tex': '\\in'},
    {'chr': '∉', 'key': 'not_elementof', 'utf_name': 'NOT AN ELEMENT OF', 'tex': '\\notin'},
    {'chr': '∀', 'key': 'forall', 'utf_name': 'FOR ALL', 'tex': '\\forall'},
    {'chr': '∃', 'key': 'exists', 'utf_name': 'THERE EXISTS', 'tex': '\\exists'},
    {'chr': '∄', 'key': 'not_exists', 'utf_name': 'THERE DOES NOT EXIST', 'tex': '\\nexists'},
]

TABLES['numeric_sets'] = [
    {'chr': '𝔽', 'key': 'finitefield', 'utf_name': 'MATHEMATICAL DOUBLE-STRUCK CAPITAL F', 'tex': '\\mathbb{F}'},

    {'chr': 'ℕ', 'key': 'natural', 'utf_name': 'DOUBLE-STRUCK CAPITAL N', 'tex': '\\mathbb{N}'},

    {'chr': 'ℚ', 'key': 'rational', 'utf_name': 'DOUBLE-STRUCK CAPITAL Q', 'tex': '\\mathbb{Q}'},

    {'chr': 'ℂ', 'key': 'complex', 'utf_name': 'DOUBLE-STRUCK CAPITAL C', 'tex': '\\mathbb{C}'},

    {'chr': 'ℍ', 'key': 'quaternion', 'utf_name': 'DOUBLE-STRUCK CAPITAL H', 'tex': '\\mathbb{H}'},

    {'chr': '𝕆', 'key': 'octernion', 'utf_name': 'MATHEMATICAL DOUBLE-STRUCK CAPITAL O', 'tex': '\\mathbb{O}'},

    {'chr': 'ℙ', 'key': 'irrational', 'utf_name': 'DOUBLE-STRUCK CAPITAL P', 'tex': '\\mathbb{P}'},

    {'chr': 'ℝ', 'key': 'real', 'utf_name': 'DOUBLE-STRUCK CAPITAL R', 'tex': '\\mathbb{R}'},

    {'chr': 'ℤ', 'key': 'integer', 'utf_name': 'DOUBLE-STRUCK CAPITAL Z', 'tex': '\\mathbb{Z}'},

    {'chr': '𝕋', 'key': 'trigintaduonion', 'utf_name': 'MATHEMATICAL DOUBLE-STRUCK CAPITAL T', 'tex': '\\mathbb{T}'},

    {'chr': '𝟙', 'key': 'ones', 'utf_name': 'MATHEMATICAL DOUBLE-STRUCK DIGIT ONE', 'tex': '\\mathbb{1}'},

    {'chr': '∅', 'key': 'emptyset', 'utf_name': 'EMPTY SET', 'tex': '\\varnothing'},

    # floating    = '𝕃'  # proposed
]

TABLES['set_operators'] = [
    {'chr': '∖', 'key': 'setdiff', 'utf_name': 'SET MINUS', 'tex': '\\smallsetminus'},
    {'chr': '⊂', 'key': 'subset', 'utf_name': 'SUBSET OF', 'tex': '\\subset'},
    {'chr': '⊃', 'key': 'supset', 'utf_name': 'SUPERSET OF', 'tex': '\\supset'},
    {'chr': '⊆', 'key': 'subset_eq', 'utf_name': 'SUBSET OF OR EQUAL TO', 'tex': '\\subseteq'},
    {'chr': '⊇', 'key': 'supset_eq', 'utf_name': 'SUPERSET OF OR EQUAL TO', 'tex': '\\supseteq'},
    {'chr': '⊊', 'key': 'subset_eq', 'utf_name': 'SUBSET OF WITH NOT EQUAL TO', 'tex': '\\subsetneq'},
    {'chr': '⊋', 'key': 'supset_neq', 'utf_name': 'SUPERSET OF WITH NOT EQUAL TO', 'tex': '\\supsetneq'},
    {'chr': '∩', 'key': 'isect', 'utf_name': 'INTERSECTION', 'tex': '\\cap', 'alias': ['cup']},
    {'chr': '∪', 'key': 'union', 'utf_name': 'UNION', 'tex': '\\cup', 'alias': ['cap']},

    {'chr': '⊉', 'key': 'subset_not_ge', 'utf_name': 'NEITHER A SUPERSET OF NOR EQUAL TO', 'tex': '\\nsupseteq'},
    {'chr': '⊅', 'key': 'subset_not_gt', 'utf_name': 'NOT A SUPERSET OF', 'tex': '\\nsupset'},
    {'chr': '⊄', 'key': 'subset_not_lt', 'utf_name': 'NOT A SUBSET OF', 'tex': '\\nsubset'},
    {'chr': '⊈', 'key': 'subset_not_le', 'utf_name': 'NEITHER A SUBSET OF NOR EQUAL TO', 'tex': '\\nsubseteq'},

]

TABLES['relational'] = [
    {'chr': '≤', 'key': 'le', 'utf_name': 'LESS-THAN OVER EQUAL TO', 'tex': '\\leq'},
    {'chr': '≥', 'key': 'ge', 'utf_name': 'GREATER-THAN OR EQUAL TO', 'tex': '\\geq'},
    {'chr': '<', 'key': 'lt', 'utf_name': 'LESS-THAN SIGN', 'tex': '<'},
    {'chr': '>', 'key': 'gt', 'utf_name': 'GREATER-THAN SIGN', 'tex': '>'},
    {'chr': '=', 'key': 'eq', 'utf_name': 'EQUALS SIGN'},
    {'chr': '≠', 'key': 'ne', 'utf_name': 'NOT EQUAL TO', 'tex': '\\neq'},
    {'chr': '≈', 'key': 'approx_eq', 'utf_name': 'ALMOST EQUAL TO', 'tex': '\\approx'},
    {'chr': '≇', 'key': 'not_approx', 'utf_name': 'NEITHER APPROXIMATELY NOR ACTUALLY EQUAL TO', 'tex': '\\ncong'},
    {'chr': '≆', 'key': 'approx_ne', 'utf_name': 'APPROXIMATELY BUT NOT ACTUALLY EQUAL TO', 'tex': '\\simneqq'},
    {'chr': '∝', 'key': 'propor', 'utf_name': 'PROPORTIONAL TO', 'tex': '\\propto'},
    {'chr': '≡', 'key': 'equiv', 'utf_name': 'IDENTICAL TO', 'tex': '\\equiv'},
    {'chr': '≢', 'key': 'not_equiv', 'utf_name': 'NOT IDENTICAL TO', 'tex': '\\nequiv'},
    {'chr': '≅', 'key': 'cong', 'utf_name': 'APPROXIMATELY EQUAL TO', 'tex': '\\cong'},
    {'chr': '≔', 'key': 'doteq', 'utf_name': 'COLON EQUALS', 'tex': '\\coloneq'},
    {'chr': '≕', 'key': 'eqdot', 'utf_name': 'EQUALS COLON', 'tex': '\\eqcolon'},
]

TABLES['numeric_operators'] = [
    {'chr': '±', 'key': 'pm', 'utf_name': 'PLUS-MINUS SIGN', 'tex': '\\pm'},
    {'chr': '√', 'key': 'square_root', 'utf_name': 'SQUARE ROOT', 'tex': '\\sqrt'},
    {'chr': '∛', 'key': 'cube_root', 'utf_name': 'CUBE ROOT', 'tex': '\\sqrt[3]'},
    {'chr': '∜', 'key': 'quad_root', 'utf_name': 'FOURTH ROOT', 'tex': '\\sqrt[4]'},
]

TABLES['other_operators'] = [
    {'chr': '⋅', 'key': 'cdot', 'utf_name': 'DOT OPERATOR', 'tex': '\\cdot'},
    {'chr': '∘', 'key': 'circ', 'utf_name': 'RING OPERATOR', 'tex': '\\circ'},
    {'chr': '×', 'key': 'times', 'utf_name': 'MULTIPLICATION SIGN', 'tex': '\\times'},
    {'chr': '⊕', 'key': 'oplus', 'utf_name': 'CIRCLED PLUS', 'tex': '\\oplus'},
]


TABLES['nary'] = [
    {'chr': '∏', 'key': 'nary_prod', 'utf_name': 'N-ARY PRODUCT', 'tex': '\\prod'},
    {'chr': '∑', 'key': 'nary_sum', 'utf_name': 'N-ARY SUMMATION', 'tex': '\\sum'},
    {'chr': '⋂', 'key': 'nary_isect', 'utf_name': 'N-ARY INTERSECTION', 'tex': '\\bigcap'},
    {'chr': '⋃', 'key': 'nary_union', 'utf_name': 'N-ARY UNION', 'tex': '\\bigcup'},
]


TABLES['arrows'] = [
    {'chr': '→', 'key': 'right_arrow', 'utf_name': 'RIGHTWARDS ARROW', 'tex': '\\rightarrow', 'alias': ['to']},
    {'chr': '←', 'key': 'left_arrow', 'utf_name': 'LEFTWARDS ARROW', 'tex': '\\leftarrow'},
    {'chr': '←', 'key': 'bidir_arrow', 'utf_name': 'LEFTWARDS ARROW', 'tex': '\\leftarrow'},
    {'chr': '⇒', 'key': 'right_darrow', 'utf_name': 'RIGHTWARDS DOUBLE ARROW', 'tex': '\\Rightarrow'},
    {'chr': '⇐', 'key': 'left_darrow', 'utf_name': 'LEFTWARDS DOUBLE ARROW', 'tex': '\\Leftarrow'},
    {'chr': '⇔', 'key': 'bidir_darrow', 'utf_name': 'LEFT RIGHT DOUBLE ARROW', 'tex': '\\Leftrightarrow'},
]


TABLES['logic'] = [
    {'chr': '∧', 'key': 'and', 'utf_name': 'LOGICAL AND', 'tex': '\\wedge'},
    {'chr': '∨', 'key': 'or', 'utf_name': 'LOGICAL OR', 'tex': '\\vee'},
    {'chr': '¬', 'key': 'not', 'utf_name': 'NOT SIGN', 'tex': '\\neg'},
]

TABLES['calclus'] = [
    {'chr': '∫', 'key': 'integral', 'utf_name': 'INTEGRAL', 'tex': '\\int'},
    {'chr': '∂', 'key': 'partial', 'utf_name': 'PARTIAL DIFFERENTIAL', 'tex': '\\partial'},
    {'chr': '∆', 'key': 'delta_upper', 'utf_name': 'INCREMENT', 'tex': '\\increment'},
    {'chr': '∇', 'key': 'nabla', 'utf_name': 'NABLA', 'tex': '\\varnabla', 'alias': ['del', 'gradient'], 'references': ['https://en.wikipedia.org/wiki/Del']},
]

TABLES['proof'] = [
    {'chr': '∴', 'key': 'therefore', 'utf_name': 'THEREFORE', 'tex': '\\therefore'},
    {'chr': '∎', 'key': 'qed', 'utf_name': 'END OF PROOF', 'tex': '\\QED'},
]

TABLES['nesting'] = [
    {'chr': '⟨', 'key': 'langle', 'utf_name': 'MATHEMATICAL LEFT ANGLE BRACKET', 'tex': '\\langle'},
    {'chr': '⟩', 'key': 'rangle', 'utf_name': 'MATHEMATICAL RIGHT ANGLE BRACKET', 'tex': '\\rangle'},
]

TABLES['misc'] = [
    {'chr': '⊥', 'key': 'perp', 'utf_name': 'UP TACK', 'tex': '\\bot'},
    {'chr': '⊢', 'key': 'yields', 'utf_name': 'RIGHT TACK', 'tex': '\\vdash', 'references': ['https://en.wikipedia.org/wiki/Turnstile_(symbol)']},
    {'chr': '⊨', 'key': 'satisfies', 'utf_name': 'TRUE', 'tex': '\\vDash', 'references': ['https://en.wikipedia.org/wiki/Double_turnstile']},
    {'chr': '…', 'key': 'ldots', 'utf_name': 'HORIZONTAL ELLIPSIS', 'tex': '\\ldots'},
    {'chr': '⋯', 'key': 'cdots', 'utf_name': 'MIDLINE HORIZONTAL ELLIPSIS', 'tex': '\\cdots'},
    {'chr': '⋈', 'key': 'join', 'utf_name': 'BOWTIE', 'tex': '\\bowtie'},
    {'chr': '≦', 'key': 'leqq', 'utf_name': 'LESS-THAN OVER EQUAL TO', 'tex': '\\leqq'},
    {'chr': '≧', 'key': 'geqq', 'utf_name': 'GREATER-THAN OVER EQUAL TO', 'tex': '\\geqq'},
]

TABLES['transfinite'] = [
    {'chr': '∞', 'key': 'infinity', 'utf_name': 'INFINITY', 'alias': ['infty'], 'tex': '\\infty'},
    {'chr': 'ℵ', 'key': 'aleph', 'utf_name': 'ALEF SYMBOL', 'tex': '\\aleph'},
    {'chr': 'ℶ', 'key': 'beth', 'utf_name': 'BET SYMBOL', 'alias': ['bet'], 'tex': '\\beth'},
]


def _compositions():
    """
    from mathutf.symbols import *  # NOQA
    """
    print(SYMBOLS['aleph'] + SYMBOLS['sub_1'])
    print(SYMBOLS['beth'] + SYMBOLS['sub_1'])


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


def _build_unicode_named_table():
    """
    https://stackoverflow.com/questions/10229156/how-many-characters-can-utf-8-encode
    TODO: generate all unicode characters, for now this is enough.
    """
    import unicodedata
    num_chars = 11141120
    import pygtrie
    trie = pygtrie.StringTrie(separator='_')
    invalids = []
    for index in range(1, num_chars):
        try:
            chr_ = chr(index)
            utf_name = unicodedata.name(chr_)
            key = utf_name.replace('-', '_').replace(' ', '_').lower()
            trie[key] = chr_
        except Exception:
            invalids.append(index)
    trie['greek_capital_letter_theta']
    # kwarray.group_consecutive(invalids)


def _show_all():
    import unicodedata
    all_items = []
    for table_name, subtable in TABLES.items():
        for item in subtable:
            v = item['chr']
            all_items.append(item)
            utf_name = unicodedata.name(v)
            item['group'] = table_name
            if item.get('utf_name', None) != utf_name:
                raise AssertionError(f'{item["utf_name"]} != {utf_name}')
            # print('{},'.format(ub.repr2(item, nl=0)))

    import pandas as pd
    import rich
    import rich.markup
    rich.print(rich.markup.escape(pd.DataFrame(all_items).to_string()))

    # dups = ub.find_duplicates(all_items, key=lambda x: x['chr'])


def _dev_map_to_latex():
    """
    Used to map symbols to latex names
    """
    js_map = ub.grabdata('https://raw.githubusercontent.com/fKunstner/latex-to-utf8/master/map.js')
    import ast
    latex_to_utf = ast.literal_eval(ub.Path(js_map).read_text()[10:])
    latex_to_utf = ub.udict(latex_to_utf)
    utf_to_latex = latex_to_utf.invert(unique_vals=0)

    def reorder_dict(d, head=[], tail=[]):
        orig = d
        d = ub.udict(d)
        head_parts = d & head
        tail_parts = d & tail
        rest_parts = d - (head_parts) - (tail_parts)
        new = head_parts | rest_parts | tail_parts
        orig.clear()
        orig.update(new)
        return new

    hard_coded = {
        'Υ': {r'\Upsilon'},
        'ᵦ': {r'_\beta'},
        'ᵧ': {r'_\gamma'},
        'ᵨ': {r'_\rho'},
        'ᵩ': {r'_\phi'},
        'ᵪ': {r'_\chi'},
        '∂': {r'\partial'},
        '→': {r'\rightarrow'},
        '∘': {r'\circ'},
        '…': {r'\ldots'},
        '≠': {r'\neq'},
        '𝜏': {r'\mittau'},
    }
    utf_to_latex.update(hard_coded)

    def lookup_item_tex(item):
        tex_items = list(utf_to_latex[item['chr']])
        if len(tex_items) > 1:
            norms = list(ub.unique([t.replace('\\up', '\\') for t in tex_items]))
            if len(norms) == 1:
                tex_items = norms
            norms = list(ub.unique([t.replace('\\unicode', '\\') for t in tex_items]))
            if len(norms) == 1:
                tex_items = norms
            norms = list(ub.unique([t.lower() for t in tex_items]))
            if len(norms) == 1:
                tex_items = norms
            if any('mathbb' in t for t in tex_items):
                norms = [t for t in tex_items if t.startswith('\\mathbb{')]
                if len(norms) == 1:
                    tex_items = norms
            if any('sqrt[' in t for t in tex_items):
                norms = [t for t in tex_items if t.startswith('\\sqrt[')]
                if len(norms) == 1:
                    tex_items = norms
        if len(tex_items) > 1:
            ambiguous.append([item, tex_items])

        return tex_items[0]

    failed = []
    ambiguous = []
    for table_name, subtable in TABLES.items():
        for item in subtable:
            if 'tex' not in item:
                try:
                    item['tex'] = lookup_item_tex(item)
                except Exception:
                    failed.append(item)

            reorder_dict(item, tail=['alias', 'references'])

    print('TABLES = {}')
    for table_name, subtable in TABLES.items():
        print('')
        print(f'TABLES["{table_name}"] = ' + ub.urepr(subtable))
        ...


def _dev_search_for_symbols():
    """
    Used to help build the initial list.
    """
    import unicodedata

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


def search(query):
    """
    Example:
        query = 'beta'
    """
    # Handle normalization of queries
    if query == '*':
        query = '.*'

    import re
    pat = re.compile(query, flags=re.IGNORECASE)

    for table_name, subtable in TABLES.items():
        for item in subtable:
            item['group'] = table_name

            flag = pat.search(item['key'])
            if not flag:
                flag = pat.search(item['utf_name'])
            if not flag:
                flag = pat.search(item['group'])
            if not flag:
                for alias in item.get('alias', []):
                    flag = pat.search(alias)
                    if flag:
                        break

            if flag:
                yield item
