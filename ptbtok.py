"""Penn Treebank tokenizer, adapted from NLTK

This is a simple word tokenizer for English, adapted from NLTK's
`nltk.tokenize.treebank.py`, in turn adapted from an infamous sed script by
Robert McIntyre. Even ignoring the reduced import overhead, this is about half
again faster than the NLTK version; don't ask me why.

**Note that this is intended to be applied one sentence at a time.**

>>> s = '''Good muffins cost $3.88\\nin New York.  Please buy me\\ntwo of them.\\nThanks.'''
>>> tokenize(s)
['Good', 'muffins', 'cost', '$', '3.88', 'in', 'New', 'York.', 'Please', 'buy', 'me', 'two', 'of', 'them.', 'Thanks', '.']
>>> s = "They'll save and invest more."
>>> tokenize(s)
['They', "'ll", 'save', 'and', 'invest', 'more', '.']
"""

import re

from typing import List


RULES1 = [
    # Initial quotes.
    (r"^\"", r"``"),
    (r"(``)", r" \1 "),
    (r'([ (\[{<])"', r"\1 `` "),
    # Punctuation.
    (r"([:,])([^\d])", r" \1 \2"),
    (r"\.\.\.", r" ... "),
    (r"[;@#$%&]", r" \g<0> "),
    (r'([^\.])(\.)([\]\)}>"\']*)\s*$', r"\1 \2\3 "),
    (r"[?!]", r" \g<0> "),
    (r"([^'])' ", r"\1 ' "),
    # Parens, brackets, etc.
    (r"[\]\[\(\)\{\}\<\>]", r" \g<0> "),
    (r"--", r" -- "),
]

# Final quotes.
RULES2 = [(r'"', " '' "), (r"(\S)(\'\')", r"\1 \2 ")]

# All replaced with r"\1 \2 ".
CONTRACTIONS = [
    r"(?i)([^' ])('S|'M|'D|') ",
    r"(?i)([^' ])('LL|'RE|'VE|N'T) ",
    r"(?i)\b(CAN)(NOT)\b",
    r"(?i)\b(D)('YE)\b",
    r"(?i)\b(GIM)(ME)\b",
    r"(?i)\b(GON)(NA)\b",
    r"(?i)\b(GOT)(TA)\b",
    r"(?i)\b(LEM)(ME)\b",
    r"(?i)\b(MOR)('N)\b",
    r"(?i)\b(WAN)(NA) ",
    r"(?i) ('T)(IS)\b",
    r"(?i) ('T)(WAS)\b",
]


def tokenize(text: str) -> List[str]:
    """Splits string `text` into word tokens."""
    for (regexp, replacement) in RULES1:
        text = re.sub(regexp, replacement, text)
    # Adds extra space to make things easier.
    text = " " + text + " "
    for (regexp, replacement) in RULES2:
        text = re.sub(regexp, replacement, text)
    for regexp in CONTRACTIONS:
        text = re.sub(regexp, r"\1 \2 ", text)
    return text.split()


if __name__ == "__main__":
    import doctest
    doctest.testmod()

