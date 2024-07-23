import plotly.graph_objects as go
import numpy as np

def sel_plot(wl, spectra_arr, class_names, yMax = 0.75):
    # Inputs:
    #   wl: numpy array of wavelengths
    #   spectra_arr: numpy array where each row is a spectrum, shape = num_spec x num_bands
    #   class_names: a list of class names, same length as the number of spectra
    
    fig = go.Figure()

    # Add traces for each class
    for class_name in np.unique(np.asarray(class_names)):
        spec = spectra_arr[np.where(class_names == class_name)[0], :]
        m = np.mean(spec, axis=0)
        fig.add_trace(go.Scatter(
            x=wl, y=m,
            mode='lines',
            name=class_name,
            line=dict(width=2)
        ))

    # Create update menus (buttons)
    updatemenus = [
        {
            'buttons': [
                {
                    'label': 'Show All',
                    'method': 'update',
                    'args': [{'visible': [True] * len(fig.data)},
                            {'title': 'Showing All Traces'}]
                },
                {
                    'label': 'Hide All',
                    'method': 'update',
                    'args': [{'visible': ['legendonly'] * len(fig.data)},
                            {'title': 'Hiding All Traces'}]
                }
            ],
            'direction': 'left',
            'pad': {'r': 10, 't': 10},
            'showactive': True,
            'x': 0.1,
            'xanchor': 'left',
            'y': 1.1,
            'yanchor': 'top'
        }
    ]

    # Update the layout
    fig.update_layout(
        title='Class Means',
        xaxis=dict(title='Wavelength (nm)'),
        yaxis=dict(title='Reflectance', range=[0, yMax]),
        legend_title_text='Class',
        legend=dict(
            itemclick="toggle",
            itemdoubleclick="toggleothers"
        ),
        updatemenus=updatemenus,  # Add the buttons to the layout
        height=700,  # Change the height of the plot
        plot_bgcolor='white',  # Change the background color of the plot area to white
        paper_bgcolor='white'  # Change the background color of the entire figure to white
    )

    # Add grid lines
    fig.update_xaxes(showgrid=True, gridwidth=0.5, gridcolor='LightGray', minor=dict(showgrid=True, gridwidth=0.25))
    fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='LightGray', minor=dict(showgrid=True, gridwidth=0.25))

    # Show the figure
    fig.show()