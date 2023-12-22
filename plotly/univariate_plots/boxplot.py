# boxplot 

import pandas as pd 
import plotly as px 

data = pd.read_csv("file.txt")
fig = px.box(
    data_frame = data,
    # hover_data = [] list of column names to display over hover
    #                 useful to find outliers
    # points = specify how to show outliers
    y='Y axis label',
    color='city',
    color_discrete_map={
        'London': 'rgb(0,0,128)',
        'Melbourne': 'rgb(235, 207, 0)'}
    )

fig.show()