from nltk import WordNetLemmatizer
from nltk.corpus import wordnet

text = "can"
lemmatizer = WordNetLemmatizer()

synSet = wordnet.synsets(text)
for i, syn in enumerate(wordnet.synsets(text)):
    for l in syn.lemmas():
        if lemmatizer.lemmatize(text) != lemmatizer.lemmatize(l.name()):
            synonym = l.name()
            #
            # if word_exist(synonym.lower()):
            #     synonym_id = get_id_word(synonym.lower())
            #     add_synonym(english_word.id, synonym_id)
            #     add_synonym(synonym_id, english_word.id)
            print text, synonym, i
        if l.antonyms():
            ant = l.antonyms()
            antonym = l.antonyms()[0].name()

            # if word_exist(antonym.lower()):
            #     antonym_id = get_id_word(antonym.lower())
            #     add_antonym(english_word.id, antonym_id)
            #     add_antonym(antonym_id, english_word.id)
            print "ant: ", antonym
    print



