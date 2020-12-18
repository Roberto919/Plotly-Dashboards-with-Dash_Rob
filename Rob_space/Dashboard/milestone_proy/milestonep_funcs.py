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
def stock_graph(company, datareader_api, start, end):
    """
    """

    ## Getting closing stock price from data
    df_cstock = data.DataReader(company, datareader_api, start, end)["Close"]

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df_cstock.index
            y=df_cstock
        )
    )
