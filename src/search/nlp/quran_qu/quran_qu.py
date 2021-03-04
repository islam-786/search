from search.nlp.qu import QU
from .quran_intents import quran_intents


class QuranQU:
    def analyze(self, query, debug=False):
        qu = QU(quran_intents, "quran", ["ayah"])

        # Replace # symbol with space
        query = query.replace("#", " ")

        # Replace word "number" fom query
        query = query.replace("number", " ").replace(
            "num", " ").replace("no.", " ").replace("no", " ")

        # Remove "al" from query e.g surah-al-baqarah
        query = query.replace("-al-", " al-").replace("-ul-", " al-")

        return qu.analyzer(query, debug)
