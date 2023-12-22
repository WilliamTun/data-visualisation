import plotly.express as px 

data = pd.read_csv("file.txt")

'''
# optional arguments:
1. trendline
2. symbol: dif symbols for dif categories
3.

'''

fig = px.scatter(
    data_frame=data,
    x="col1",
    y="col2",
    # trendline
    # symbol 
    hover_data=['col3'] # show data on hover
)

fig.update_layout({
    'showlegend': 'True',
    'legend': {
        'title': 'my company',
        'x': 0.5, 
        'y': 0.8,
        'bgcolor': 'rgb(246, 228, 129)'
    }
})

fig.show()