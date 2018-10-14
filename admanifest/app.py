import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Hello world."),
    dcc.Graph(
        id='example-graph-2',
        figure={
            'data': [
                {
                    'x': [1, 2, 3],
                    'y': [4, 1, 2],
                    'type': 'scatter',
                    'name': 'SF',
                },
                {
                    'x': [1, 2, 3],
                    'y': [2, 4, 5],
                    'type': 'scatter',
                    'name': 'Montréal',
                },
            ],
        }
    )
])


if __name__ == "__main__":
    app.run_server(debug=True)
