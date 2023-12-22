
sliders = [
    {
        'steps': [
            {
             'method': 'update',
             'label': 'X'
             'args': [{'visible': [True, False, False]}]
             },
             {
             'method': 'update',
             'label': 'Y'
             'args': [{'visible': [False, True, False]}]
             },
             {
             'method': 'update',
             'label': 'Z'
             'args': [{'visible': [False, False, True]}]
             }
        ]
    }
]


# make traces invivisble
fig.data[1].visible=False 
fig.data[2].visible=False 
fig.update_layout({'sliders': sliders})

fig.show()