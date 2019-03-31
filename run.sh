#!/usr/bin/env bash

# loading word
python ./ANC_Corpus.py
python ./BNC_corpus.py
python ./ENWIKI_corpus.py
python ./Google_corpus.py
python ./OpenSubtitles_corpus.py

#cleaning database
python ./Cleaning_database.py

#loading synonym
python ./fetching_synonym_antonym_wordnet.py

#loading translation
python ./fetching_translation_local_json.py
python ./fetching_translation_local_csv.py

#cleaning database
python ./Cleaning_database.py

shutdown -h 0
