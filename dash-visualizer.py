from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv('processed-data.csv')
fig = px.line(df, x="date", y="sales")
fig.update_layout(xaxis_title = 'transaction-date', yaxis_title= 'pink morsels\' sales')


app.layout = html.Div(children=[
    dcc.Graph(
        id='line-graph',
        figure=fig,
        style={'height':'90vh'}
    )
])
app.run()


