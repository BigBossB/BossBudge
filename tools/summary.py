import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
from tools import chargelib

class monthly:
    
    def __init__(self, month):
        df = pd.read_csv(month.write_path, index_col=0)

        df = df[ df['Category'] != 'payment']

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
        
        # Switch first and second 
        _famt = Amounts[0]; _samt = Amounts[1]
        _ftype = Type[0]; _stype = Type[1]
        Amounts[0] = _samt; Amounts[1] = _famt
        Type[0] = _stype; Type[1] = _ftype
        
        for k in [-1 , -2, -3]:
            top = Amounts[-1*k]
            bottom = Amounts[k]
            Amounts[-1*k] = bottom
            Amounts[k] = top
        
        for k in [-1 , -2, -3]:
            top = Type[-1*k]
            bottom = Type[k]
            Type[-1*k] = bottom
            Type[k] = top
            
        
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
        
        
class annual:
     
    def __init__(self, summary_dir):
        self.summary_dir = summary_dir
        self.summary = dict()
        files = os.listdir(summary_dir)
        self.months = ['january' , 'february' , 'march' , 'april', 'may' , 'june', 'july']
        self.Amounts = []
        for m in self.months:
            for f in files:            
                if m in f:
                    name = summary_dir + f
                    df = pd.read_csv(name, index_col=0)
                        
                    categories = list(chargelib.charges.keys())    
                    amounts = dict()
                    
                    df = df[ df['Category'] != 'payment']
                    
                    
                    
                    for c in categories:
                        if c != 'payment':
                            amounts[c] = np.round(np.sum(df[df['Category'] == c]['Amount']), decimals=2)
                    self.Type = list(amounts.keys())
                    self.Amounts.append(list(amounts.values()))
            
#                    self.summary[m] = {'Category' : Type, 'Amounts' : Amounts}

    def plot(self):
        money_matrix = np.array(self.Amounts)
        plt.figure(figsize=(15,10))
        for count , p in enumerate(money_matrix.T):
            
            plt.plot(p, hold=True, linewidth=2, label = self.Type[count])
        plt.xticks(range(len(self.months)), self.months)
        plt.legend()        
            
            
        
