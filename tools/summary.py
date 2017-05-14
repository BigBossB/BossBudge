import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tools import chargelib

def monthly(month):
    df = pd.read_csv(month.write_path, index_col=0)

    categories = list(chargelib.charges.keys())    
    amounts = dict()
    
    for c in categories:
        amounts[c] = np.round(np.sum(df[df['Category'] == c]['Amount']), decimals=2)

    return amounts
    
#def annual:(df)    
    


