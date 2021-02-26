class FilterFinder:
    def __init__(self, numbers, query_intents):
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
        return filters
