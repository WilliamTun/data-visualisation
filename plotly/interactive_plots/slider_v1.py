fig = px.scatter(
    data_frame=df,
    y="col 1",
    x="col 2",
    color='col 3',
    animation_frame='col 4', # what value is on slide
    animation_group='col 5'  # what we are changing across time
)

fig.update_layout({
    'yaxis': {'range': [0, 1000]},
    'xaxis': {'range': [-100, 100]}
})

# remove unnecessary part of animation
fig['layout'].pop('updatemenus')

fig.show()