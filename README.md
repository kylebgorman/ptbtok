# Penn Treebank tokenizer

This is a simple fork of the famous Penn Treebank tokenizer. It is forked from
[DetectorMorse](https://github.com/cslu-nlp/DetectorMorse/blob/master/detectormorse/ptbtokenizer.py)
via
[NLTK](https://www.nltk.org/api/nltk.tokenize.html?highlight=nltk%20word_tokenize#nltk.tokenize.word_tokenize).

-   It is appropriate for English, **but not other languages**.
-   It is appropriate when applied one sentence at a time, **but should not be
    applied to paragraphs or documents**.

Unlike the NLTK equivalent, it has no (library or data) dependencies except the
built-in [`re`](https://docs.python.org/3/library/re.html). Unlike the NLTK
equivalent, it is not [hostilely
polymorphic](https://twitter.com/wellformedness/status/1385280329527742469).
