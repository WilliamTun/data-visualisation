
my_buttons = [
    {'label': 'Bar plot',
     'method': 'update',
     'args': [{"type": "bar"}]},
    {'label': 'scatterplot',
     'method': 'update',
     'args': [{"type": "scatter",
               "mode": "markers"
               }]}
]


fig.update_layout({
    'updatemenus': [
        {
            "type": "buttons",
            "direction": "down",
            "x":1.3, "y": 0.5,
            "showactive": True, 
            "active": 0,
            "buttons": my_buttons
        }
    ]
})

fig.show()