#!/usr/bin/python3

# test_document_embedding_model.py
# Date:  08.09.2021
# Author: Stratulat Ștefan
# Email: stefan.stratulat1997@gmail.com

from mfy_nlp_core.adapters.embedding_models import TfIdfDocumentEmbeddingModel, BasicSentenceSplitterModel, UniversalSentenceEmbeddingModel
from tests.test_embedding_models import DOCUMENTS


def test_tfidf_document_embedding_model():
    doc_emb_model = TfIdfDocumentEmbeddingModel(sent_emb_model=UniversalSentenceEmbeddingModel(),
                                                sent_splitter=BasicSentenceSplitterModel(),
                                                top_k=10)
    documents = DOCUMENTS
    doc_emb = doc_emb_model.encode(documents)
    assert len(doc_emb) == len(documents)

