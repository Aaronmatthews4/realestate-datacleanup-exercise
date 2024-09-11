import pandas as pd

df = pd.read_csv('assets/real_estate.csv', sep=';')

south_belt_populations = ["Fuenlabrada", "Leganés", "Getafe", "Alcorcón"]


south_belt_df = df[df['level5'].isin(south_belt_populations)]

south_belt_df['normalized_price'] = south_belt_df.groupby('level5')['price'].transform(
    lambda x: (x - x.min()) / (x.max() - x.min())
)
south_belt_df[['level5', 'price', 'normalized_price']].head()

# Plot the histograms for each population in the same plot
south_belt_df.groupby('level5')['normalized_price'].plot(kind='hist', alpha=0.5, legend=True, bins=20)

plt.xlabel('Normalized Price')
plt.ylabel('Frequency')
plt.title('Histograms of Normalized Prices for South Belt Populations')
plt.show()











