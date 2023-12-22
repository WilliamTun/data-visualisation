# Plotly

Python library that wraps around javascript
to produce plots. 

3 main ways to plot:
1. plotly.express            # simple plots
2. plotly.graph_object       # customizable plots
3. plotly.figure_library     # advanced plots

Key resource:
https://plotly.com/python/


Plotly figures has 3 main elements:
1. layout
a dictionary controlling style of the figure
one layout per figure
2. data
takes in list of dictionaries defining graph types
trace: data + type
one graph can have multiple traces
3. frames
for animated plots

Example:
'''
print(fig)

>> Figure({
    'data': [{'type': 'bar'
        'x': [Mon, Tue, Wed]
        'y': [10, 12, 15]}],
    'layout': {
        'template': '...'
        'title': {'font': {
            'color': 'red',
            'size': 15
        }},
        'text': 'my chart is good'}
    })
'''