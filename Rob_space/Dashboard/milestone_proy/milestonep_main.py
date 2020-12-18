## MILESTONE PROYECT MAIN EXECUTION FUNCTION





"------------------------------------------------------------------------------"
#############
## Imports ##
#############


## Standard library imports


## Third party imports

import plotly.offline as pyo

import pandas as pd


## Local application imports

from milestonep_params import (
    datareader_api,
    def_company,
    def_start,
    def_end,
)

from milestonep_funcs import (
    stock_graph
)





"------------------------------------------------------------------------------"
############################################
## Milesone proyect orchestrator function ##
############################################


## Orchestrator function
def orch_func():
    """
    """

    ## Creating stock prices graph
    fig_cstock = stock_graph(def_company, datareader_api, def_start, def_end)

    pyo.plot(fig_cstock)





"------------------------------------------------------------------------------"
#############################
## Main execution function ##
#############################


## Main function
if __name__ == '__main__':
    orch_func()
