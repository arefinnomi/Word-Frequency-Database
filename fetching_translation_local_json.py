import json
import re

from models.ProgressTimer import ProgressTimer
from orm.orm import *

create_tables()

input_file = file("source/translation/dictionary_cracked_min_garbage.json", "r")

translations = json.loads(input_file.read().decode("utf-8-sig"))

runtime = ProgressTimer(len(translations))

for translation in translations:

    runtime.increase_process(1)
    print "fetching_translation_local_json.py:", runtime

    word = translation['english'].lower()
    if not word_exist(word):
        continue
    word_id = get_id_word(word)

    for synonym in translation['synonyms']:
        if not word_exist(synonym.lower()):
            continue
        synonym_id = get_id_word(synonym.lower())
        add_synonym(word_id, synonym_id)
        add_synonym(synonym_id, word_id)

    # bangla = translation['bangles'].strip()
    #
    # if not re.search("^[A-Za-z\s]+$|^$", bangla):
    #     bangla_word_id = add_bangla_word(bangla)[0].id
    #     add_translation(_english_word_id=word_id, _bangla_word_id=bangla_word_id)

    for bn_synonym in translation['bangles']:

        trimmed_bn_synonym = bn_synonym.strip()

        if not re.search("^[A-Za-z\s]+$|^$", trimmed_bn_synonym):
            bangla_word_id = add_bangla_word(trimmed_bn_synonym)[0].id
            add_translation(_english_word_id=word_id, _bangla_word_id=bangla_word_id)

