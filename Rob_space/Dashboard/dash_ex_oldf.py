## CODE FOR OLD FAITHFUL DASHBOARD EXERCISE.





#############
## Imports ##
#############
import pandas as pd

import plotly.offline as pyo
import plotly.graph_objs as go

import dash
import dash_core_components as dcc
import dash_html_components as html





##########
## Data ##
##########
df_of = pd.read_csv("../../Data/OldFaithful.csv")





###########################
## Graphs - Scatter plot ##
###########################

data = [
    go.Scatter(
        x=df_of["X"],
        y=df_of["Y"],
        mode="markers"
    )
]

layout = go.Layout(
    title='Old Faithful Eruption Intervals vs. Durations',
    xaxis={
        "title": "Duration of eruption [mins]"
    },
    yaxis={
        "title": "Interval to next eruption [mins]"
    }
)

fig_sc = go.Figure(
    data=data,
    layout=layout
)

# fig_sc.update_layout(
#     title="Old Faithful Eruption Intervals vs. Durations",
# )

# pyo.plot(fig_sc)

# fig_sc.show()





##############
## Dasboard ##
##############

app = dash.Dash()

app.layout = html.Div(
    [
        dcc.Graph(
            id="Scatter_old_faithful",
            figure=fig_sc
        )
    ]
)





#############################
## Main execution function ##
#############################

if __name__ == "__main__":
    app.run_server()
