from textdistance import levenshtein
from .stop_words import stop_words


class IntentFinder:
    def __init__(self, tokens, intent_list):
        self.tokens = tokens
        self.intent_list = intent_list
        self.score = 0

    def intents(self):
        # Founded intent in query
        query_intents = []

        # Search intent from tokens
        for intent in self.intent_list:
            for index, token in enumerate(self.tokens):
                if token in intent["words"]:
                    query_intent = intent.copy()
                    query_intent["value"] = token
                    query_intent["index"] = index
                    query_intents.append(query_intent)
                    # Calculate confidence
                    self.score += 5

        # Those tokens which intents are not found
        left_tokens = []

        for index, token in enumerate(self.tokens):
            found = False
            for intent in query_intents:
                if token == intent["value"]:
                    found = True
                    break

            if not found:
                t = {
                    "word": token,
                    "index": index
                }
                left_tokens.append(t)

        # remove stop words from left tokens
        cleaned_tokens = []
        if left_tokens:
            cleaned_tokens = [
                t for t in left_tokens if t["word"] not in stop_words]

        # If there are some tokens left then
        # find those intents which are based on levenshtein distance
        for token in cleaned_tokens:
            intents = []
            for intent in self.intent_list:
                for word in intent["words"]:
                    if len(word) <= 3:
                        continue

                    max_distance = 1

                    if len(word) <= 5:
                        max_distance = 1
                    else:
                        max_distance = 2

                    d = levenshtein.distance(token["word"], word)
                    if d <= max_distance:
                        i = {}
                        i["intent"] = intent.copy()
                        i["distance"] = d
                        intents.append(i)
                        break

            if intents:
                min_distance_intent = min(intents, key=lambda i: i["distance"])
                i = min_distance_intent["intent"]
                i["value"] = token["word"]
                i["index"] = token["index"]
                query_intents.append(i)

                # Calculate confidence
                self.score += 5 - (min_distance_intent["distance"] + 1)

        return query_intents
