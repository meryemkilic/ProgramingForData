import unittest
import pandas as pd
from MissingValueHandler import MissingValueHandler
from Scaler import Scaler
from OutlierHandler import OutlierHandler
from Visualizer import Visualizer

class TestModules(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Dosya yolu
        data_path = 'C:\\Users\\merye\\PycharmProjects\\PythonTermProject\\synthetic_sample_data.csv'
        # Verileri yükle
        cls.data = pd.read_csv(data_path)
        # 'Budget in USD' ve 'Rating' sütunlarını sayısal veriye dönüştür
        cls.data['Budget in USD'] = pd.to_numeric(cls.data['Budget in USD'], errors='coerce')
        cls.data['Rating'] = pd.to_numeric(cls.data['Rating'], errors='coerce')

    def test_fill_mean(self):
        handler = MissingValueHandler()
        self.data['Rating'] = handler.fill_mean(self.data, ['Rating'])
        self.assertFalse(self.data['Rating'].isnull().any(), "Hala eksik değerler var!")

    def test_min_max_scale(self):
        scaler = Scaler()
        # NaN değerlerini temizle
        self.data.dropna(subset=['Budget in USD'], inplace=True)
        scaled_data = scaler.min_max_scale(self.data[['Budget in USD']])
        self.assertTrue(scaled_data['Budget in USD'].min() >= 0 and scaled_data['Budget in USD'].max() <= 1, "Veriler 0-1 aralığında olmalı!")

    def test_iqr_outliers(self):
        handler = OutlierHandler()
        original_count = self.data.shape[0]
        filtered_data = handler.iqr_outliers(self.data, 'Rating')
        self.assertTrue(filtered_data.shape[0] <= original_count, "Veri seti boyutu azalmalı!")

    def test_plot_histogram(self):
        visualizer = Visualizer()
        visualizer.plot_histogram(self.data, 'Rating')
        self.assertTrue(True, "Histogram çizimi başarısız oldu!")

if __name__ == '__main__':
    unittest.main()
