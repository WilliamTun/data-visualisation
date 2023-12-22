import plotly.express as px 

data = pd.read_csv("file.txt")

fig = px.line(
    data_frame=data,
    x="col1",
    y="col2",
    title="Stock price"
    # trendline
    # symbol 
)

fig.show()