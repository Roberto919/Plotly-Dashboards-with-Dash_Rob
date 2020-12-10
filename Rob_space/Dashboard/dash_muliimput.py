## EXERCISE TO CREATE DASHBOARD WITH MULTIPLE INPUTS FOR A GRAPH





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
df = pd.read_csv("../../Data/mpg.csv")





###############
## Dashboard ##
###############

app = dash.Dash()

## ["mpg", "hp", "displace"...]
features = df.columns



## Dashboard layout
app.layout = html.Div(
    [
        html.Div(
            [
                dcc.Dropdown(
                    id="xaxis",
                    options=[{"label": i, "value": i} for i in features],
                    value="displacement"
                )
            ],
            style={
                "width": "48%",
                "display": "inline-block"
            }
        ),
        html.Div(
            [
                dcc.Dropdown(
                    id="yaxis",
                    options=[{"label": i, "value": i} for i in features],
                    value="mpg"
                )
            ],
            style={
                "width": "48%",
                "display": "inline-block"
            }
        ),
        dcc.Graph(id="feature-graphic")
    ],
    style={
        "padding": 10,
    }
)



## Adjusting figures
@app.callback(
    Output("feature-graphic", "figure"),
    [
        Input("xaxis", "value"),
        Input("yaxis", "value")
    ]
)
def update_graph(xaxis_name, yaxis_name):

    trace = [
        go.Scatter(
            x=df[xaxis_name],
            y=df[yaxis_name],
            text=df["name"],
            mode="markers",
            marker={
                "size": 15,
                "opacity": 0.5,
                "line": {
                    "width": 0.5,
                    "color": "white"
                }
            }
        )
    ]

    layout = go.Layout(
        title="My Dashboard for MPG",
        xaxis={
            "title": xaxis_name,
        },
        yaxis={
            "title": yaxis_name
        },
        hovermode="closest"
    )

    return_dict = {
        "data": trace,
        "layout": layout
    }

    return return_dict





#############################
## Main execution function ##
#############################

if __name__ == "__main__":
    app.run_server()
