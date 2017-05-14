import os
from tools import statements , summary



month_dir = '/home/tyto/Documents/Finances/statements/2017/February/'
write_path = '/home/tyto/Documents/Finances/statements/2017/summary/january_summary.csv'
write = False



month = statements.month(month_dir, write_path, write = False)
month.read()
month.parse()
month.export()
print(month.out)


amounts = summary.monthly(month)