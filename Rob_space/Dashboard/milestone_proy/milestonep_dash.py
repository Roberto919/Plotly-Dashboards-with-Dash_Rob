## MODULE WITH DASHBOARD LAYOUT





"------------------------------------------------------------------------------"
#############
## Imports ##
#############


## Standard library imports

from datetime import date


## Third party imports

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import (
    Input,
    Output,
    State
)
import plotly.graph_objs as go

import pandas as pd


## Local application imports

from milestonep_params import (
    datareader_api,
    def_company,
    def_start,
    def_end,
    dash_title,
    dash_stock_sel,
    dash_date_sel,
    tickers_base
)

from milestonep_funcs import (
    stock_graph
)





"------------------------------------------------------------------------------"
######################
## Dashboard layout ##
######################


## Initializing dashboard
app = dash.Dash()


## Dashboard layout
app.layout = html.Div( ## Master div
    [
        html.Div( ## Dashboard title
            [
                dcc.Markdown(dash_title)
            ]
        ),
        html.Div( ## Select menus
            [
                html.Div( ## Stock select dropdown
                    [
                        dcc.Markdown(dash_stock_sel),
                        dcc.Dropdown(
                            id="select_stock",
                            options=[{"label": cmp, "value": tickers_base[cmp]["symbol"]} for cmp in tickers_base],
                            value=["TSLA", "GE"],
                            multi=True
                        )
                    ],
                    style={
                        "display": "inline-block",
                        "width": "20%"
                    }
                ),
                html.Div( ## Date select dcc components
                    [
                        dcc.Markdown(dash_date_sel),
                        dcc.DatePickerRange(
                            id="select_dates",
                            min_date_allowed=date(2015, 1, 1),
                            max_date_allowed=date.today(),
                            initial_visible_month=date(2015, 1, 1),
                            end_date=date.today()
                        )
                    ],
                    style={
                        "display": "inline-block",
                        "width": "30%",
                        "margin-left": "20px",
                        "verticalAlign": "top"
                    }
                ),
                html.Div( ## Submit button
                    [
                        html.Button(
                            "Submit",
                            id="submit_but",
                        )
                    ],
                    style={
                        "display": "inline-block",
                        "width": "30%",
                        "margin-up": "100px",
                        "margin-left": "20px",
                        # "verticalAlign": "top"
                    }
                ),
            ]
        ),
        html.Div( ## Stock prices graph
            [
                dcc.Graph(
                    id="cstock_graph",
                    figure=stock_graph(def_company, datareader_api, def_start, def_end)
                )
            ]
        )
    ]
)





"------------------------------------------------------------------------------"
########################
## Callback functions ##
########################


@app.callback(
    Output("cstock_graph", "figure"),
    [
        Input("submit_but", "n_clicks")
    ],
    [
        State("select_stock", "value"),
        State("select_dates", "start_date"),
        State("select_dates", "end_date"),
    ],
)
## Updating closing prices stock price based on company dropdown and dates menu selection.
def update_graph(n_clicks, sel_company, sel_start_date, sel_end_date):
    """
    """

    ## Creating figure
    fig = stock_graph(sel_company, datareader_api, sel_start_date, sel_end_date)

    return fig
