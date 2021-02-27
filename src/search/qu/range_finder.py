from .alpha_numbers import numeric_words, alpha_numbers


class RangeFinder:
    def __init__(self, tokens):
        self.tokens = tokens

    def query_range(self):
        # Find range format
        # e.g from to
        # e.g start end
        range_format = None

        # check "form" word exists in token
        from_word_index = None
        try:
            from_word_index = self.tokens.index("from")
        except ValueError:
            try:
                from_word_index = self.tokens.index("start")
            except ValueError:
                pass

        try:
            if from_word_index:
                range_format = {}

                # Check next word should be number
                next_token = self.tokens[from_word_index+1]
                if next_token.isnumeric() or next_token in numeric_words:
                    try:
                        range_format["from"] = int(next_token)
                    except ValueError:
                        range_format["from"] = next(
                            a["number"] for a in alpha_numbers if a["alpha"] == next_token)

                # Check next word should be "to" or "end"
                next_index = from_word_index + 2
                next_token = self.tokens[from_word_index+2]
                if next_token == "to" or next_token == "end":
                    next_index += 1

                # Check if next word is "end"
                next_token = self.tokens[next_index]
                if next_token == "end":
                    next_index += 1

                # Next world should be number
                next_token = self.tokens[next_index]
                if next_token.isnumeric() or next_token in numeric_words:
                    try:
                        range_format["to"] = int(next_token)
                    except ValueError:
                        range_format["to"] = next(
                            a["number"] for a in alpha_numbers if a["alpha"] == next_token)
        except:
            pass

        return range_format
