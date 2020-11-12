## MODULE CREATED FOR Section 3: Plotly Basics





## Imports
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px





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

# pyo.plot(fig, filename="line_chart.html")



## Creating chart with real data


## Importing data and filtering
df = pd.read_csv("../SourceData/nst-est2017-alldata.csv")

df2 = df[df["DIVISION"] == "1"]

df2.set_index("NAME", inplace=True)

list_of_pop_col = [col for col in df2.columns if col.startswith("POP")]
df2 = df2[list_of_pop_col]

data = [go.Scatter(
            x=df2.columns,
            y=df2.loc[name],
            mode="lines",
            name=name) for name in df2.index]

# pyo.plot(data, filename="lineplot_real_data.html")



## Line charts exercise
#### Develop chart


#### Import and working with data
df_yaz = pd.read_csv("../Data/2010YumaAZ.csv")


#### Creating plot
fig = px.line(
    x=df_yaz["LST_TIME"],
    y=df_yaz["T_HR_AVG"],
    color=df_yaz["DAY"],
)

pyo.plot(fig, filename="line_chart_exercise.html")
