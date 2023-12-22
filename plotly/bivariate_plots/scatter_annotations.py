
# Annotations = extra boxes of text and info
# unlike hover information, annotations are always present

# Two purposes:
# 1. data linked annotations
#    draw attention to a specific data point
# 2. adding notes to a plot. 
#    via  a text box


# Key arguments in annotation parameter
# 1. showarrow = True/False
#     draw arraw from a box to a given x & y co-ordinate
# 2. text = textbox to display
# 3. x and y = 
#    co-ordinates to procue annotation

import plotly.express as px 
import pandas as pd 

data = pd.read_csv("file.txt")

fig = px.scatter(
    data_frame=data,
    x="col1",
    y="col2",
    # trendline
    # symbol 
    hover_data=['col3'] # show data on hover
)

my_annotation = {
    'x': 215111, 'y': 449000,
    'showarrow': True, 
    'arrowhead': 3, 
    'text': "This is an annotation",
    'font': {
        'size': 10,
        'color': 'red'
    }
}

'''
# Float annotation


my_annotation = {
    'xref': 'paper', 'yref': 'paper',
    'x': 0.5, 'y': 0.8,
    'showarrow': False, 
    'text': "This is an annotation",
    'font': {
        'size': 10,
        'color': 'red'
    },
    'bgcolor': 'rgb(255,0,0)'
}
'''


fig.update_layout({
    'annotations': {my_annotation}
})

# X & Y labels
fig.update_xaxes(title_text='my X label')
fig.update_yaxes(title_text='my Y label')
fig.update_layout({
    'xaxis': {'title': {'text' : 'New x label'}},
    'yaxis': {'title': {'text' : 'New y label'}}
})


fig.show()