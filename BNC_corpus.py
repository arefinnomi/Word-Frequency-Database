import csv
import re
from string import strip

from nltk.corpus import wordnet

from models.ProgressTimer import ProgressTimer
from models.CorpusDict import CorpusDict
from models.WordModel import WordModel
from orm.orm import *

corpus_size = 1000000
BNC_corpus = CorpusDict()

with open('source/corpus/BNC 1_1_all_alpha.csv', 'rb') as BNC_csvFile:
    BNC_csv_reader = csv.reader(BNC_csvFile, delimiter=',', quotechar='\"')

    for row in BNC_csv_reader:
        first_cell = True
        if row[0] == '@' and row[1] == '@':
            continue

        word = WordModel(strip(row[0]).lower(), row[3], corpus_size)
        BNC_corpus.add(word)
    BNC_csvFile.close()

wn_lemmas = set(wordnet.all_lemma_names())

create_tables()

words = BNC_corpus.get_all_words_list()

runtime = ProgressTimer(len(words))

for word in words:

    if word.lemma in wn_lemmas:

        if re.match(r'\d+|^\w{0,2}$', word.lemma):
            continue

        word_id = add_word(word.lemma)[0]
        frequency_id = add_frequency(_word_id=word_id, _frequency=word.frequency, _corpus_size=word.corpus_size,
                                     _normalized_frequency=word.normalized_frequency)

    runtime.increase_process(1)
    print "BNC_corpus.py:", runtime
