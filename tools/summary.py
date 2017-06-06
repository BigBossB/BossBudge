import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tools import chargelib

class monthly:
    
    def __init__(self, month):
        df = pd.read_csv(month.write_path, index_col=0)

        categories = list(chargelib.charges.keys())    
        amounts = dict()
    
        for c in categories:
            amounts[c] = np.round(np.sum(df[df['Category'] == c]['Amount']), decimals=2)

        self.amounts = amounts
    
    def plot(self):
        Type = list(self.amounts.keys())
        Amounts = list(self.amounts.values())
        
        df = pd.DataFrame({'types' : Type , 'amounts' : Amounts})
        gtz = df['amounts'] > 0
        df = df[gtz]
        df = df.sort_values('amounts', ascending=False)
        
        Type = list(df['types'].get_values())
        Amounts = list(df['amounts'].get_values())
        
        for k in [-1 , -2, -3]:
            first = Amounts[-1*k]
            second = Amounts[k]
            Amounts[-1*k] = second
            Amounts[k] = first
        
        for k in [-1 , -2, -3]:
            first = Type[-1*k]
            second = Type[k]
            Type[-1*k] = second
            Type[k] = first
            
        
        def make_autopct(values):
            def my_autopct(pct):
                total = sum(values)
                val = pct*total/100.0
                return '${v:.2f} ({p:.2f}%)  '.format(p=pct,v=val)
            return my_autopct

        fig1, ax1 = plt.subplots(figsize=(12, 12))
        ax1.pie(Amounts, labels=Type, autopct = make_autopct(Amounts),
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        
        plt.show()
        
        
#def annual(summary):(df)    
# another class instantiation    



        
