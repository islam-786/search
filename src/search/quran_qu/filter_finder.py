class FilterFinder:
    def __init__(self, tokens, numbers, query_intents):
        self.tokens = tokens
        self.numbers = numbers
        self.query_intents = query_intents

    def intents(self):
        # Founded numbers intent
        filters_intent = []

        # Find intent that are comming before numbers
        for number in self.numbers:
            for intent in self.query_intents:
                if intent["index"] == number["index"] - 1:
                    filter_intent = intent.copy()
                    filter_intent["number"] = number["number"]
                    filters_intent.append(filter_intent)
                    break

        self.filters_intent = filters_intent
        return filters_intent

    def filters(self):
        if not self.filters_intent:
            self.intents()

        filters = [{"name": filter_intent["name"], "number": filter_intent["number"]}
                   for filter_intent in self.filters_intent]

        # If filters None then check if any token contain (:) or (-)
        if not filters:
            for token in self.tokens:
                seperator = None

                if ":" in token:
                    seperator = ":"
                if "-" in token:
                    seperator = "-"

                if seperator:
                    parts = token.split(seperator)
                    # Consider first part is surah and second is ayah
                    filters = [
                        {
                            "name": "surah",
                            "number": parts[0]
                        },
                        {
                            "name": "ayah",
                            "number": parts[1]
                        }
                    ]

        return filters
