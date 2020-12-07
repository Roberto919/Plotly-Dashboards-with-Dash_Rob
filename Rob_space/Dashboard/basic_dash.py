## DASH MODULE


"-------------------------------------------------------------------------------"
#############
## Imports ##
#############

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np


## Data
np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)


app = dash.Dash()


app.layout = html.Div(
    [
        dcc.Graph(
            id="scatterplot",
            figure={
                "data": [
                    go.Scatter(
                        x=random_x,
                        y=random_y,
                        mode="markers",
                        marker={
                            "size": 12,
                            "color": "rgb(51, 204, 153)",
                            "symbol": "pentagon",
                            "line": {
                                "width": 2
                            }
                        }
                    )
                ],
                "layout": go.Layout(
                    title="My Scatterplot",
                    xaxis={
                        "title": "Some X title"
                    }
                )
            }
        ),
        dcc.Graph(
            id="scatterplot2",
            figure={
                "data": [
                    go.Scatter(
                        x=random_x,
                        y=random_y,
                        mode="markers",
                        marker={
                            "size": 12,
                            "color": "rgb(200, 204, 53)",
                            "symbol": "pentagon",
                            "line": {
                                "width": 2
                            }
                        }
                    )
                ],
                "layout": go.Layout(
                    title="Second plot",
                    xaxis={
                        "title": "Some X title"
                    }
                )
            }
        ),
    ]
)


## Creating base


colors = {
    "background": "#111111",
    "text": "#7FDBFF"
}



# app.layout = html.Div(children=[
#     html.H1(
#         "Hello Dash!",
#         style={
#             "textAlign": "center",
#             "color": colors["text"]
#         }
#     ),
#     dcc.Graph(
#         id="example",
#         figure={
#             "data": [
#                 {
#                     "x": [1, 2, 3],
#                     "y": [4, 1, 2],
#                     "type": "bar",
#                     "name": "SF"
#                 },
#                 {
#                     "x": [1, 2, 3],
#                     "y": [2, 4, 5],
#                     "type": "bar",
#                     "name": "NYC"
#                 },
#             ],
#             "layout": {
#                 "plot_bgcolor": colors["background"],
#                 "paper_bgcolor": colors["background"],
#                 "font": {
#                     "color": colors["text"]
#                 },
#                 "title": "BAR PLOTS!"
#             }
#         }
#     )
# ],
# style = {
#     "backgroundColor": colors["background"]
#     }
# )



## Executing file
if __name__ == "__main__":
    app.run_server()
