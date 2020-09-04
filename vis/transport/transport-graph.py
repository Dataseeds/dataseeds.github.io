
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import plotly.figure_factory as ff
from plotly.subplots import make_subplots

pd.set_option("display.max_columns", 40)
pd.set_option("display.max_colwidth", 200)

df = pd.read_csv("C:\\Users\\ismae\\Documents\\GitHub\\dataseeds.github.io\\vis\\transport\\change-energy-consumption.csv")

df.rename(columns={"geo": "Eurozone",
                   "share": "Share"}, inplace=True)

dff = df.pivot_table('obsValue', 'Eurozone', 'Transport mode').reset_index()

# #############################################################################
# variables
EU13=["Bulgaria", "Czech Republic", "Cyprus", "Estonia", "Croatia", "Hungary",
      "Lithuania", "Latvia", "Malta", "Poland", "Romania", "Slovenia", "Slovakia"]
EU15 = ["Austria", "Belgium", "Denmark", "Finland", "France", "Germany",
        "Greece", "Ireland", "Italy", "Luxembourg", "Netherlands", "Portugal",
        "Spain", "Sweden", "United Kingdom"]
EEA33 = ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic',
         'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece',
         'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 'Liechtenstein',
         'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Norway', 'Poland',
         'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Spain', 'Sweden',
         'United Kingdom']

conf = {"autosizable": False, "displayModeBar": False, "doubleClickDelay": 1000,
        "fillFrame": False, "showTips": False, "showAxisDragHandles": False,
        "scrollZoom": False, "responsive": True}

# #############################################################################
# Map + table with EU-13, EU-15 and EEA-33

fig = make_subplots(rows=2, cols=1, shared_xaxes=False,
                    vertical_spacing=0, row_heights=[0.65, 0.35],
                    specs=[[{"type": "choropleth"}], [{"type": "table"}]],
                    shared_yaxes=False)
)
fig.add_trace(
    go.Choropleth(colorscale='Greens', hovertext=[],
        locationmode='country names', locations=EEA33,
        marker_line_color='gray', marker_opacity=0.75, marker_line_width=0.5,
        showscale=False, z=[1]*35, hoverinfo='location'
    ),
    row=1, col=1
)
fig.add_trace(
    go.Table(
        header=dict(values=dff.columns.tolist(), font=dict(size=10), align="center"),
        cells=dict(
            values=[dff[k].tolist() for k in dff.columns],
            align = "center", fill=dict(color=[["#90ce96", "#e5ecf6", "#e5ecf6"]])
        ),
    ),
    row=2, col=1
)


button_EEA33  = dict(method= 'update', label='EEA-33',
                     args=[{"locations": [EEA33],
                            "cells":  dict(
                                values=[dff[k].tolist() for k in dff.columns],
                                fill=dict(color=[["#90ce96", "#e5ecf6", "#e5ecf6"]]) )}])
button_EU13  = dict(method= 'update', label='EU-13',
                    args=[{"locations": [EU13],
                           "cells":  dict(
                               values=[dff[k].tolist() for k in dff.columns],
                               fill=dict(color=[["#e5ecf6", "#90ce96", "#e5ecf6"]]) )}])
button_EU15  = dict(method= 'update', label='EU-15',
                    args=[{"locations": [EU15],
                           "cells":  dict(
                               values=[dff[k].tolist() for k in dff.columns],
                               fill=dict(color=[["#e5ecf6", "#e5ecf6", "#90ce96"]]) )}])
buttons = [button_EEA33, button_EU13, button_EU15]
fig.update_layout(updatemenus=[dict(active=0, buttons=buttons, bgcolor="#FFFFFF",
                                    x=0.03, xanchor="left", yanchor="top")],
                  autosize=True, dragmode=False,
                  geo=dict(
                      scope='europe', bgcolor="#F0F0F0", projection_scale=1.2,
                      center=dict(lat=60, lon=15)
                    ),
                  margin={"r": 0, "t": 20, "l": 0, "b": 0, "pad": 0, "autoexpand": True},
                  paper_bgcolor = "#F0F0F0",
                  height = 700)

fig.show(config=conf)
fig.write_html("C:\\Users\\ismae\\Documents\\GitHub\\dataseeds.github.io\\vis\\transport.html",
               config=conf)
