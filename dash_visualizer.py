from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd


#intializing Dash app
app = Dash(__name__)

#load in data
df = pd.read_csv('processed_data.csv')

#create visualization
app.layout = html.Div(id='wrapper', children=[

    html.Div(id='header',children='''
        Pink Morsel Sales - Line Graph
    '''),

    html.Div(id='radio-wrapper', children=[
         
        dcc.RadioItems(
            id='radio-buttons',
            options=['East', 'West', 'North', 'South', 'All'],
            value='All',
            labelStyle={'display': 'inline-block'}
        )
    ]),
    dcc.Graph(id='line-graph')
])

#updates graphs based on the selection

@callback(
    Output(component_id='line-graph', component_property='figure'),
    Input(component_id='radio-buttons', component_property='value')
)

def update_graph(input_value):
    figure = px.line(df, x="date", y="sales")
    
    #checks the region and filters dataframe accordingly
    if input_value.lower() != 'all':
        filtered_df = df[df['region'] == input_value.lower()]
        figure = px.line(filtered_df, x="date", y="sales")

    figure.update_layout(xaxis_title=f'transaction-date ({input_value})', yaxis_title='total sales')
    return figure

if __name__ == '__main__':
    app.run_server()


