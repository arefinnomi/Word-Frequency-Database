from WordModel import WordModel


class CorpusDict:

    def __init__(self):
        self.words = dict()

    def add(self, _word):
        if _word.lemma not in self.words:
            self.words[_word.lemma] = WordModel(_word.lemma, _word.frequency, _word.corpus_size)
        else:
            self.words[_word.lemma].frequency += _word.frequency
            self.words[_word.lemma].normalized_frequency \
                = self.words[_word.lemma].frequency * 10000000000000 / self.words[_word.lemma].corpus_size

    def get_all_words_list(self):
        return self.words.values()
