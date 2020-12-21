## MODULE WITH FUNCTIONS FOR THE MILESTONE PROYECT




"------------------------------------------------------------------------------"
#############
## Imports ##
#############


## Standard library imports


## Third party imports

import plotly.graph_objs as go

import pandas as pd
from pandas_datareader import data, wb

from dash.dependencies import (
    Input,
    Output,
    State
)


## Local application imports

from milestonep_params import (
    datareader_api,
    tickers_base,
)





"------------------------------------------------------------------------------"
#####################
## Graph functions ##
#####################


## Creating stock prices graph
def stock_graph(company_sym, datareader_api, start, end):
    """
    """

    ## Getting the company symbol
    # company_sym = tickers_base[company]["symbol"]

    ## Getting closing stock price from data
    df_cstock = data.DataReader(company_sym, datareader_api, start, end)["Close"]

    ## Creating graph
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df_cstock.index,
            y=df_cstock
        )
    )

    fig.update_layout(
        title=company_sym + " Closing Prices"
    )

    return fig





"------------------------------------------------------------------------------"
##################################
## Dashboard callback functions ##
##################################


## Updating company stock info based on dcc component
def update_company_sel(comp_sel):
    """
    """

    ##
    tckr_sel = tickers_base[comp_sel]["symbol"]

    return tckr_sel
