alpha_numbers = [
    {
        "alpha": "one",
        "number": 1
    },
    {
        "alpha": "two",
        "number": 2
    },
    {
        "alpha": "three",
        "number": 3
    },
    {
        "alpha": "four",
        "number": 4
    },
    {
        "alpha": "five",
        "number": 5
    },
    {
        "alpha": "six",
        "number": 6
    },
    {
        "alpha": "seven",
        "number": 7
    },
    {
        "alpha": "eight",
        "number": 8
    },
    {
        "alpha": "nine",
        "number": 9
    },
    {
        "alpha": "ten",
        "number": 10
    },
    {
        "alpha": "first",
        "number": 1
    },
    {
        "alpha": "second",
        "number": 2
    },
    {
        "alpha": "third",
        "number": 3
    },
    {
        "alpha": "fourth",
        "number": 4
    },
    {
        "alpha": "fifth",
        "number": 5
    },
    {
        "alpha": "sixth",
        "number": 6
    },
    {
        "alpha": "seventh",
        "number": 7
    },
    {
        "alpha": "eighth",
        "number": 8
    },
    {
        "alpha": "ninth",
        "number": 9
    },
    {
        "alpha": "tenth",
        "number": 10
    }
]


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

        return query_numbers
