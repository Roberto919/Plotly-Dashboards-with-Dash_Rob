##





"------------------------------------------------------------------------------"
#############
## Imports ##
#############


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import pandas as pd
import json
import base64
from numpy import random





"------------------------------------------------------------------------------"
##########
## Data ##
##########


## Reading data
df = pd.read_csv("../../Data/mpg.csv")

## Year with jitter
df["year"] = random.randint(-4, 5, len(df))*0.1 + df["model_year"]





"------------------------------------------------------------------------------"
#####################
## Base parameters ##
#####################


## Default car that will be shown in the line graph
default_car = "toyota corolla 1600 (sw)"
def_accel = list(df[df["name"] == default_car].loc[:, "acceleration"])[0]
def_disp = list(df[df["name"] == default_car].loc[:, "displacement"])[0]
def_disp_scl = def_disp/max(df["displacement"])*10





"------------------------------------------------------------------------------"
############
## Graphs ##
############


## Graph 1: Model year vs mpg scatter graph.

#### Creating figure
fig_g1 = go.Figure()


#### Data traces
fig_g1.add_trace(
    go.Scatter(
        x=df["year"] + 1900,
        y=df["mpg"],
        mode="markers",
        text=df["name"],
        hoverinfo=["text", "y", "x"]
    )
)


#### Figure layout
fig_g1.update_layout(
    title="MPG Data",
    xaxis_title="model year",
    yaxis_title="miles per gallon",
    hovermode="closest"
)





"------------------------------------------------------------------------------"
######################
## Dashboard layout ##
######################


app = dash.Dash()

app.layout = html.Div(
    [
        html.Div( ## Div for the scatter plot
            [
                dcc.Graph(
                    id="fig_g1",
                    figure=fig_g1
                ),
            ],
            style={
                "width": "70%",
                "display": "inline-block"
            }
        ),
        html.Div( ## Div for the line plot
            [
                dcc.Graph(
                    id="fig_g2",
                    figure={
                        "data": [
                            go.Scatter(
                                x=[0, def_accel],
                                y=[0, 60],
                                line={
                                    "color": "blue",
                                    "width": def_disp_scl
                                }
                            )
                        ],
                        "layout": go.Layout(
                            title=default_car,
                            xaxis={"visible": False},
                            yaxis={
                                "visible": False,
                                "range": [0, 8]
                            },
                            margin={"l": 0}
                        )
                    }
                ),
                html.Pre(
                    id="car_data"
                )
            ],
            style={
                "width": "30%",
                "display": "inline-block",
                "verticalAlign": "top"
            }
        )
    ]
)





"------------------------------------------------------------------------------"
#########################
## Dashboard callbacks ##
#########################


## Text callback
@app.callback(
    Output("car_data", "children"),
    [Input("fig_g1", "hoverData")]
)
def callback_text(car_selected_data):
    """
    """

    car_name = car_selected_data["points"][0]["text"]

    cyl = list(df[df["name"] == car_name].loc[:, "cylinders"])[0]
    disp = list(df[df["name"] == car_name].loc[:, "displacement"])[0]
    accel = list(df[df["name"] == car_name].loc[:, "acceleration"])[0]

    return_text = """
    {} cylinders
    {}cc displacement
    0 to 60 mph in {} seconds
    """.format(cyl, disp, accel)

    # return_text = json.dumps(car_selected_data, indent=2)

    return return_text



## Acceleration graph callback
@app.callback(
    Output("fig_g2", "figure"),
    [Input("fig_g1", "hoverData")]
)
def update_graph(car_selected_data):
    """
    """

    ## Car selected
    car_selected = car_selected_data["points"][0]["text"]
    accel = list(df[df["name"] == car_selected].loc[:, "acceleration"])[0]
    disp = list(df[df["name"] == car_selected].loc[:, "displacement"])[0]

    ## Scale displacement
    disp_scl = disp/max(df["displacement"])*10


    ## Graph 2: Line plot with info about a particular model

    #### Creating figure
    fig_g2 = go.Figure()


    #### Data traces
    fig_g2.add_trace(
        go.Scatter(
            x=[0, accel], #df[df["name"] == dummy_entry]["acceleration"]
            y=[0, 60],
            line={
                "color": "blue",
                "width": disp_scl
            }
        )
    )


    #### Figure layout
    fig_g2.update_layout(
        title=car_selected,
        margin={
            "l": 0
        }
    )
    fig_g2.update_xaxes(range=[0, 8])


    return fig_g2








"------------------------------------------------------------------------------"
#############################
## Main execution function ##
#############################

if __name__ == "__main__":
    app.run_server()
