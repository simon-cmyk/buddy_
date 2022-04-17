from target import target


class daily_input(target):
    def __init__(self, text, rating):
        super().__init__(self, "daily_input.yaml", 1000000, text, rating, "fun for the future")