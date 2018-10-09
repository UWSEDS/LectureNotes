"""Using callbacks to interact with widgets."""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='my-id1', value='initial value1', type='text'),
    dcc.Input(id='my-id2', value='initial value2', type='text'),
    html.Div(id='my-div'),
])


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id1', component_property='value'),
     Input(component_id='my-id2', component_property='value')]
)
def update_output_div(input_value1, input_value2):
    print(input_value1, input_value2)
    return 'You\'ve entered "{}"'.format(input_value1 + input_value2)


if __name__ == '__main__':
    app.run_server()
