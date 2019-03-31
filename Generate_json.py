import codecs
import json

from orm.orm import EnglishWord, database, Frequency, BanglaWord, Translation, Synonym, Antonym

database.connect()
englishWords = EnglishWord.select()
data = {}
for i, englishWord in enumerate(englishWords):
    # if i == 10000:
    #     break
    values = {}

    # find relative frequency
    total_frequency = 0
    frequencies = Frequency.select().where(Frequency.word == englishWord)
    cont = 0
    for frequency in frequencies:
        cont += 1
        total_frequency += frequency.normalized_frequency
    total_frequency /= cont
    values["freq"] = total_frequency

    banglaWord_list = []
    banglaWords = BanglaWord.select().join(Translation).where(Translation.english_word == englishWord)
    for banglaWord in banglaWords:
        banglaWord_list.append(banglaWord.text)
    values['bn'] = banglaWord_list

    synonym_list = {}
    synonyms = Synonym.select().where(Synonym.word == englishWord)
    for synonym in synonyms:
        synonymWords = EnglishWord.select().where(EnglishWord.id == synonym.synonym)
        for synonymWord in synonymWords:
            synonym_list[synonymWord.text] = synonym.wordnet_serial
    values['syn'] = synonym_list
    data[englishWord.text] = values

    antonym_list = []
    antonyms = Antonym.select().where(Antonym.word == englishWord)
    for antonym in antonyms:
        antonymWords = EnglishWord.select().where(EnglishWord.id == antonym.antonym)
        for antonymWord in antonymWords:
            antonym_list.append(antonymWord.text)
    values['ant'] = antonym_list
    data[englishWord.text] = values

with codecs.open('/home/bigdaddy/AndroidStudioProjects/SpellingFrequency/app/src/main/assets/dictionary.json', 'w',
                 encoding='utf-8') as outputFile:
    json.dump(data, outputFile, indent=4, ensure_ascii=False)

# with open('dictionary.json', 'wb') as outfile:
#     outfile.write(data[0]['bn'][0].encode('utf8'))
