import pandas as pd

class CityEngine:
    def __init__(self, data):
        self.data = data
    
    def analyze(self):
        # Sample analysis logic
        return self.data.describe()

# Example usage
if __name__ == "__main__":
    data = pd.DataFrame({"population": [500000, 200000, 800000]})
    engine = CityEngine(data)
    print(engine.analyze())
