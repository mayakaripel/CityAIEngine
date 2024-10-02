import matplotlib.pyplot as plt

def plot_population(data):
    plt.figure(figsize=(10, 6))
    plt.bar(data['city'], data['population'])
    plt.xlabel('City')
    plt.ylabel('Population')
    plt.title('City Population Overview')
    plt.show()

# Example usage
if __name__ == "__main__":
    data = {'city': ['CityA', 'CityB'], 'population': [500000, 800000]}
    plot_population(pd.DataFrame(data))
