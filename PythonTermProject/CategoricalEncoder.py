import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

class CategoricalEncoder:
    def __init__(self):
        self.one_hot_encoder = OneHotEncoder(sparse=False)
        self.label_encoder = LabelEncoder()

    def one_hot_encode(self, data, column):
        encoded = self.one_hot_encoder.fit_transform(data[[column]])
        encoded_df = pd.DataFrame(encoded, columns=self.one_hot_encoder.get_feature_names_out([column]),index=data.index)

        data.drop(column, axis=1, inplace=True)

        return pd.concat([data, encoded_df], axis=1)

    def label_encode(self, data, column):
        data[column] = self.label_encoder.fit_transform(data[column])
        return data


