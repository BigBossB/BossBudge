import bokeh.plotting as bk
from bokeh.models import HoverTool
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
        X = amounts.amounts.keys()
        Y = amounts.amounts.values()
        
#def annual(summary):(df)    
# another class instantiation    

    def plot(self):
        # define starts/ends for wedges from percentages of a circle
        percents = [0, 0.3, 0.4, 0.6, 0.9, 1]
        starts = [p*2*pi for p in percents[:-1]]
        ends = [p*2*pi for p in percents[1:]]
        
        # a color for each pie piece
        colors = ["red", "green", "blue", "orange", "yellow"]
        
        
        # Not Working
        p = bk.figure(x_range=(-1,1), y_range=(-1,1))
        
        # Not Working        
        p.circle('x', 'y', size=20, source=source)
        
        
        # Working
        source = bk.ColumnDataSource(
                data=dict(
                    x=amounts.amounts.keys(),
                    y=amounts.amounts.values(),            
                )
            )
        
        # Working
        hover = HoverTool(
                tooltips=[
                    ("Amount", "@x"),
                    ("Category", "@y")
                    
                ]
            )

        
        # Working?        
        p = bk.figure(plot_width=400, plot_height=400, tools=[hover],
                   title="Mouse over the dots")

        
        # Working                
        bk.show(p)

        
