import pandas as pd 
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# Possible lahyers plots:
# 1. Line + bar
# 2. Line + scatter
# 3. Line + Line
# 4. bar + bar

# make sure x and y axis has same units


df = pd.read_csv("x.csv")
fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=df["x"],
        y=df["y"],
        name="bar chart title"
    )
)

fig.add_trace(
    go.Scatter(
        x=df["x"],
        y=df["y"],
        name="scatter chart title",
        mode="lines+markers"
    )
)

fig.show()