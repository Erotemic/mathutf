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
    # Digits
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

    # Signs
    {'chr': '₊', 'key': 'sub_plus', 'utf_name': 'SUBSCRIPT PLUS SIGN', 'tex': '_+'},
    {'chr': '₋', 'key': 'sub_minus', 'utf_name': 'SUBSCRIPT MINUS', 'tex': '_-'},
    {'chr': '₌', 'key': 'sub_eq', 'utf_name': 'SUBSCRIPT EQUALS SIGN', 'tex': '_='},

    {'chr': '₍', 'key': 'sub_lparen', 'utf_name': 'SUBSCRIPT LEFT PARENTHESIS', 'tex': '_('},
    {'chr': '₎', 'key': 'sub_rparen', 'utf_name': 'SUBSCRIPT RIGHT PARENTHESIS', 'tex': '_)'},

    # IPA-derived subscripts (outside main subscript block)
    # https://en.wikipedia.org/wiki/Unicode_subscripts_and_superscripts
    {'chr': 'ᵢ', 'key': 'sub_i', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER I', 'tex': '_i'},
    {'chr': 'ᵣ', 'key': 'sub_r', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER R', 'tex': '_r'},
    {'chr': 'ᵤ', 'key': 'sub_u', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER U', 'tex': '_u'},
    {'chr': 'ᵥ', 'key': 'sub_v', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER V', 'tex': '_v'},
    {'chr': 'ⱼ', 'key': 'sub_j', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER J', 'tex': '_j'},

    # Latin subscripts (U+2090–U+209F block)
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

    # There are no subscripts for b c d f g q w y z

    # Greek subscripts
    {'chr': 'ᵦ', 'key': 'sub_beta', 'utf_name': 'GREEK SUBSCRIPT SMALL LETTER BETA', 'tex': '_\\beta'},
    {'chr': 'ᵧ', 'key': 'sub_gamma', 'utf_name': 'GREEK SUBSCRIPT SMALL LETTER GAMMA', 'tex': '_\\gamma'},
    {'chr': 'ᵨ', 'key': 'sub_rho', 'utf_name': 'GREEK SUBSCRIPT SMALL LETTER RHO', 'tex': '_\\rho'},
    {'chr': 'ᵩ', 'key': 'sub_phi', 'utf_name': 'GREEK SUBSCRIPT SMALL LETTER PHI', 'tex': '_\\phi'},
    {'chr': 'ᵪ', 'key': 'sub_chi', 'utf_name': 'GREEK SUBSCRIPT SMALL LETTER CHI', 'tex': '_\\chi'},

    # Misc
    {'chr': 'ₔ', 'key': 'sub_schwa', 'utf_name': 'LATIN SUBSCRIPT SMALL LETTER SCHWA', 'tex': '_\\schwa'},

    {'chr': '⨧', 'key': 'plus_with_sub_2', 'utf_name': 'PLUS SIGN WITH SUBSCRIPT TWO', 'tex': '\\plussubtwo'},

]

TABLES['superscripts'] = [
    {'chr': '⁰', 'key': 'sup_0', 'utf_name': 'SUPERSCRIPT ZERO', 'tex': '^0'},
    {'chr': '¹', 'key': 'sup_1', 'utf_name': 'SUPERSCRIPT ONE', 'tex': '^1'},
    {'chr': '²', 'key': 'sup_2', 'utf_name': 'SUPERSCRIPT TWO', 'tex': '^2', 'alias': ['squared']},
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

    # The letters i, n have dedicated Superscripts and Subscripts block representations
    # because they are historically important in math and chemistry, added in
    # (1993 AI fact, todo check)
    # https://rupertshepherd.info/resource_pages/superscript-letters-in-unicode
    {'chr': 'ⁿ', 'key': 'sup_n', 'utf_name': 'SUPERSCRIPT LATIN SMALL LETTER N', 'tex': '^n'},
    {'chr': 'ⁱ', 'key': 'sup_i', 'utf_name': 'SUPERSCRIPT LATIN SMALL LETTER I', 'tex': '^i'},

    # The rest of the superscript alphabet exists in the Phonetic Extensions /
    # Spacing Modifier Letters blocks (added in 2003 AI fact, todo check).
    {'chr': 'ᵃ', 'key': 'sup_a', 'utf_name': 'MODIFIER LETTER SMALL A', 'tex': '^a'},
    {'chr': 'ᵇ', 'key': 'sup_b', 'utf_name': 'MODIFIER LETTER SMALL B', 'tex': '^b'},
    {'chr': 'ᶜ', 'key': 'sup_c', 'utf_name': 'MODIFIER LETTER SMALL C', 'tex': '^c'},
    {'chr': 'ᵈ', 'key': 'sup_d', 'utf_name': 'MODIFIER LETTER SMALL D', 'tex': '^d'},
    {'chr': 'ᵉ', 'key': 'sup_e', 'utf_name': 'MODIFIER LETTER SMALL E', 'tex': '^e'},
    {'chr': 'ᶠ', 'key': 'sup_f', 'utf_name': 'MODIFIER LETTER SMALL F', 'tex': '^f'},
    {'chr': 'ᵍ', 'key': 'sup_g', 'utf_name': 'MODIFIER LETTER SMALL G', 'tex': '^g'},
    {'chr': 'ʰ', 'key': 'sup_h', 'utf_name': 'MODIFIER LETTER SMALL H', 'tex': '^h'},
    {'chr': 'ʲ', 'key': 'sup_j', 'utf_name': 'MODIFIER LETTER SMALL J', 'tex': '^j'},
    {'chr': 'ᵏ', 'key': 'sup_k', 'utf_name': 'MODIFIER LETTER SMALL K', 'tex': '^k'},
    {'chr': 'ˡ', 'key': 'sup_l', 'utf_name': 'MODIFIER LETTER SMALL L', 'tex': '^l'},
    {'chr': 'ᵐ', 'key': 'sup_m', 'utf_name': 'MODIFIER LETTER SMALL M', 'tex': '^m'},
    # n is above
    {'chr': 'ᵒ', 'key': 'sup_o', 'utf_name': 'MODIFIER LETTER SMALL O', 'tex': '^o'},
    {'chr': 'ᵖ', 'key': 'sup_p', 'utf_name': 'MODIFIER LETTER SMALL P', 'tex': '^p'},
    {'chr': 'ʳ', 'key': 'sup_r', 'utf_name': 'MODIFIER LETTER SMALL R', 'tex': '^r'},
    {'chr': 'ˢ', 'key': 'sup_s', 'utf_name': 'MODIFIER LETTER SMALL S', 'tex': '^s'},
    {'chr': 'ᵗ', 'key': 'sup_t', 'utf_name': 'MODIFIER LETTER SMALL T', 'tex': '^t'},
    {'chr': 'ᵘ', 'key': 'sup_u', 'utf_name': 'MODIFIER LETTER SMALL U', 'tex': '^u'},
    {'chr': 'ᵛ', 'key': 'sup_v', 'utf_name': 'MODIFIER LETTER SMALL V', 'tex': '^v'},
    {'chr': 'ʷ', 'key': 'sup_w', 'utf_name': 'MODIFIER LETTER SMALL W', 'tex': '^w'},
    {'chr': 'ˣ', 'key': 'sup_x', 'utf_name': 'MODIFIER LETTER SMALL X', 'tex': '^x'},
    {'chr': 'ʸ', 'key': 'sup_y', 'utf_name': 'MODIFIER LETTER SMALL Y', 'tex': '^y'},
    {'chr': 'ᶻ', 'key': 'sup_z', 'utf_name': 'MODIFIER LETTER SMALL Z', 'tex': '^z'},


]

TABLES['quantifiers'] = [
    # {'chr': '∊', 'key': 'small_element_of', 'utf_name': 'SMALL ELEMENT OF'},
    # {'chr': 'ϵ', 'key': 'lunate_epsilon', 'utf_name': 'GREEK LUNATE EPSILON SYMBOL'},
    {'chr': '∈', 'key': 'elementof', 'utf_name': 'ELEMENT OF', 'tex': '\\in', 'alias': ['epsilon']},
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

# 𝔸

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
    {'chr': '≤', 'key': 'le', 'utf_name': 'LESS-THAN OR EQUAL TO', 'tex': '\\leq'},
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
    {'chr': '×', 'key': 'times', 'utf_name': 'MULTIPLICATION SIGN', 'tex': '\\times', 'alias': ['product']},
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
    {'chr': '∬', 'key': 'double_integral', 'utf_name': 'DOUBLE INTEGRAL', 'tex': '\\iint', 'description': 'Double integral (area/volume integration)'},
    {'chr': '∭', 'key': 'triple_integral', 'utf_name': 'TRIPLE INTEGRAL', 'tex': '\\iiint', 'description': 'Triple integral (volume integration in 3D)'},

    # Surface and contour integrals
    {'chr': '∮', 'key': 'contour_integral', 'utf_name': 'CONTOUR INTEGRAL', 'tex': '\\oint', 'description': 'Closed loop/contour integral (complex analysis)'},
    {'chr': '∯', 'key': 'surface_integral', 'utf_name': 'SURFACE INTEGRAL', 'tex': '\\oiint', 'description': 'Closed surface integral (flux calculations)'},
    {'chr': '∰', 'key': 'volume_integral', 'utf_name': 'VOLUME INTEGRAL', 'tex': '\\oiiint', 'description': 'Closed volume integral (e.g., divergence theorem)'},

    {'chr': '∂', 'key': 'partial', 'utf_name': 'PARTIAL DIFFERENTIAL', 'tex': '\\partial'},
    {'chr': '∆', 'key': 'delta_upper', 'utf_name': 'INCREMENT', 'tex': '\\increment'},
    {'chr': '∇', 'key': 'nabla', 'utf_name': 'NABLA', 'tex': '\\varnabla', 'alias': ['del', 'gradient'], 'references': ['https://en.wikipedia.org/wiki/Del']},
]

TABLES['proof'] = [
    {'chr': '∴', 'key': 'therefore', 'utf_name': 'THEREFORE', 'tex': '\\therefore'},
    {'chr': '∎', 'key': 'qed', 'utf_name': 'END OF PROOF', 'tex': '\\QED'},
    {'chr': '□', 'key': 'square', 'utf_name': 'WHITE SQUARE', 'tex': r'\square', 'description': 'QED/□ end-of-proof marker (alternative to ∎).'},
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
    {'chr': '𝔠', 'key': 'fraktur_c', 'utf_name': 'Mathematical Fraktur Small C', 'tex': '\\mathfrak{c}', 'description': 'cardinality of the continumou', 'references': ['https://en.wikipedia.org/wiki/Cardinal_characteristic_of_the_continuum']},
]

TABLES['geometry'] = [
    {'chr': '∦', 'key': 'not_parallel', 'utf_name': 'NOT PARALLEL TO', 'tex': r'\nparallel', 'description': 'Lines are not parallel.'},
    {'chr': '∥', 'key': 'parallel', 'utf_name': 'PARALLEL TO', 'tex': r'\parallel', 'description': 'Parallel lines (a ∥ b).'},
    {'chr': '∠', 'key': 'angle', 'utf_name': 'ANGLE', 'tex': r'\angle', 'description': 'Plain angle (∠ABC).'},
    {'chr': '∡', 'key': 'measured_angle', 'utf_name': 'MEASURED ANGLE', 'tex': r'\measuredangle', 'description': 'Oriented/measured angle.'},
    {'chr': '∢', 'key': 'spherical_angle', 'utf_name': 'SPHERICAL ANGLE', 'tex': r'\sphericalangle', 'description': 'Angle on a sphere (solid/dihedral angle contexts).'},
    {'chr': '∟', 'key': 'right_angle', 'utf_name': 'RIGHT ANGLE', 'tex': r'\rightangle', 'description': 'Right angle glyph; often used in diagrams.'},
    {'chr': '⊾', 'key': 'right_angle_with_arc', 'utf_name': 'RIGHT ANGLE WITH ARC', 'tex': r'\rightanglewitharc', 'description': 'Right angle marked with arc (diagrammatic).'},
    {'chr': '⟂', 'key': 'perpendicular', 'utf_name': 'PERPENDICULAR', 'tex': r'\perp', 'description': 'Perpendicular/orthogonal relation.'},
    {'chr': '≅', 'key': 'congruent', 'utf_name': 'APPROXIMATELY EQUAL TO', 'tex': r'\cong', 'description': 'Congruent (often used for geometric figures).'},
    {'chr': '∼', 'key': 'similar', 'utf_name': 'TILDE', 'tex': r'\sim', 'description': 'Similar figures (same shape, scaled).'},
]

TABLES['other'] = [
    {'chr': '™', 'key': 'trademark', 'utf_name': 'TRADE MARK SIGN', 'alias': ['tm'], 'tex': r'\textsuperscript{\texttrademark}'},
]


# ---- Relational / equivalence refinements -----------------------------------
TABLES['relational'].extend([
    {'chr': '≃', 'key': 'simeq', 'utf_name': 'ASYMPTOTICALLY EQUAL TO', 'tex': r'\simeq', 'description': '“Equal up to small error”; used for asymptotics or shape/structural equivalence.'},
    {'chr': '≍', 'key': 'asymp', 'utf_name': 'EQUIVALENT TO', 'tex': r'\asymp', 'description': 'Two quantities grow at comparable rate; f ≍ g means same order of magnitude.'},
    {'chr': '≜', 'key': 'triangleq', 'utf_name': 'DELTA EQUAL TO', 'tex': r'\triangleq', 'description': 'Definition by fiat: “is defined as”.'},
    {'chr': '≝', 'key': 'defeq', 'utf_name': 'EQUAL TO BY DEFINITION', 'tex': r'\stackrel{\mathrm{def}}{=}', 'description': 'Explicitly marks an equality as a definition.'},
    {'chr': '≟', 'key': 'questeq', 'utf_name': 'QUESTIONED EQUAL TO', 'tex': r'\overset{?}{=}', 'description': 'Proposed/unknown equality (used in derivations or puzzles).'},
])

# ---- Logic: more connectives & turnstiles -----------------------------------
TABLES['logic'].extend([
    {'chr': '⊻', 'key': 'xor', 'utf_name': 'XOR', 'tex': r'\veebar', 'description': 'Exclusive OR (true when exactly one operand is true).'},
    {'chr': '⊼', 'key': 'nand', 'utf_name': 'NAND', 'tex': r'\barwedge', 'description': 'NOT (A AND B); functionally complete connective.'},
    {'chr': '⊽', 'key': 'nor', 'utf_name': 'NOR', 'tex': r'\curlyvee', 'description': 'NOT (A OR B); also functionally complete.'},
])

TABLES['misc'].extend([
    {'chr': '⊩', 'key': 'forces', 'utf_name': 'FORCES', 'tex': r'\Vdash', 'description': 'Semantic entailment/forcing; model-theoretic truth in all extensions.'},
    {'chr': '⊬', 'key': 'not_proves', 'utf_name': 'DOES NOT PROVE', 'tex': r'\nvdash', 'description': 'Syntactic non-derivability (no proof in the calculus).'},
    {'chr': '⊭', 'key': 'not_models', 'utf_name': 'NOT TRUE', 'tex': r'\nVdash', 'description': 'Does not semantically entail; not valid in all models.'},
    {'chr': '⊧', 'key': 'models_alt', 'utf_name': 'MODELS', 'tex': r'\models', 'description': 'Semantic consequence / satisfaction (𝔐 ⊧ φ).'},
])

# ---- Arrows: injections/surjections/harpoons/hooks ---------------------------
TABLES['arrows'].extend([
    {'chr': '↪', 'key': 'hookrightarrow', 'utf_name': 'RIGHTWARDS ARROW WITH HOOK', 'tex': r'\hookrightarrow', 'description': 'Injection/monomorphism (structure-preserving embedding).'},
    {'chr': '↩', 'key': 'hookleftarrow', 'utf_name': 'LEFTWARDS ARROW WITH HOOK', 'tex': r'\hookleftarrow', 'description': 'Left hook variant (category theory; partial inverses).'},
    {'chr': '↠', 'key': 'twoheadrightarrow', 'utf_name': 'RIGHTWARDS TWO-HEADED ARROW', 'tex': r'\twoheadrightarrow', 'description': 'Surjection/epimorphism.'},
    {'chr': '⇀', 'key': 'rightharpoonup', 'utf_name': 'RIGHTWARDS HARPOON WITH BARB UPWARDS', 'tex': r'\rightharpoonup', 'description': 'Vector/functional mappings; also used for limits/arrows in analysis.'},
    {'chr': '↼', 'key': 'leftharpoonup', 'utf_name': 'LEFTWARDS HARPOON WITH BARB UPWARDS', 'tex': r'\leftharpoonup', 'description': 'Paired with right harpoon for bidirectional maps.'},
    {'chr': '⟶', 'key': 'longrightarrow', 'utf_name': 'LONG RIGHTWARDS ARROW', 'tex': r'\longrightarrow', 'description': 'Long arrow for maps/sequences; improves readability in displays.'},
    {'chr': '⟵', 'key': 'longleftarrow', 'utf_name': 'LONG LEFTWARDS ARROW', 'tex': r'\longleftarrow', 'description': 'Long left arrow (inverse maps, rewrites).'},
    {'chr': '⟷', 'key': 'longleftrightarrow', 'utf_name': 'LONG LEFT RIGHT ARROW', 'tex': r'\longleftrightarrow', 'description': 'Long bidirectional arrow (bijections, correspondences).'},
    {'chr': '⟹', 'key': 'LongRightarrow', 'utf_name': 'LONG RIGHTWARDS DOUBLE ARROW', 'tex': r'\Longrightarrow', 'description': 'Long implication; used for “therefore” style steps.'},
    {'chr': '⟸', 'key': 'LongLeftarrow', 'utf_name': 'LONG LEFTWARDS DOUBLE ARROW', 'tex': r'\Longleftarrow', 'description': 'Long reverse implication.'},
    {'chr': '⟺', 'key': 'LongLeftrightarrow', 'utf_name': 'LONG LEFT RIGHT DOUBLE ARROW', 'tex': r'\Longleftrightarrow', 'description': 'Long logical equivalence.'},
])

# ---- Lattices / set-like binary operators -----------------------------------
TABLES['other_operators'].extend([
    {'chr': '⊓', 'key': 'sqcap', 'utf_name': 'SQUARE CAP', 'tex': r'\sqcap', 'description': 'Lattice-theoretic meet; “and”-like aggregation.'},
    {'chr': '⊔', 'key': 'sqcup', 'utf_name': 'SQUARE CUP', 'tex': r'\sqcup', 'description': 'Lattice-theoretic join; “or”-like aggregation.'},
])

# ---- Membership / containment complements -----------------------------------
TABLES['set_operators'].extend([
    {'chr': '∋', 'key': 'contains_as_member', 'utf_name': 'CONTAINS AS MEMBER', 'tex': r'\ni', 'description': 'Reverse membership; x ∈ A  ⇔  A ∋ x.'},
    {'chr': '∌', 'key': 'not_contains_as_member', 'utf_name': 'DOES NOT CONTAIN AS MEMBER', 'tex': r'\not\ni', 'description': 'Negation of reverse membership.'},
])

# ---- Brackets often used in semantics / intervals ----------------------------
TABLES['nesting'].extend([
    {'chr': '⟦', 'key': 'llbracket', 'utf_name': 'MATHEMATICAL LEFT WHITE SQUARE BRACKET', 'tex': r'\llbracket', 'description': 'Denotation/semantic brackets; also Iverson brackets.'},
    {'chr': '⟧', 'key': 'rrbracket', 'utf_name': 'MATHEMATICAL RIGHT WHITE SQUARE BRACKET', 'tex': r'\rrbracket', 'description': 'Right denotation/semantic bracket.'},
])

# ---- Ellipses variants -------------------------------------------------------
TABLES['misc'].extend([
    {'chr': '⋮', 'key': 'vdots', 'utf_name': 'VERTICAL ELLIPSIS', 'tex': r'\vdots', 'description': 'Vertical continuation (matrices, systems).'},
    {'chr': '⋱', 'key': 'ddots', 'utf_name': 'DIAGONAL ELLIPSIS', 'tex': r'\ddots', 'description': 'Diagonal continuation (block matrices).'},
    {'chr': '⋰', 'key': 'udots', 'utf_name': 'UP RIGHT DIAGONAL ELLIPSIS', 'tex': r'\iddots', 'description': 'Ascending diagonal continuation (variant).'},
])

# ---- Numeric sets / common fancy letters ------------------------------------
TABLES['numeric_sets'].extend([
    {'chr': '𝔸', 'key': 'dblA', 'utf_name': 'MATHEMATICAL DOUBLE-STRUCK CAPITAL A', 'tex': r'\mathbb{A}', 'description': 'Context-dependent: adele ring in number theory; also affine space A^n.'},
    {'chr': '𝒪', 'key': 'bigO', 'utf_name': 'MATHEMATICAL SCRIPT CAPITAL O', 'tex': r'\mathcal{O}', 'description': 'Big-O growth rate (analysis/CS complexity).'},
    {'chr': '℘', 'key': 'weierstrass_p', 'utf_name': 'SCRIPT CAPITAL P', 'tex': r'\wp', 'description': 'Weierstrass elliptic function (complex analysis).'},
    {'chr': '𝒫', 'key': 'powerset', 'utf_name': 'MATHEMATICAL SCRIPT CAPITAL P', 'tex': r'\mathcal{P}', 'description': 'Power set / set of all subsets.'},
])


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
            try:
                key = item['key']
                if keyword.iskeyword(key):
                    key = key + '_'
                SYMBOLS[key] = item['chr']
            except Exception:
                print(f'issue with item = {ub.urepr(item, nl=1)} in {table_name}')
                raise
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
    """
    Used to map symbols to latex names

    Ignore:
        from mathutf.symbols import *  # NOQA
        from mathutf.symbols import _compositions, _populate_class, _build_unicode_named_table, _show_all, _dev_map_to_latex, _dev_search_for_symbols
        _show_all()
    """
    import unicodedata
    all_items = []
    for table_name, subtable in TABLES.items():
        for item in subtable:
            v = item['chr']
            all_items.append(item)
            utf_name = unicodedata.name(v)
            item['group'] = table_name
            cp = ord(item['chr'])
            item['utf_code'] = f"U+{cp:04X}"
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

    Ignore:
        import sys, ubelt
        from mathutf.symbols import *  # NOQA
        from mathutf.symbols import _compositions, _populate_class, _build_unicode_named_table, _show_all, _dev_map_to_latex, _dev_search_for_symbols
        _dev_map_to_latex()
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
