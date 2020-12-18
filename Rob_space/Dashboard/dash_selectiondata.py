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





"------------------------------------------------------------------------------"
#########################
## Ancillary functions ##
#########################
def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, "rb").read())
    return "data:image/png;base64,{}".format(encoded.decode())





"------------------------------------------------------------------------------"
##########
## Data ##
##########
df = pd.read_csv("../../Data/wheels.csv")





"------------------------------------------------------------------------------"
###############
## Dashboard ##
###############


app = dash.Dash()

app.layout = html.Div(
    [
        html.Div( ## Div to hold graph
            [
                dcc.Graph(
                    id="wheels-plot",
                    figure={
                        "data": [
                            go.Scatter(
                                x=df["color"],
                                y=df["wheels"],
                                dy=1,
                                mode="markers",
                                marker={
                                    "size": 12,
                                    "color": "rgb(51, 204, 153)",
                                    "line": {"width": 2}
                                }
                            )
                        ],
                        "layout": go.Layout(
                            title="Wheels & Colors Scatterplot",
                            xaxis={"title": "Color"},
                            yaxis={
                                "title": "# of Wheels",
                                "nticks": 3
                            },
                            hovermode="closest"
                        )
                    }
                )
            ],
            style={
                "width": "30%",
                "display": "inline-block"
            }
        ),
        html.Div( ## Div to hold hover data results
            [
                html.Pre(
                    id="selection",
                    style={"paddingTop": 25}
                )
            ],
            style={
                "width": "30%",
                "display": "inline-block",
                "verticalAlign": "top"
            }
        ),
    ]
)



## Callbacks
@app.callback(
    Output("selection", "children"),
    [Input("wheels-plot", "selectedData")]
)
def callback_image(selectedData):
    """
    """

    return_val = json.dumps(selectedData, indent=2)

    return return_val





"------------------------------------------------------------------------------"
#############################
## Main execution function ##
#############################

if __name__ == "__main__":
    app.run_server()
