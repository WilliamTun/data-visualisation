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
fig.show()