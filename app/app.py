import pandas as pd
import seaborn as sns
import plotly.express as px
import dash
from dash.dependencies import Input, Output, State
from dash import dcc, html, dash_table
from waitress import serve

app = dash.Dash()
server = app.server

df = sns.load_dataset('iris')
fig1=px.bar(df,x=df['species'],y=df['petal_width'])
df1 = px.data.iris()
fig2 = px.scatter_matrix(df1)

app.layout = html.Div(children=[
  html.H2(children='Sample Data Analysis with iris dataset',style={'textAlign': 'center'}),
    dcc.Graph(
       id='irssp',
       figure=fig2
    ), dcc.Graph(

       figure=fig1
    ),
                      ])


if __name__ == '__main__':
    app.run()
    #app.run_server(host='0.0.0.0',port=9090)
    # serve(app.server, host='0.0.0.0',port=9090)
