from target import target


class daily_input(target):
    def __init__(self, hope, fear, general, rating):
        super().__init__("daily_input.yaml", 1000000, (hope, fear, general), rating, "fun for the future")
