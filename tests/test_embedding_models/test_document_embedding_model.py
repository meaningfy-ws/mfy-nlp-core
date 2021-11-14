#!/usr/bin/python3

# test_document_embedding_model.py
# Date:  08.09.2021
# Author: Stratulat Ștefan
# Email: stefan.stratulat1997@gmail.com

from mfy_nlp_core.adapters.embedding_models import TfIdfDocumentEmbeddingModel, BasicSentenceSplitterModel, UniversalSentenceEmbeddingModel


def test_tfidf_document_embedding_model():
    doc_emb_model = TfIdfDocumentEmbeddingModel(sent_emb_model=UniversalSentenceEmbeddingModel(),
                                                sent_splitter=BasicSentenceSplitterModel(),
                                                top_k=10)
    documents = ["As part of human exploration of the Moon, numerous space missions have been undertaken to study Earth's natural satellite.",
                 "Of the Moon landings, Luna 2 of the Soviet Union was the first spacecraft to reach its surface successfully, intentionally impacting the Moon on 13 September 1959.",
                 "In 1966, Luna 9 became the first spacecraft to achieve a controlled soft landing, while Luna 10 became the first mission to enter orbit. "]
    doc_emb = doc_emb_model.encode(documents)
    assert len(doc_emb) == len(documents)

