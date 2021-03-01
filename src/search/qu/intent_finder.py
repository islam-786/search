from textdistance import levenshtein


class IntentFinder:
    def __init__(self, tokens, intent_list):
        self.tokens = tokens
        self.intent_list = intent_list

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
            stop_words = ["from", "of", "in", "on",
                          "the", "to", "start", "starting", "last", "end", "ending"]
            cleaned_tokens = [
                t for t in left_tokens if t["word"] not in stop_words]

        # If there are some tokens left then
        # find those intents which are levenshtein distance
        # is less than 3
        for token in cleaned_tokens:
            intents = []
            for intent in self.intent_list:
                for word in intent["words"]:
                    d = levenshtein.distance(token["word"], word)
                    if d < 3:
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

        return query_intents
