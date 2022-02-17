from covid19dh import covid19
import pandas as pd
import random


class Covid19:
    country = ['USA', 'ITALY', 'RUSSIA', 'KAZAKHSTAN', 'UZBEKISTAN', "JAPAN", 'GB', 'GERMANY', 'MONGOLIA','SPAIN']

    def __init__(self):
        self.choice = random.choice(self.country)
        xx, src = covid19(self.choice, verbose=False)
        df = pd.DataFrame(xx)
        df.fillna(0.0, inplace=True)
        self.data = {
            "country": self.choice,
            "confirmed": df['confirmed'][df.index[-1]],
            "deaths": df['deaths'][df.index[-1]],
            "recovered": df['recovered'][df.index[-1]]
        }