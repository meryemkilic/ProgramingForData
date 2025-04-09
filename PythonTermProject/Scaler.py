import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

class Scaler:
    def __init__(self):
        self.min_max_scaler = MinMaxScaler()
        self.standard_scaler = StandardScaler()

    def min_max_scale(self, data):
        return pd.DataFrame(self.min_max_scaler.fit_transform(data), columns=data.columns, index=data.index)

    def standard_scale(self, data):
        return pd.DataFrame(self.standard_scaler.fit_transform(data), columns=data.columns, index=data.index)
