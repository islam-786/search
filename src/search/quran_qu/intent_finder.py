from .quran_intents import quran_intents


class IntentFinder:
    def __init__(self, tokens):
        self.tokens = tokens

    def intents(self):
        # Founded intent in query
        query_intents = []

        # Search intent from tokens
        for intent in quran_intents:
            for index, token in enumerate(self.tokens):
                if token in intent["words"]:
                    query_intent = intent.copy()
                    query_intent["value"] = token
                    query_intent["index"] = index
                    query_intents.append(query_intent)

        return query_intents
