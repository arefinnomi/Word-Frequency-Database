from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase

database = SqliteExtDatabase('dictionary.db', regexp_function=True)


class BaseModel(Model):
    class Meta:
        database = database


class EnglishWord(BaseModel):
    text = CharField(unique=True, null=False, index=True)


class Frequency(BaseModel):
    word = ForeignKeyField(EnglishWord, null=False, index=True)
    frequency = IntegerField(null=False)
    normalized_frequency = IntegerField(null=False)
    corpus_size = IntegerField(null=False)


class BanglaWord(BaseModel):
    text = CharField(unique=True, null=False, index=True)


class Translation(BaseModel):
    english_word = ForeignKeyField(EnglishWord, null=False, index=True)
    bangla_word = ForeignKeyField(BanglaWord, null=False)


class Synonym(BaseModel):
    word = ForeignKeyField(EnglishWord, index=True)
    synonym = ForeignKeyField(EnglishWord)
    wordnet_serial = IntegerField()


class Antonym(BaseModel):
    word = ForeignKeyField(EnglishWord, index=True)
    antonym = ForeignKeyField(EnglishWord)


def create_tables():
    with database:
        database.create_tables([EnglishWord, Frequency, Translation, Synonym, BanglaWord, Antonym])


def word_exist(_text):
    exist = EnglishWord.select().where(EnglishWord.text == _text)
    return exist


def get_id_word(_text):
    word = EnglishWord.get(EnglishWord.text == _text).id
    return word


def add_word(_text):
    english_word = EnglishWord.get_or_create(text=_text)
    return english_word


def add_frequency(_word_id, _frequency, _normalized_frequency, _corpus_size):
    frequency = Frequency.get_or_create(word=_word_id, frequency=_frequency, normalized_frequency=_normalized_frequency,
                                        corpus_size=_corpus_size)
    return frequency


def add_translation(_english_word_id, _bangla_word_id):
    translation = Translation.get_or_create(english_word=_english_word_id, bangla_word=_bangla_word_id)
    return translation


def add_synonym(_word_id, _synonym, _wordnet_serial):
    synonym = Synonym.get_or_create(word=_word_id, synonym=_synonym, defaults={'wordnet_serial': _wordnet_serial})
    return synonym


def add_antonym(_word_id, _antonym):
    antonym = Antonym.get_or_create(word=_word_id, antonym=_antonym)
    return antonym


def add_bangla_word(_text):
    bangla_word = BanglaWord.get_or_create(text=_text)
    return bangla_word
