from .tokenizer import Tokenizer
from .intent_finder import IntentFinder
from .number_finder import NumberFinder
from .filter_finder import FilterFinder
from .limit_finder import LimitFinder
from .range_finder import RangeFinder
from .collection_finder import CollectionFinder


class QU:
    def __init__(self, query_intents, caller, remove_filters=[]):
        """Initialize the QU

        query_intents: Provide query intents
        remove_filters: Provide list of names which need to remove when limit or range
                        found eg. ayah
        """
        self.query_intents = query_intents
        self.remove_filters = remove_filters
        self.caller = caller

    def analyzer(self, query, debug=False):
        scores = 0
        # formated query
        formated_query = {"_debug": {}}

        # Tokenize query
        tokenizer = Tokenizer(query)
        tokens = tokenizer.tokens()

        # Find query intents
        intent_finder = IntentFinder(tokens, self.query_intents)
        intents = intent_finder.intents()

        scores += intent_finder.score

        # Find query numbers
        number_finder = NumberFinder(tokens)
        numbers = number_finder.numbers()

        scores += number_finder.score

        # Find filter intents
        filter_finder = FilterFinder(tokens, numbers, intents, self.caller)
        filters_intent = filter_finder.intents()

        if debug:
            formated_query["_debug"]["filters_intent_before_limit"] = filters_intent

        # Find limit
        limit_finder = LimitFinder(tokens, filters_intent)
        limit_intent = limit_finder.intent()

        scores += limit_finder.score

        # if limit intent found than remove this intent from filters intent
        if limit_intent:
            filters_intent = [
                i for i in filters_intent if i["index"] != limit_intent["index"]]

        # if limit intent found remove any ayah intent from filters intent
        if limit_intent and self.remove_filters:
            filters_intent = [
                i for i in filters_intent if i["name"] not in self.remove_filters]

        if debug:
            formated_query["_debug"]["filters_intent_before_range"] = filters_intent

        # Find Range
        range_finder = RangeFinder(tokens)
        query_range = range_finder.query_range()

        scores += range_finder.score

        # if Query Range found than remove the ayah intent from filters
        if query_range and self.remove_filters:
            filters_intent = [
                i for i in filters_intent if i["name"] not in self.remove_filters]

            # Add query range into formated query
            formated_query["range"] = query_range

        # Find filters
        filters = filter_finder.filters(filters_intent)

        scores += filter_finder.score

        # Find query collection
        collection_finder = CollectionFinder(tokens, intents, filters_intent)
        collection = collection_finder.collection()

        scores += collection_finder.score

        formated_query["confidence"] = scores
        formated_query["collection"] = collection
        formated_query["filters"] = filters

        if limit_intent:
            formated_query["limit"] = {
                "name": limit_intent["name"],
                "number": limit_intent["number"],
                "direction": limit_intent["direction"]
            }

        if debug:
            formated_query["_debug"]["token"] = tokens
            formated_query["_debug"]["intents"] = intents
            formated_query["_debug"]["numbers"] = numbers
            formated_query["_debug"]["filters_intent"] = filters_intent
            formated_query["_debug"]["limit"] = limit_intent

        return formated_query
