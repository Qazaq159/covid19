from covid19dh import covid19
import datetime
import pandas as pd
import random


class Covid19:
    country = ['USA', 'ITALY', 'RUSSIA', 'KAZAKHSTAN', 'UZBEKISTAN',  "JAPAN", 'GB', 'GERMANY']


    def __init__(self):
        self.choice = random.choice(self.country)
        xx, src = covid19(self.choice, verbose=False)
        df = pd.DataFrame(xx)

        self.data = {
            "country": self.choice,
            "confirmed": df['confirmed'][df.index[-195]],
            "deaths": df['deaths'][df.index[-195]],
            "recovered": df['recovered'][df.index[-195]]
        }
