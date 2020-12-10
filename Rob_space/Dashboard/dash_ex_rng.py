## EXERCISE TO CREATE DASHBOARD WITH MULTIPLE INPUTS FOR A GRAPH





"------------------------------------------------------------------------------"
#############
## Imports ##
#############

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go

import pandas as pd





"------------------------------------------------------------------------------"
######################
## Dashboard layout ##
######################


## Initialize dashboard
app = dash.Dash()


## Layout
main_range_s_min = -15
main_range_s_max = 15
app.layout = html.Div( ## Main dashboard div
    [
        dcc.RangeSlider(
            id="main_range_s",
            min=main_range_s_min,
            max=main_range_s_max,
            step=1,
            value=[-5, 5],
            marks={str(i): str(i) for i in range(main_range_s_min, main_range_s_max + 1)}
        ),
        html.H1(
            id="main_range_s_out"
        ),
    ]
)





"------------------------------------------------------------------------------"
#########################
## Dashboard callbacks ##
#########################


## Main range slider callback
@app.callback(
    Output("main_range_s_out", "children"),
    [Input("main_range_s", "value")]
)
def main_range_s_callb(rs_vals):
    """
    """

    product = rs_vals[0]*rs_vals[1]

    # The values selected are: {} and {}\n\n \
    return_text = "The obtained product is: {}".format(product)

    return return_text





"------------------------------------------------------------------------------"
#############################
## Main execution function ##
#############################

if __name__ == "__main__":
    app.run_server()
