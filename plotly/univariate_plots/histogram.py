# plot distribution of a single variable

# Histogram
import pandas as pd 
import plotly as px 

data = pd.read_csv("file.txt")
fig = px.histogram(
    data_frame = data,
    # orientation = vertical / horizontal plot
    # histfunc = set bin aggregation method - average / min / max
    x='X axis label',
    nbins=10)