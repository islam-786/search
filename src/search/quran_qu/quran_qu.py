from search.qu import QU
from .quran_intents import quran_intents


class QuranQU:
    def analyze(self, query, debug=False):
        qu = QU(quran_intents, ["ayah"])

        # Replace # symbol with space
        query = query.replace("#", " ")

        # Replace word "number" fom query
        query = query.replace("number", " ").replace(
            "num", " ").replace("no.", " ").replace("no", " ")

        return qu.analyzer(query, debug)
