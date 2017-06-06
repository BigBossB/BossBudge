from bokeh.plotting import *
import matplotlib.pyplot as plt
from numpy import pi
import pandas as pd

from bokeh.charts import Donut, show, output_file
from bokeh.sampledata.olympics2014 import data



df = pd.DataFrame({'Type' :  Type,
'Amounts' : Amounts})

d = Donut(df, label='Type' , values = 'Amounts', 
          hover_text = 'Amounts',
          plot_width=800, plot_height=800, 
          legend = 'top_right')
show(d)


