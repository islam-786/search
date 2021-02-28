class Tokenizer:
    def __init__(self, query):
        self.query = query

    def tokens(self):
        query = self.query

        # Replace extra white spaces from query
        query = " ".join(query.split())

        # Lowercase and split
        tokens = query.lower().split(" ")
        return tokens
