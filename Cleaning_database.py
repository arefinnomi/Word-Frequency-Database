import re

from orm.orm import *
from yandex.yandexhandler import get_translation

database.connect()

result_EnglishWord = EnglishWord.select().where(EnglishWord.text.regexp('\d+|^\w{0,2}$'))
for i, row_EnglishWord in enumerate(result_EnglishWord):
    row_EnglishWord.delete_instance(recursive=True)

result_BanglaWord = BanglaWord.select().where(BanglaWord.text.regexp("[A-za-z]+|^$"))
for row_BanglaWord in result_BanglaWord:

    word_bangla = row_BanglaWord.text
    result_Translation = Translation.select().where(Translation.bangla_word == row_BanglaWord.id)

    for row_Translation in result_Translation:
        word_english = EnglishWord.get(id=row_Translation.english_word)

        word_id = word_english.id
        have_traslation = Translation.select().where(Translation.english_word == word_id)

        if have_traslation.exists():
            continue

        new_bangla_word = get_translation(word_english.text)

        if not re.search("[A-za-z]+|^$", new_bangla_word):
            print word_english.text, ": ", word_bangla, ":", new_bangla_word
            bangla_word_id = add_bangla_word(new_bangla_word)[0].id
            add_translation(_english_word_id=word_id, _bangla_word_id=bangla_word_id)
    row_BanglaWord.delete_instance(recursive=True)
