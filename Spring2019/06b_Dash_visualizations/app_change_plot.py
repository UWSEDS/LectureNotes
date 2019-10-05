"""
Select which plot type to do, bar or scatter.
To run: python app_live_update.py

This also demonstrates how to change a figure.
"""

import numpy as np
import pandas as pd
import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
from dash.dependencies import Input, Output

SIZE = 10
COL_X = 'x'
COL_Y1 = 'y1'
COL_Y2 = 'y2'
DF = pd.DataFrame({
    COL_X: range(SIZE),
    COL_Y1: np.random.randint(0, 10, SIZE),
    COL_Y2: np.random.randint(0, 10, SIZE),
})
OPT_BAR = "bar"
OPT_LINE = "scatter"
OPTIONS = [
    {'label': 'Bar plot', 'value': OPT_BAR},
    {'label': 'Line plot', 'value': OPT_LINE},
]


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(
    html.Div([
        html.H4('Plot Type Selection'),
        dcc.Graph(id='graph'),
        html.Label('Plot selector'),
        dcc.RadioItems(id='radio', 
            options=[
                {'label': 'Bar plot', 'value': OPT_BAR},
                {'label': 'Line plot', 'value': OPT_LINE},
            ],
            value=OPT_BAR),
    ])
)


# Select the aplot
@app.callback(Output('graph', 'figure'), [Input('radio', 'value')])
def update_graph(selected_plot_type):
    # Create the graph with subplots
    fig = plotly.tools.make_subplots(rows=2, cols=1, vertical_spacing=0.2)
    fig['layout']['margin'] = {
        'l': 30, 'r': 10, 'b': 30, 't': 10
    }
    fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}

    fig.append_trace({
        'x': DF[COL_X],
        'y': DF[COL_Y1],
        'name': 'Plot1',
        'type': selected_plot_type,
    }, 1, 1)
    fig.append_trace({
        'x': DF[COL_X],
        'y': DF[COL_Y2],
        'name': 'Plot2',
        'type': selected_plot_type,
    }, 2, 1)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)

