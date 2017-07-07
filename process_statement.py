import os
from tools import statements , summary


# Setup directories
month_dir = '/home/tyto/Documents/Finances/statements/2017/March/'
write_path = '/home/tyto/Documents/Finances/statements/2017/summary/march_summary.csv'
write = False


# Proess all statements in the directory
month = statements.month(month_dir, write_path, write = write)
month.read()
month.parse()
month.export()
print(month.out[month.out.Category == 'X'])
print('Charges Read: %i. Charges Sorted: %i' % (month.df['Amount'].count() , month.out['Amount'].count()))
month.out[month.out['Category'] == 'sports']

# Read the sumary reports (generated .csv files)
monthsum = summary.monthly(month)

#month.plot()

# Print out individual categories for inspection
yearsum = summary.annual('/home/tyto/Documents/Finances/statements/2017/summary/')
yearsum.plot()