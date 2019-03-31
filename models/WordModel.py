class WordModel(object):

    def __init__(self, lemma, frequency, corpus_size):
        self.lemma = lemma
        self.frequency = int(frequency)
        self.corpus_size = int(corpus_size)
        self.normalized_frequency = self.frequency * 10000000000000 / self.corpus_size

    def __eq__(self, other):
        return self.lemma == other.lemma

    def __hash__(self):
        return hash(self.lemma)

    def __str__(self):
        return str((self.lemma, self.frequency))

    def __repr__(self):
        return str(self)
