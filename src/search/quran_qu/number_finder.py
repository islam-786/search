class NumberFinder:
    def __init__(self, tokens):
        self.tokens = tokens

    def numbers(self):
        # Founded query numbers
        query_numbers = []

        # search numbers in query
        for index, token in enumerate(self.tokens):
            try:
                number = int(token)
                query_numbers.append({
                    "index": index,
                    "number": number
                })
            except ValueError:
                pass

        return query_numbers
