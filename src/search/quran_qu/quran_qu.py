from .quran_intents import quran_intents
from .tokenizer import Tokenizer
from .intent_finder import IntentFinder
from .number_finder import NumberFinder
from .filter_finder import FilterFinder
from .collection_finder import CollectionFinder


class QuranQU:
    def analyze(self, query, debug):
        # Tokenize query
        tokenizer = Tokenizer(query)
        tokens = tokenizer.tokens()

        # Find query intents
        intent_finder = IntentFinder(tokens)
        intents = intent_finder.intents()

        # Find query numbers
        number_finder = NumberFinder(tokens)
        numbers = number_finder.numbers()

        # Find filter intents and filters
        filter_finder = FilterFinder(tokens, numbers, intents)
        filters_intent = filter_finder.intents()
        filters = filter_finder.filters()

        # Find query collection
        collection_finder = CollectionFinder(intents, filters_intent)
        collection = collection_finder.collection()

        formated_query = {
            "collection": collection,
            "filters": filters
        }

        if debug:
            formated_query["debug"] = {
                "tokens": tokens,
                "intents": intents,
                "numbers": numbers,
                "filters_intent": filters_intent,
                "filters": filters
            }

        return formated_query
