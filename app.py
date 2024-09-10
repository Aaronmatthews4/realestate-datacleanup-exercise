import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler


df = pd.read_csv('assets/real_estate.csv', sep=';')


south_belt_populations = ["Fuenlabrada", "Leganés", "Getafe", "Alcorcón"]


south_belt_df = df[df['level5'].isin(south_belt_populations)]


scaler = MinMaxScaler()

normalized_prices = {}
for population in south_belt_populations:
    subset = south_belt_df[south_belt_df['level5'] == population]
    prices = subset[['price']].values
    normalized_prices[population] = scaler.fit_transform(prices).flatten()

plt.figure(figsize=(12, 8))
for population, prices in normalized_prices.items():
    plt.hist(prices, bins=30, alpha=0.5, label=population)

plt.title('Histograms of Normalized Prices for South Belt of Madrid')
plt.xlabel('Normalized Price')
plt.ylabel('Frequency')
plt.legend(loc='upper right')
plt.grid(True)
plt.tight_layout()
plt.show()











