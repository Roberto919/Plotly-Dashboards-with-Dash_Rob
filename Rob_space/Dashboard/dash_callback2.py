##





#############
## Imports ##
#############

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go

import pandas as pd





##########
## Data ##
##########
df = pd.read_csv("../../Data/gapminderDataFiveYear.csv")
print(df.head)





###############
## Dashboard ##
###############

app = dash.Dash()

app.layout = html.Div(
    [
        dcc.Graph()
    ]
)





#############################
## Main execution function ##
#############################

if __name__ == "__main__":
    app.run_server()
