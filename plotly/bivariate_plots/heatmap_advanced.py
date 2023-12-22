import pandas as pd 
import plotly.graph_objects as go 

df = pd.read_csv("file.txt")

# pandas creates a correlation matrix
cr = df.corr(method="pearson")

fig = go.Figure(go.Heatmap(
    x=cr.columns,
    y=cr.columns,
    z=cr.values.tolist(),
    colorscale='rdylgn',
    zmin=-1, # minimum value allowed
    zmax=1   # maximum value allowed
))