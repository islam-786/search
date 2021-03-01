from search.qu import QU
from .hadith_intents import hadith_intents


class HadithQU:
    def analyze(self, query, debug=False):
        qu = QU(hadith_intents)

        # Replace # symbol with space
        query = query.replace("#", " ")

        # Replace word "number" fom query
        query = query.replace("number", " ").replace(
            "num", " ").replace("no.", " ").replace("no", " ")

        # Remove hadith prefix
        query = query.replace("-", " ").replace("sahih",
                                                " ").replace("sunan", " ")

        return qu.analyzer(query, debug)
