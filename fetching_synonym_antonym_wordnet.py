from nltk import WordNetLemmatizer
from nltk.corpus import wordnet

from models.ProgressTimer import ProgressTimer
from orm.orm import create_tables, EnglishWord, word_exist, get_id_word, add_synonym, add_antonym, Synonym

create_tables()

english_words_with_synonyms = Synonym.select(Synonym.word)
# select_english_words = EnglishWord.select().where(EnglishWord.id.not_in(english_words_with_synonyms))
select_english_words = EnglishWord.select()

lemmatizer = WordNetLemmatizer()


runtime = ProgressTimer(select_english_words.count())


for english_word in select_english_words:

    runtime.increase_process(1)
    print "fetching_synonym_antonym_wordnet.py:", runtime

    for wordnetSerial, syn in enumerate(wordnet.synsets(english_word.text)):
        for l in syn.lemmas():
            synonym = l.name().lower()
            if lemmatizer.lemmatize(english_word.text) != lemmatizer.lemmatize(
                    synonym) and english_word.text != synonym and word_exist(synonym):
                    synonym_id = get_id_word(synonym)
                    add_synonym(english_word.id, synonym_id, wordnetSerial+1)
                    # add_synonym(synonym_id, english_word.id)

            if l.antonyms():
                antonym = l.antonyms()[0].name().lower()
                if lemmatizer.lemmatize(english_word.text) != lemmatizer.lemmatize(
                        antonym) and english_word.text != antonym and word_exist(antonym):
                        antonym_id = get_id_word(antonym)
                        add_antonym(english_word.id, antonym_id)
                        # add_antonym(antonym_id, english_word.id)


