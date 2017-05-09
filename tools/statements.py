from tools import chargelib
import pandas as pd
import os

class month:
    
    def __init__(self, month_dir, overwrite=False):
        
        self.month_dir = month_dir
        self.overwrite = overwrite
        
        self.statements = os.listdir(month_dir)
        self.charge_lib = chargelib.charges
        self.amounts = chargelib.amount
        
    def read(self):
        for count , s in enumerate(self.statements):
            if 'CitiBank' in s:
                df_temp = pd.read_csv(self.month_dir + s)
            elif 'Chase' in s:
                df_temp = pd.read_csv(self.month_dir + s)
                            
            
            if count == 0:
                self.df = df_temp
            else:                
                self.df = pd.concat( (self.df , df_temp) , axis=0)
                
    def parse(self):
        amt = []
        category = []
        desc = []
        
        for i in range(self.df.shape[0]):
            charge = self.df.iloc[i]
                        
            _amt = charge.Amount
            _desc = charge.Description.split(' ')
            
            amt.append(_amt)
            desc.append(_desc)                   
            category.append(self.get_charge_type(_desc, _amt))
            
            
        data = {'Category' : category, 'Description' : desc , 'Amount' : amt}
        out = pd.DataFrame(data)
        
        self.out = out[ out['Category'] != 'payment']
        
    def get_charge_type(self, desc, amt):
        unsorted = True
        for category in self.charge_lib.keys():            
                              
            for word in desc:
                word = str.lower(str(word))
                if word in self.charge_lib[category]:
                    self.amounts[category] += amt
                    return category
                    
        if unsorted == True:
            #print('UNSORTED:   %s' % desc)
            return 'X'
                
if __name__ == '__main__':
    month_dir = '/home/tyto/Documents/Finances/statements/2017/January/'

    month = month(month_dir, False)
    month.read()                
    month.parse()
    month.df.head()