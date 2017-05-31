import os
from tools import statements , summary


# Setup directories
month_dir = '/home/tyto/Documents/Finances/statements/2017/January/'
write_path = '/home/tyto/Documents/Finances/statements/2017/summary/april_summary.csv'
write = False


# Proess all statements in the directory
month = statements.month(month_dir, write_path, write = write)
month.read()
month.parse()
month.export()
print(month.out[month.out.Category == 'X'])


# Read the sumary reports (generated .csv files)
amounts = summary.monthly(month)




amounts.plot()