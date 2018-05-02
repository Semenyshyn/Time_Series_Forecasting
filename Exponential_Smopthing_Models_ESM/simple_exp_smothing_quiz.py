import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('single-family-home-sales.xlsx',
                   header=0)
df['Month'] = pd.to_datetime(df['Month'])

# time-series visualization
sns.pointplot(y='Home Sales', x='Month', data=df)
plt.show()


def exponential_smoothing(series, alpha_value):
    output = sum([alpha_value * (1 - alpha_value) ** i * x for i, x in
                  enumerate(reversed(series[:-1]))])
    return output


# calculation forecast
for alpha in [0.8, 0.6, 0.2]:
    print('forecast for December 1995 with alpha {} is {}'.
          format(alpha, exponential_smoothing(df['Home Sales'], alpha)))
