
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import plotly.figure_factory as ff
from plotly.subplots import make_subplots

pd.set_option("display.max_columns", 40)
pd.set_option("display.max_colwidth", 200)

path = "C:\\Users\\ismae\\Documents\\GitHub\\dataseeds.github.io"
df = pd.read_csv(
    path + "\\vis\\finance\\ESIF.2014-20-Finance.Implementation.csv")

pie = df.query('year == 2020 & Fund == "EAFRD"').groupby(
    ['TO_short'])["Total_Amount_planned"].sum().sort_values()

pie = pie.apply(lambda x: int(x/10e+5))


conf = {"autosizable": False,
        "fillFrame": False,
        "displayModeBar": False,
        "showTips": False,
        "showAxisDragHandles": False,
        "scrollZoom": False,
        "responsive": True,
        "doubleClickDelay": 1000}

colorlist = ["#143129", "#193e33", "#1e4a3d", "#276251", "#317a65", "#3b9279", "#44ab8d",
             "#56bb9e", "#6ec5ac", "#92d3c1", "#abddcf"]


# Plotly Graph Objects (GO)
labels = pie.index.tolist()
values = pie.values.tolist()

fig = go.Figure(data=go.Pie(labels=labels, values=values))

fig.update_layout(paper_bgcolor="#F0F0F0", height=400, margin={
                  "r": 0, "t": 10, "l": 0, "b": 10, "pad": 0, "autoexpand": True},)
fig.update_traces(hoverinfo='label+percent+value', textinfo='percent',
                  showlegend=False,
                  marker=dict(colors=colorlist,
                              line=dict(color='rgba(0, 0, 0, 0.2)', width=1)))


fig.show(config=conf)


fig.write_html("C:\\Users\\ismae\\Documents\\GitHub\\dataseeds.github.io\\pages\\finance-piechart.html",
               config=conf)
