import unittest
from src.core.engine import CityEngine
import pandas as pd

class TestCityEngine(unittest.TestCase):
    def test_analyze(self):
        data = pd.DataFrame({"population": [500000, 200000, 800000]})
        engine = CityEngine(data)
        analysis = engine.analyze()
        self.assertEqual(analysis['population']['mean'], 500000)

if __name__ == '__main__':
    unittest.main()
