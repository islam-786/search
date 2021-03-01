class FilterFinder:
    def __init__(self, tokens, numbers, query_intents):
        self.tokens = tokens
        self.numbers = numbers
        self.query_intents = query_intents

    def intents(self):
        # Founded numbers intent
        filters_intent = []

        # Get Pre define filters
        for intent in self.query_intents:
            if intent["type"] == "pre_define_filter":
                filters_intent.append(intent)

        # Find intent that are comming before numbers
        for number in self.numbers:
            for intent in self.query_intents:
                if intent["index"] == number["index"] - 1:
                    filter_intent = intent.copy()
                    filter_intent["number"] = number["number"]
                    filter_intent["number_index"] = number["index"]
                    filters_intent.append(filter_intent)
                    break

        # if filters intent and number length is not same this
        # mean some numbers left and need to find the intents for them
        if len(filters_intent) != len(self.numbers):
            numbers_left = []
            for number in self.numbers:
                found = False
                for intent in filters_intent:

                    # Pass pre define filters
                    if intent["type"] == "pre_define_filter":
                        found = True
                        break

                    if number["index"] == intent["number_index"]:
                        found = True
                        break

                if not found:
                    numbers_left.append(number)

            # Find intent that are comming after numbers
            for number in self.numbers:
                for intent in self.query_intents:
                    if intent["index"] == number["index"] + 1:
                        filter_intent = intent.copy()
                        filter_intent["number"] = number["number"]
                        filter_intent["number_index"] = number["index"]
                        filters_intent.append(filter_intent)
                        break

        return filters_intent

    def filters(self, filters_intent):

        filters = [{"name": filter_intent["name"], "number": filter_intent["number"]}
                   for filter_intent in filters_intent]

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
                    try:
                        filters = [
                            {
                                "name": "surah",
                                "number": int(parts[0])
                            },
                            {
                                "name": "ayah",
                                "number": int(parts[1])
                            }
                        ]
                    except ValueError:
                        pass

        return filters
