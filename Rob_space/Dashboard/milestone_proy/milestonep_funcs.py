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
def stock_graph(companies_sym, datareader_api, start, end):
    """
    """

    ## Creating graph
    fig = go.Figure()

    for company_sym in companies_sym:

        ## Getting closing stock price from data
        df_cstock = data.DataReader(company_sym, datareader_api, start, end)["Close"]

        fig.add_trace(
            go.Scatter(
                x=df_cstock.index,
                y=df_cstock,
                name=company_sym
            )
        )

    sel_companies_string = "".join(c if companies_sym.index(c) + 1 == len(companies_sym) else c + ", " for c in companies_sym)
    fig.update_layout(
        title=sel_companies_string + " Closing Prices"
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
