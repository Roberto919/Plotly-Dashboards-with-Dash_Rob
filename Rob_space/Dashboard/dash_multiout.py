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

import base64





##########
## Data ##
##########
df = pd.read_csv("../../Data/wheels.csv")





###############
## Dashboard ##
###############

app = dash.Dash()



def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, "rb").read())
    return "data:image/png;base64,{}".format(encoded.decode())



## Dashboard layout
app.layout = html.Div(
    [
        dcc.RadioItems(
            id="wheels",
            options=[{"label": i, "value": i} for i in df["wheels"].unique()],
            value=1
        ),
        html.Div(
            id="wheels-output"
        ),
        html.Hr(),
        dcc.RadioItems(
            id="colors",
            options=[{"label": i, "value": i} for i in df["color"].unique()],
            value="blue"
        ),
        html.Div(
            id="colors-output"
        ),
        html.Img(
            id="display-image",
            src="children",
            height=300
        ),
    ],
    style={
        "fontFamily": "helvetica",
        "fontSize": 18
    }
)




## Callbacks
@app.callback(
    Output("wheels-output", "children"),
    [Input("wheels", "value")]
)
def callback_a(wheels_value):
    return "You chose {}".format(wheels_value)



@app.callback(
    Output("colors-output", "children"),
    [Input("colors", "value")]
)
def callback_b(colors_value):
    return "You chose {}".format(colors_value)



@app.callback(
    Output("display-image", "src"),
    [Input("wheels", "value"), Input("colors", "value")]
)
def callback_image(wheel, color):

    path = "../../Data/Images/"

    return_image = encode_image(
        path +
        list(df.loc[
            ((df["wheels"] == wheel) &
            (df["color"] == color)),
            "image"
        ])[0]
    )

    print("return_image: ", return_image)

    return return_image





#############################
## Main execution function ##
#############################

if __name__ == "__main__":
    app.run_server()
