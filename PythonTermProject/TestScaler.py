import pandas as pd
from Scaler import Scaler

class TestScaler:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
        self.scaler = Scaler()

        # Only select numeric columns for scaling
        self.numeric_columns = self.data.select_dtypes(include=['float64', 'int64']).columns
        self.data_numeric = self.data[self.numeric_columns]

    def run_tests(self):
        print("Original numeric data:")
        print(self.data_numeric)

        print("\nMin-Max scaled data:")
        data_min_max_scaled = self.scaler.min_max_scale(self.data_numeric.copy())
        print(data_min_max_scaled)

        print("\nStandard scaled data:")
        data_standard_scaled = self.scaler.standard_scale(self.data_numeric.copy())
        print(data_standard_scaled)


if __name__ == "__main__":
    data_path = 'C:\\Users\\merye\\PycharmProjects\\PythonTermProject\\data.csv'
    test_scaler = TestScaler(data_path)
    test_scaler.run_tests()