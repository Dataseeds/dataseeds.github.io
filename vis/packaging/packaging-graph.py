
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from plotly.subplots import make_subplots

# src: https://www.eea.europa.eu/data-and-maps/daviz/sds/packaging-waste-recycling-2/@@view

# #############################################################################
# Read and clean the dataset
df = pd.read_csv(
    "C:\\Users\\ismae\\Documents\\GitHub\\dataseeds.github.io\\vis\\packaging\\packaging-waste-recycling.csv")

df.drop(columns=["target_2008", "target_2025", "target_2030"], inplace=True)
df.rename(columns={"generated_waste": "Generated",
                   "recycled_waste": "Recycled",
                   "ugeo": "Country",
                   "share": "Share"}, inplace=True)
df = df.astype({"Generated": int, "Recycled": int})


df1 = df.query('date==2005').drop(columns="date")
df2 = df.query('date==2016').drop(columns="date")
dff = df1.merge(df2, on="Country", suffixes=["_2005", "_2016"])

conf = {"autosizable": False, "displayModeBar": False, "doubleClickDelay": 1000,
        "fillFrame": False, "showTips": False, "showAxisDragHandles": False,
        "scrollZoom": False, "responsive": True}


def human_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    # add more suffixes if you need them
    n = ("%.3f" % num).strip("0").strip(".")
    return "%s %s" % (n, [' kg', ' Ton', ' KTon'][magnitude])


def readable_format(num):
    return "{:.2f}".format(num / 1000).strip("0").strip(".") + " Ton"


df["Generated"] = df["Generated"].apply(lambda x: readable_format(x))
df["Recycled"] = df["Recycled"].apply(lambda x: readable_format(x))
df["Share"] = df["Share"].apply(lambda x: str(x) + "%")

# #############################################################################
# Map + table
fig = make_subplots(rows=2, cols=1, shared_xaxes=False,
                    vertical_spacing=0, row_heights=[0.4, 0.6],
                    specs=[[{"type": "choropleth"}], [{"type": "table"}]],
                    shared_yaxes=False)
fig.add_trace(
    go.Choropleth(colorscale='BuGn', locationmode='country names',
                  locations=dff['Country'], marker_line_color='gray',
                  marker_opacity=0.75, marker_line_width=0.5, showscale=False,
                  z=dff['Share_2016'], hoverinfo='z+location'
                  ), row=1, col=1
)
fig.add_trace(
    go.Table(
        header=dict(values=df.columns[1:].tolist(),
                    font=dict(size=10), align="center"),
        cells=dict(
            values=[df.query('date==2016')[k].tolist()
                    for k in df.columns[1:]],
            align="center"
        ),
    ),
    row=2, col=1
)

buttons = []
for year in [2005, 2016]:
    dfp = df.query('date==@year').reset_index()
    buttons.append(
        dict(method='update', label=str(year),
             args=[{"cells": dict(values=[df.query('date==@year')[k].tolist() for k in df.columns[1:]]),
                    "z": [df.query('date==@year')['Share']]}])
    )

fig.update_layout(updatemenus=[dict(active=1, buttons=buttons, bgcolor="#FFFFFF",
                                    x=0.1, xanchor="left", yanchor="top")],
                  autosize=True, dragmode=False,
                  geo=dict(
                      scope='europe', bgcolor="#F0F0F0", projection_scale=1.2,
                      center=dict(lat=60, lon=15)
),
    margin={"r": 0, "t": 20, "l": 0, "b": 0,
            "pad": 0, "autoexpand": True},
    paper_bgcolor="#F0F0F0",
    height=1200)

fig.show(config=conf)

fig.write_html("C:\\Users\\ismae\\Documents\\GitHub\\dataseeds.github.io\\pages\\packaging-graph.html",
               config=conf)
