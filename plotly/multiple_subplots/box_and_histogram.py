import pandas as pd 
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv("x.csv")
fig = make_subplots(rows=2, cols=1,
        subplot_titles = [
            "Histogram subplot1 title",
            "Boxplot subplot title"
        ])
fig.add_trace(
    go.Histogram(x=df["col"], nbinsx=5),
    row=1,
    col=1 
)
fig.add_trace(
    go.Box(x=df["col"],
           hovertext=df["col2"]),
    row=1,
    col=1
)

fig.update_layout({
    'title': {
        'text': 'Main title',
        'x': 0.5, 'y': 0.9
    }
})

fig.show()