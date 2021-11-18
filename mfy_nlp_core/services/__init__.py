import spacy

SPACY_MODEL_NAME = "en_core_web_md"

try:
    nlp = spacy.load(SPACY_MODEL_NAME)
except:
    print(f'Download {SPACY_MODEL_NAME}...')
    from spacy.cli import download
    download(SPACY_MODEL_NAME)
    nlp = spacy.load(SPACY_MODEL_NAME)
    print('Done')