
import pandas as pd 
import plotly.graph_objects as go
from plotly.subplots import make_subplots


df = pd.read_csv("file.txt")

fig = make_subplots(rows=3, cols=1, shared_xaxes=True)

row_num = 1 

for category in ["X", "Y", "Z"]:
    data = df[df["category"] == category]
    fig.add_trace(
        go.Scatter(
            x = data["X values"],
            y = data["Y values"],
            name = category, 
            mode = "markers" 
        ),
        row=row_num, col=1
    )
    row_num += 1


dropdown_buttons = [
    {
     "label": 'X', 
     'method': 'update',
     "args": [ {"visible": [True, False, False]},
               {"title": "X title"}]
    },

    {
     "label": 'Y', 
     'method': 'update',
     "args": [ {"visible": [False, True, False]},
               {"title": "Y title"}]
    }, 

    {
     "label": 'Z', 
     'method': 'update',
     "args": [ {"visible": [False, False, True]},
               {"title": "Z title"}]
    } 
]

fig.update_layout({
    'updatemenus': [
        {
            "type": "dropdown",
            "x":1.3, "y": 0.5,
            "showactive": True, 
            "active": 0,
            "buttons": dropdown_buttons
        }
    ]
})

fig.show()