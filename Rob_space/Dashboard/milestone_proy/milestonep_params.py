## MODULE WITH PARAMETERS FOR THE MILESTONE PROYECT





"------------------------------------------------------------------------------"
#############
## Imports ##
#############


## Standard library imports


## Third party imports


## Local application imports

from datetime import date





"------------------------------------------------------------------------------"
######################################
## General configuration parameters ##
######################################


## Pandas datareader
datareader_api = "yahoo"


## Stock graph base params
def_company = "TSLA Tesla, Inc."
def_start = date(2015, 1, 1)
def_end = date(2020, 12, 1)





"------------------------------------------------------------------------------"
##########################
## Stock market tickers ##
##########################


## List of the tickers that will be references
tickers_base = {
    "TSLA Tesla, Inc.": {
        "symbol": "TSLA",
        "name": "Tesla, Inc."
    },
    "AAPL Apple Inc.": {
        "symbol": "AAPL",
        "name": "Apple Inc."
    },
    "AMZN Amazon.com Inc.": {
        "symbol": "AMZN",
        "name": "Amazon.com Inc."
    },
    "GE General Electric Co.": {
        "symbol": "GE",
        "name": "General Electric Co."
    },
    "NVDA NVIDIA Corp.": {
        "symbol": "NVDA",
        "name": "NVIDIA Corp."
    },
}
