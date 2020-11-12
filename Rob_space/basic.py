## MODULE CREATED FOR Section 3: Plotly Basics





## Imports
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go





## Creating scatter plot

#### Creating random data for chart
np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)


#### Creating chart
data = [
    go.Scatter(
        x=random_x,
        y=random_y,
        mode="markers",
        marker={
            "size": 12,
            "color": "rgb(51, 204, 153)",
            "symbol": "pentagon",
            "line": {"width": 2}
        }
    ),
]

layout = go.Layout(
    title="Hello first plot",
    xaxis={
        "title":"MY X AXIS",
    },
    yaxis=dict(title="MY X AXIS"),
    hovermode="closest"
)

fig = go.Figure(data=data, layout=layout)

# pyo.plot(fig, filename="scatter.html")



## Creating line plot

#### Creating random data for chart
np.random.seed(56)
x_values = np.linspace(0, 1, 100)
y_values = np.random.randn(100)



#### Creating chart
trace0 = go.Scatter(
    x=x_values,
    y=(y_values + 5),
    mode="markers",
    name="markers"
)

trace1 = go.Scatter(
    x=x_values,
    y=(y_values),
    mode="lines",
    name="mylines"
)

trace2 = go.Scatter(
    x=x_values,
    y=(y_values - 5),
    mode="lines+markers",
    name="my fav"
)


data = [trace0, trace1, trace2]

layout = go.Layout(
    title="Line Charts"
)

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename="line_chart.html")
