#!/usr/bin/env python3
import datadotworld as dw
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
import numpy as np
import pandas as pd
register_matplotlib_converters()

# Import data
results = dw.query(
	'markmarkoh/coronavirus-data', 
    'SELECT * FROM full_data')
df = results.dataframe
countries = np.sort(df.location.unique())

# Graph info
plt.figure(figsize=(8,5))
plt.title('Total cases', fontdict={'fontsize':22})
plt.xlabel('Date', fontdict={'fontsize':15})
plt.ylabel('Cases', fontdict={'fontsize':15})

# Set range
youngest = max(df['date'])
oldest = min(df['date'])
scale = np.arange(oldest, youngest)

# User input
print("\nOptions:\n\n".upper(), np.array2string(countries, separator=', ').replace("'", ''))
while True:
    new_country = input("\nEnter country name or hit Enter to continue: ").capitalize()
    if not new_country:
        break
    elif new_country in countries:
        for country in countries:
            if country == new_country:
                new_df = df.loc[df['location'] == country]
                plt.plot(new_df.date, new_df.total_cases, marker='.', label=country)
    else:
        print("\nCountry doesn't exist. Try again.")
        continue

# Adjust and show graph
plt.xticks(scale[::15])
plt.legend()
plt.xlim(['2020-03-01', youngest])
plt.show()