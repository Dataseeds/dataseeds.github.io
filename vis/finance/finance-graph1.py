
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import plotly.figure_factory as ff
from plotly.subplots import make_subplots

pd.set_option("display.max_columns", 40)
pd.set_option("display.max_colwidth", 200)

path = "C:\\Users\\ismae\\Documents\\GitHub\\dataseeds.github.io"
df = pd.read_csv(path + "\\vis\\finance\\ESIF.2014-20-Finance.Implementation.csv")

df.groupby(["geo", "Transport mode"])["obsValue"].sum()

# Plotly Graph Objects (GO)
fig = go.Figure(layout=dict(
                    legend=dict(
                        xanchor="right",
                        x=0.9),
                    margin={"r": 0, "t": 30, "l": 0, "b": 0, "pad": 0},
                    title="<b>1990-2017 — Change in final energy consumption by transport mode</b>",
                    title_font=dict(size=16, family='PT Sans Narrow'),
                    paper_bgcolor = "#F0F0F0",
                    plot_bgcolor="#F0F0F0",
                    xaxis={"zerolinecolor": "#FFFFFF",
                           "showgrid": False,
                           "ticksuffix": "%"},
                    yaxis={"showgrid": False,
                           "categoryorder": "array",
                           "categoryarray": ["Final consumption - transport sector - road - energy use",
                           "Air Domestic/International",
                           "International maritime bunkers",
                           "Final consumption - transport sector - rail - energy use",
                           "Final consumption - transport sector - domestic navigation - energy use"]}))
fig.add_trace(go.Bar(
    y=df.query('geo == "EEA-33"')["Transport mode"].values,
    x=df.query('geo == "EEA-33"')["obsValue"].values,
    name='EEA-33',
    orientation='h',
    marker=dict(
        color='rgba(255, 204, 100, 0.6)',
        line=dict(color='rgba(255, 204, 100, 1.0)', width=1)
    )
))
fig.add_trace(go.Bar(
    y=df.query('geo == "EU-13"')["Transport mode"].values,
    x=df.query('geo == "EU-13"')["obsValue"].values,
    name='EU-13',
    orientation='h',
    marker=dict(
        color='rgba(51, 153, 255, 0.6)',
        line=dict(color='rgba(51, 153, 255, 1.0)', width=1)
    )
))
fig.add_trace(go.Bar(
    y=df.query('geo == "EU-15"')["Transport mode"].values,
    x=df.query('geo == "EU-15"')["obsValue"].values,
    name='EU-15',
    orientation='h',
    marker=dict(
        color='rgba(13, 137, 13, 0.6)',
        line=dict(color='rgba(13, 137, 13, 1.0)', width=1)
    )
))

conf = {"autosizable": False,
        "fillFrame": False,
        "displayModeBar": False,
        "showTips": False,
        "showAxisDragHandles": False,
        "scrollZoom": False,
        "responsive": True,
        "doubleClickDelay": 1000}
fig.show(config=conf)


fig.write_html("C:\\Users\\ismae\\Documents\\GitHub\\dataseeds.github.io\\transport-graph-change.html",
               config=conf)



fig = go.Figure(go.Table(
    header=dict(values=list(df['Transport mode'].unique()),
                align='left'),
    cells=dict(values=df.query('geo == "EEA-33"')['obsValue'],
               fill_color='lavender',
               align='center'))
)
button_EU13  = dict(method= 'update', label='EU-13',
                    args=[{"cells": dict(values=df.query('geo == "EU-13"')['obsValue'])}])
button_EU15  = dict(method= 'update', label='EU-15',
                    args=[{"cells": dict(values=df.query('geo == "EU-15"')['obsValue'])}])
button_EEA33 = dict(method= 'update', label='EEA-33', 
                    args=[{"cells": dict(values=df.query('geo == "EEA-33"')['obsValue'])}])
buttons = [button_EU13, button_EU15, button_EEA33]
fig.update_layout(updatemenus=[dict(active=0,
                                    buttons=buttons,
                                    bgcolor="#FFFFFF",
                                    direction="down",
                                    pad={"r": 0, "t": 0, "l": 0, "b": 0},
                                    x=0.1,
                                    xanchor="left",
                                    yanchor="top"
                                    )]);




map1 = go.Choropleth(
                colorscale='Greens',
                locationmode='country names',
                locations=dff['GEO_LABEL'],
                marker_line_color='gray',
                marker_opacity=0.75,
                marker_line_width=0.5,
                z=dff['Value'],
            )
map1_layout = dict(
    autosize=True,
    geo=dict(
        scope='europe',
        bgcolor="#F0F0F0",
        projection_scale=1.2,
        center=dict(lat=60, lon=15)
    ),
    height=400,
    margin={"r": 0, "t": 90, "l": 0, "b": 0, "pad": 0, "autoexpand": True},
    paper_bgcolor = "#F0F0F0",
    width=500,
)


table1 = go.Table(
    header=dict(values=list(df['Transport mode'].unique()), align='left'),
    cells=dict(values=df.query('geo == "EEA-33"')['obsValue'],
               fill_color='lavender', align='center')
)
go.Figure(data=[map1, table1], layout=map1_layout)

button_EU13  = dict(method= 'update', label='EU-13',
                    args=[{"cells": dict(values=df.query('geo == "EU-13"')['obsValue'])}])
button_EU15  = dict(method= 'update', label='EU-15',
                    args=[{"cells": dict(values=df.query('geo == "EU-15"')['obsValue'])}])
button_EEA33 = dict(method= 'update', label='EEA-33', 
                    args=[{"cells": dict(values=df.query('geo == "EEA-33"')['obsValue'])}])
buttons = [button_EU13, button_EU15, button_EEA33]
fig.update_layout(updatemenus=[dict(active=0,
                                    buttons=buttons,
                                    bgcolor="#FFFFFF",
                                    direction="down",
                                    pad={"r": 0, "t": 0, "l": 0, "b": 0},
                                    x=0.1,
                                    xanchor="left",
                                    yanchor="top"
                                    )]);

fig.show();