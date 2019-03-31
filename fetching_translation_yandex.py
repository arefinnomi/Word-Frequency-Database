import re


from models.ProgressTimer import ProgressTimer
from orm.orm import *
from yandex.yandexhandler import get_translation

create_tables()

english_words_with_translation = Translation.select(Translation.english_word)
select_english_words = EnglishWord.select().where(EnglishWord.id.not_in(english_words_with_translation))
english_words = [english_word for english_word in select_english_words]

runtime = ProgressTimer(len(english_words))
for english_word in english_words:

    bangla_word = get_translation(english_word.text)
    word_id = english_word.id

    print english_word.text, ": ", bangla_word

    if not re.search("^[A-Za-z\s]+$|^$", bangla_word):
        bangla_word_id = add_bangla_word(bangla_word)[0].id
        add_translation(_english_word_id=word_id, _bangla_word_id=bangla_word_id)

    runtime.increase_process(1)
    print "fetching_translation_yandex.py:", runtime
