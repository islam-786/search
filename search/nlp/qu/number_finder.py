from .alpha_numbers import alpha_numbers, numeric_words


class NumberFinder:
    def __init__(self, tokens):
        self.tokens = tokens
        self.score = 0

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

                # Calculate confident
                self.score += 15
            except ValueError:
                for alpha_number in alpha_numbers:
                    if token == alpha_number["alpha"]:
                        query_numbers.append({
                            "index": index,
                            "number": alpha_number["number"]
                        })
                        # Calculate confident
                        self.score += 15

                # Check next token is not a number
                # if it is a number it might be a limit
                # e.g surah 3 first 5 ayahs
                # next_token = self.tokens[index+1]

                # if not next_token.isnumeric() and next_token not in numeric_words:
                #     query_numbers.append({
                #         "index": index,
                #         "number": alpha_number["number"]
                #     })

        return query_numbers
