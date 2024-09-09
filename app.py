import pandas as pd

df = pd.read_csv('assets/real_estate.csv', sep=';')

south_belt_populations = ["Fuenlabrada", "Leganés", "Getafe", "Alcorcón"]

south_belt_df = df[df['level5'].isin(south_belt_populations)]

south_belt_df['pps'] = south_belt_df['price'] / south_belt_df['surface']

getafe_alcorcon_df = south_belt_df[south_belt_df['level5'].isin(['Getafe', 'Alcorcón'])]

statistics = getafe_alcorcon_df.groupby('level5')['pps'].describe()

print(statistics)










