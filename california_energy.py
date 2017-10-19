"""
Analyze historical hourly load data for California to understand trends and
identify periods where battery storage could have a positive impact.

Data sources:
- CAISO: http://www.caiso.com/planning/Pages/ReliabilityRequirements/Default.aspx
"""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load data
# - PGE = NorCal
# - SCE = SoCal
# - SDGE = SD
# - VEA (Valley Electric Association) = out-of-state utility (NV)
df = pd.read_csv('caiso_historical.csv', sep=',',
                 parse_dates=True, index_col=0)

# plot time-series
#df[['PGE', 'SCE', 'SDGE', 'CAISO']].plot()
#df.plot()
#plt.ylabel('Hourly Load [MW]')
#plt.show()

## histograms
##df[['PGE', 'SCE', 'SDGE']].hist(layout=(1, 3))
#df[['PGE', 'SCE', 'SDGE']].hist()
#plt.xlabel('Hourly Load [MW]')
#plt.show()

## summary stats
#print df.describe()

## CAISO: distribution by hour of the day
#hours = range(24)
#hourly_mean = df['CAISO'].groupby(df.index.hour).mean()
#hourly_std = df['CAISO'].groupby(df.index.hour).std()
#
#plt.errorbar(hours, hourly_mean, yerr=hourly_std)
#plt.ylabel('Hourly Load [MW]')
#plt.show()

# seaborn plots
sns.violinplot(data=df, x=df.index.hour, y='CAISO', inner='quartile')
plt.xlabel('Hour of the day')
plt.ylabel('Load [MW]')
plt.show()
