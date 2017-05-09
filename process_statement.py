from tools import statements

month_dir = '/home/tyto/Documents/Finances/statements/2017/January/'

month = statements.month(month_dir)
month.read()
month.parse()

print(month.out)