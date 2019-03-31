import csv
import re
from string import strip

from nltk.corpus import wordnet

from models.ProgressTimer import ProgressTimer
from models.CorpusDict import CorpusDict
from models.WordModel import WordModel
from orm.orm import create_tables, add_word, add_frequency

corpus_size = 22162602
ANC_corpus = CorpusDict()

with open('source/corpus/ANC-all-lemma.csv', 'rb') as ANC_csvFile:
    ANC_csv_reader = csv.reader(ANC_csvFile, delimiter=',', quotechar='\"')

    for row in ANC_csv_reader:
        word = WordModel(strip(row[1]).lower(), row[3], corpus_size)
        ANC_corpus.add(word)

wn_lemmas = set(wordnet.all_lemma_names())

create_tables()

words = ANC_corpus.get_all_words_list()

runtime = ProgressTimer(len(words))

for word in words:

    if word.lemma in wn_lemmas:
        if re.match(r'\d+|^\w{0,2}$', word.lemma):
            continue

        word_id = add_word(word.lemma)[0]
        frequency_id = add_frequency(_word_id=word_id, _frequency=word.frequency, _corpus_size=word.corpus_size,
                                     _normalized_frequency=word.normalized_frequency)

    runtime.increase_process(1)
    print "ANC_corpus.py:", runtime
