from textdistance import levenshtein
from .alpha_numbers import numeric_words


class LimitFinder:
    def __init__(self, tokens, filters_intent):
        self.tokens = tokens
        self.filters_intent = filters_intent
        self.score = 0

    def intent(self):
        direction = "start"
        limit_index = None

        # if there is "first" word before or after number
        for index, token in enumerate(self.tokens):
            if (token == "first" and
                        (self.tokens[index + 1].isnumeric() or
                         self.tokens[index + 1] in numeric_words)
                    ):
                # This is the limit e.g first 5 ayahs
                limit_index = index + 1
                direction = "start"
                # calculate confidence
                self.score += 5

            elif (token == "last" and
                    (self.tokens[index + 1].isnumeric() or
                     self.tokens[index + 1] in numeric_words)
                  ):
                # This is the limit e.g last 5 ayahs
                limit_index = index + 1
                direction = "end"
                # calculate confidence
                self.score += 5

        # if any limit index found
        if limit_index:
            # Get filter intent
            limit_intent = next((
                filter_intent for filter_intent in self.filters_intent
                if filter_intent["number_index"] == limit_index), None)

            if limit_intent:
                limit_intent["direction"] = direction

            return limit_intent

        # Special case only to get last ayah of surah
        # e.g surah 2 last ayah
        for index, token in enumerate(self.tokens):
            if token == "last":
                special_limit_intent = {
                    "name": "ayah",
                    "collection": "quran",
                    "type": "special-limit-for-last-ayah",
                    "value": "ayah",
                    "number": 1,
                    "direction": "end",
                    "index": -1,
                    "number_index": -1
                }

                next_token = self.tokens[index + 1]
                words = ["ayah", "ayat", "ayahs"]

                # Check if next token is in these words
                if next_token in words:
                    # calculate confidence
                    self.score += 30
                    return special_limit_intent

                # if next token is not in these words then check it with distance
                for word in words:
                    d = levenshtein.distance(next_token, word)
                    if d < 2:
                        # calculate confidence
                        self.score += 20
                        return special_limit_intent

        return None
