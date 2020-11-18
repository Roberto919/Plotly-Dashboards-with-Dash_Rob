## MODULE CREATED FOR Section 3: Plotly Basics





## Imports
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff





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

# pyo.plot(fig, filename="line_chart_exercise.html")



## Bar charts

df = pd.read_csv("../Data/2018WinterOlympics.csv")

trace1 = go.Bar(
    x=df["NOC"],
    y=df["Gold"],
    name="Gold",
    marker={"color": "#FFD700"}
)

trace2 = go.Bar(
    x=df["NOC"],
    y=df["Silver"],
    name="Silver",
    marker={"color": "#9EA0A1"}
)

trace3 = go.Bar(
    x=df["NOC"],
    y=df["Bronze"],
    name="Bronze",
    marker={"color": "#CD7F32"}
)

data = [trace1, trace2, trace3]

layout = go.Layout(title="Medals", barmode="stack") ## Barmode is the option to switch between stacked or nested.
fig = go.Figure(data=data, layout=layout)
# pyo.plot(fig, filename="bar_medals.html")



## Bar chart exercise

df_bar_ex = pd.read_csv("../Data/mocksurvey.csv")
df_bar_ex.set_index("Unnamed: 0", inplace=True)


#### Vertical bar chart

data = [go.Bar(
    x=df_bar_ex.index,
    y=df_bar_ex.loc[:, col],
    name=col,
    )
for col in df_bar_ex.columns]

layout = go.Layout(title="Bar exercise - Vertical", barmode="stack")

fig = go.Figure(data=data, layout=layout)

# pyo.plot(fig, filename="bar_exercise_vertical.html")


#### Horizontal bar chart

data = [
    go.Bar(
        x=df_bar_ex.loc[:, col],
        y=df_bar_ex.index,
        name=col,
        orientation="h"
    )
for col in df_bar_ex.columns]

layout = go.Layout(title="Bar exercise - Horizontal", barmode="stack")

fig = go.Figure(data=data, layout=layout)

# pyo.plot(fig, filename="bar_exercise_horizontal.html")



## Bubble chart

df_bbl = pd.read_csv("../Data/mpg.csv")

# print(df_bbl.head())

data = [go.Scatter(
        x=df_bbl["horsepower"],
        y=df_bbl["mpg"],
        text=df_bbl["name"],
        mode="markers",
        marker={
            "size": df_bbl["weight"]/100,
            "color": df_bbl["cylinders"],
            "showscale": True
        },
    )
]

layout = go.Layout(title="Bubble chart")

fig = go.Figure(data=data, layout=layout)

# pyo.plot(fig, filename="bubble_chart.html")



## Box plot chart

#### Data
y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]


#### Box plot

data = [
    go.Box(
        y=y,
        boxpoints="all",
        jitter=0.3,
        pointpos=2.0
    )
]

# pyo.plot(data, filename="boxplot_tutorial.html")



## Box plot excercise

df_bpe = pd.read_csv("../Data/abalone.csv")

df_bpe1 = np.random.choice(df_bpe["rings"], 10, replace=False)
df_bpe2 = np.random.choice(df_bpe["rings"], 10, replace=False)

data = [
    go.Box(
        y=df_bpe1,
        name="sample_1"
    ),
    go.Box(
        y=df_bpe2,
        name="sample_2"
    )
]

# pyo.plot(data, filename="boxplot_ex.html")



## Distplots - tutprial

x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2
x4 = np.random.randn(200) + 4

hist_data = [x1, x2, x3, x4]
group_labels = ["X1", "X2", "X3", "X4"]

fig = ff.create_distplot(hist_data, group_labels, bin_size=[0.2, 0.1, 0.3, 0.4])
pyo.plot(fig, filename="distplot_tut.html")
