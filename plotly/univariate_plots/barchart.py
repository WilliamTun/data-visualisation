# Histogram
import pandas as pd 
import plotly as px 

data = pd.read_csv("file.txt")
fig = px.bar(
    data_frame = data,
    x='col1',
    y='col2',
    log_y=True, # convert y values to log(y) scale
    title='my barchart',
    color='col3')

# The color argument is a great way to segment
# our plot further in accordance to the categories
# in col3

# after the figure is made
# we can continue to update the layout:
fig.update_layout({ 
        'title': { 'text': 'A new title'}
        })

fig.show()
