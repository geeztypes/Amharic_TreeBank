# Summary

The GeezTypes Amharic UD treebank is .


# Introduction

The treebank consists of 87,913 sentences (1.5 M tokens) and its domain is
mainly newswire. The treebank is licensed under the terms of
[CC BY-NC-SA 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/)
and its original (non-UD) version can be downloaded from
[]().

# Acknowledgments

## References



# Domains and Data Split

NOTE: Earlier releases of the treebank had four training data files. This was
due to Github restrictions on file size. We have now re-joined the training
files in the official release package (beginning with UD v1.3), so there is
just one training file as in all other languages, and it is named
cs-ud-train.conllu. The four files in previous releases corresponded to the
four sources of the original texts; the sources may still be distinguished,
if desirable, by the prefixes of sentence ids. All of them are newspapers, but

* l (ln) and m (mf) are mainstream daily papers (news, commentaries, but also
  sports results and TV programs)
* c (cmpr) is a business weekly
* v (vesm) contains popular scientific articles (the hardest to parse: long
  sentences and unusual vocabulary)

The dev and test sets contain all four sources and their size is proportional
to the sizes of the respective training parts.


## Source of annotations

This table summarizes the origins and checking of the various columns of the CoNLL-U data.

| Column | Status |
| ------ | ------ |
| ID | Sentence segmentation and (surface) tokenization was automatically done and then hand-corrected; |
| FORM |  |
| LEMMA | Manual selection from possibilities provided by morphological analysis: two annotators and then an arbiter. PDT-to-UD conversion stripped from lemmas the ID numbers distinguishing homonyms, semantic tags and comments; this information is preserved as attributes in the MISC column. |
| UPOSTAG | Converted automatically from XPOSTAG, from the semantic tags in PDT lemma, and occasionally from other information available in the treebank; human checking of patterns revealed by automatic consistency tests. |
| XPOSTAG | Manual selection from possibilities provided by morphological analysis: two annotators and then an arbiter. |
| FEATS | Converted automatically from XPOSTAG, from the semantic tags in PDT lemma, and occasionally from other information available in the treebank; human checking of patterns revealed by automatic consistency tests. |
| HEAD | Original PDT annotation is manual, done by two independent annotators and then an arbiter. Automatic conversion to UD; human checking of patterns revealed by automatic consistency tests. |
| DEPREL | Original PDT annotation is manual, done by two independent annotators and then an arbiter. Automatic conversion to UD; human checking of patterns revealed by automatic consistency tests. |
| DEPS | &mdash; (currently unused) |
| MISC | Information about token spacing taken from PDT annotation. Lemma / word sense IDs, semantic tags and comments on meaning moved here from the PDT lemma. |


# Changelog

* 2021-02-01 v2.7
  * Created news crawler
  * auto generated conllu
  * cleaned up conllu
  * trained tagger and ner




<pre>
=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v1.0
License: CC BY-NC-SA 3.0
Includes text: yes
Genre: news reviews nonfiction
Lemmas: converted from manual
UPOS: converted from manual
XPOS: manual native
Features: converted from manual
Relations: converted from manual
Contributors: Josiah Solomon
Contributing: elsewhere
Contact: yosiasz@gmail.com
===============================================================================
</pre>
A description of the treebank and its origin (creation method, data sources, etc.)
A description of how the data was split into training, development and test sets
If there are multiple genres/domains, can they be told apart by sentence ids? Does the treebank consist of complete documents, or just randomly shuffled sentences?
Acknowledgments and references that should be cited when using the treebank
A changelog section for treebanks that will be released for the second (or subsequent) time
A machine-readable section with treebank metadata. This is described below.
