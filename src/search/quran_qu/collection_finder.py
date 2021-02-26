class CollectionFinder:
    def __init__(self, intents, filters_intent):
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

        return query_collection

        # Check if still collection is None
        # if formated_query["collection"] is None:
        #     print(tokens)
