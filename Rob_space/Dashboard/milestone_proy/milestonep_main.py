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

from milestonep_funcs import (
    stock_graph
)

from milestonep_dash import app





"------------------------------------------------------------------------------"
############################################
## Milesone proyect orchestrator function ##
############################################


## Orchestrator function
def orch_func():
    """
    """

    ## Creating stock prices graph
    # fig_cstock = stock_graph(def_company, datareader_api, def_start, def_end)
    #
    # pyo.plot(fig_cstock)
    app.run_server()





"------------------------------------------------------------------------------"
#############################
## Main execution function ##
#############################


## Main function
if __name__ == '__main__':
    orch_func()
