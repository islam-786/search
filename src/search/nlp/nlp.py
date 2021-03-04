from .quran_qu import QuranQU
from .hadith_qu import HadithQU


class NLP:
    @classmethod
    def analyze(cls, query):
        quran_qu = QuranQU()
        q = quran_qu.analyze(query)

        hadith_qu = HadithQU()
        h = hadith_qu.analyze(query)

        if q["score"] >= h["score"]:
            return q
        else:
            return h
