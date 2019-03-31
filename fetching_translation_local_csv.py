import csv
import re
from string import strip

from models.ProgressTimer import ProgressTimer
from orm.orm import get_id_word, add_bangla_word, add_translation, create_tables, Translation, EnglishWord

create_tables()
rows = []

with open('source/translation/words.csv', 'rb') as csvFile:
    bengaliDictionary_csv_reader = csv.reader(csvFile, delimiter=',', quotechar='\"')
    rows.extend(list(bengaliDictionary_csv_reader))

english_words_with_translation = Translation.select(Translation.english_word)
# select_english_words = EnglishWord.select().where(EnglishWord.id.not_in(english_words_with_translation))
select_english_words = EnglishWord.select()
english_words = [english_word.text for english_word in select_english_words]

runtime = ProgressTimer(len(rows))

for row in rows:
    runtime.increase_process(1)
    print "fetching_translation_local_csv.py:", runtime

    english_word = strip(row[0]).lower()
    bangla_word_list = row[1].split(",")

    if english_word in english_words:

        word_id = get_id_word(english_word)
        for bangla_word in bangla_word_list:
            if not re.search("^[A-Za-z\s]+$|^$", bangla_word):
                bangla_word_id = add_bangla_word(bangla_word)[0].id
                add_translation(_english_word_id=word_id, _bangla_word_id=bangla_word_id)

            print english_word, bangla_word
