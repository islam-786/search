from search.qu import QU
from .quran_intents import quran_intents


class QuranQU:
    def analyze(self, query, debug=False):
        qu = QU(quran_intents, ["ayah"])
        return qu.analyzer(query, debug)
