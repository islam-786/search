class CollectionFinder:
    def __init__(self, tokens, intents, filters_intent):
        self.tokens = tokens
        self.intents = intents
        self.filters_intent = filters_intent

    def collection(self):
        query_collection = None

        # Format user query
        collection = next(
            (intent["name"] for intent in self.intents if intent["type"] == "collection"), None)

        # if collection is None then find collection from filters
        if collection is not None:
            query_collection = collection
        else:
            # Filter collections based on frequency
            filter_collections = {}

            # find filters collections and their frequencies
            for filter_intent in self.filters_intent:
                # if collection not exist add it otherwise increase the feq. number
                if filter_intent["collection"] not in filter_collections:
                    filter_collections[filter_intent["collection"]] = 1
                else:
                    filter_collections[filter_intent["collection"]] += 1

            # Find collection with high frequency
            try:
                query_collection = max(
                    filter_collections, key=filter_collections.get)
            except ValueError:
                query_collection = None

        # Check if still collection is None
        if query_collection is None:
            # if token is only one e.g (2:1) or (2-1)
            # then consider Quran as a collection
            if len(self.tokens) == 1:
                if ":" in self.tokens[0] or "-" in self.tokens[0]:
                    query_collection = "quran"

        return query_collection
