import enum

class RatingChoice(enum.Enum):
        UNRATED = 0.0
        TERRIBLE = 0.5
        BAD = 1.0
        DULL = 1.5
        BORING = 2
        FINE = 2.5
        AVERAGE = 3
        GOOD = 3.5
        EXCELLENT = 4
        AMAZING = 4.5
        PERFECT = 5.0