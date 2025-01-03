from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd


#intializing Dash app
app = Dash()

#load in data
df = pd.read_csv('processed-data.csv')

#create visualization
app.layout = html.Div(id='wrapper', children=[
    dcc.RadioItems(
        id='radio-buttons',
        options=['East', 'West', 'North', 'South', 'All'],
        value = 'All',
    ),

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
    if input_value != 'All':
        filtered_df = df[df['region'] == input_value.lower()]
        figure = px.line(filtered_df, x="date", y="sales")

    figure.update_layout(xaxis_title='transaction-date', yaxis_title='sales of pink morsel')
    return figure


if __name__ == '__main__':
    app.run_server()


