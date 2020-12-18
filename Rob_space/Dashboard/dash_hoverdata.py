## LEARNING HOW EXPLOIT HOVER DATA





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
                                    "size": 15
                                }
                            )
                        ],
                        "layout": go.Layout(
                            title="Test",
                            hovermode="closest"
                        )
                    }
                )
            ],
            style={
                "width": "30%",
                "float": "left"
            }
        ),
        html.Div( ## Div to hold hover data results
            [
                html.Img(
                    id="hover-image",
                    src="children",
                    height=300
                )
            ],
            style={"paddingTop": 35}
        ),
    ]
)



## Callbacks
@app.callback(
    Output("hover-image", "src"),
    [Input("wheels-plot", "hoverData")] ## hoverData is part of any dcc.Graph component.
)
def callback_image(hoverData):
    """
    """

    wheel = hoverData["points"][0]["y"]
    color = hoverData["points"][0]["x"]
    path = "../../data/images/"
    return_image = encode_image(
        path +
        list(df.loc[
            ((df["wheels"] == wheel) &
            (df["color"] == color)),
            "image"
        ])[0]
    )

    return return_image





"------------------------------------------------------------------------------"
#############################
## Main execution function ##
#############################

if __name__ == "__main__":
    app.run_server()
