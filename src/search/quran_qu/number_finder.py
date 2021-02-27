from .alpha_numbers import alpha_numbers


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
                for alpha_number in alpha_numbers:
                    if token == alpha_number["alpha"]:
                        query_numbers.append({
                            "index": index,
                            "number": alpha_number["number"]
                        })
                        # Check next token is not a number
                        # if it is a number it might be a limit
                        # e.g surah 3 first 5 ayahs
                        # next_token = self.tokens[index+1]
                        # alpha_words = [a["alpha"] for a in alpha_numbers]

                        # if not next_token.isnumeric() and next_token not in alpha_words:
                        #     query_numbers.append({
                        #         "index": index,
                        #         "number": alpha_number["number"]
                        #     })

        return query_numbers
