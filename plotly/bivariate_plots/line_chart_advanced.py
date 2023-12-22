import plotly.graph_objects as go
import pandas as pd

data = pd.read_csv("file.txt")

fig = go.Figure(
    go.Scatter(
    x=data["col1"],
    y=data["col2"],
    mode="lines"))

fig.show()