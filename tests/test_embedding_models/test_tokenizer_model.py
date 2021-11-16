#!/usr/bin/python3

# test_tokenizer_model.py
# Date:  21.07.2021
# Author: Stratulat Ștefan
# Email: stefan.stratulat1997@gmail.com

from mfy_nlp_core.adapters.abstract_model import TokenizerModelABC
from mfy_nlp_core.adapters.embedding_models import BasicTokenizerModel, SpacyTokenizerModel
from mfy_nlp_core.services import nlp


def test_basic_tokenizer_model():
    tokenizer = BasicTokenizerModel()
    assert isinstance(tokenizer, TokenizerModelABC)
    text = 'sample text for this test'
    tokens = tokenizer.tokenize(text)
    assert len(tokens) == 5
    assert tokens[0] == 'sample'
    assert tokens[4] == 'test'


def test_spacy_tokenizer_model():
    tokenizer = SpacyTokenizerModel(spacy_tokenizer=nlp.tokenizer)
    assert isinstance(tokenizer, TokenizerModelABC)
    text = "Don't throw morphemes away"
    tokens = tokenizer.tokenize(text)
    assert len(tokens) == 5
    assert tokens[0] == 'Do'
    assert tokens[4] == 'away'
