import flask
import dash
import dash_core_components as dcc
import dash_html_components as html

server = flask.Flask(__name__)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

@server.route('/')
def index():
    return '''
            <html>
            <head>
            </head>
            <body>
              <h1 align="center">My app is here</h1>
              <p align="center"><iframe src="/dash/" width=700 height=600 /></p>
            </body>
            </html>
        '''

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    server = server,
    routes_pathname_prefix = '/dash/'
)

app.layout = html.Div(children=[
        html.H1(children='Hello Dash'),

        html.Div(children='''
            Dash: A web application framework for Python.
        '''),

        dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                ],
                'layout': {
                    'title': 'Dash Data Visualization'
                }
            }
        )
])

if __name__ == '__main__':
    app.run_server(debug=True)
