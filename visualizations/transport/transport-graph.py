
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import plotly.figure_factory as ff
from plotly.subplots import make_subplots

pd.set_option("display.max_columns", 40)
pd.set_option("display.max_colwidth", 200)

df = pd.read_csv("C:\\Users\\ismae\\Documents\\GitHub\\dataseeds.github.io\\visualizations\\transport\\change-energy-consumption.csv")

dff = df.pivot_table('obsValue', 'geo', 'Transport mode').reset_index()

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

CONF = {"autosizable": True, "fillFrame": False, "displayModeBar": False,
        "showTips": False, "showAxisDragHandles": False, "scrollZoom": False,
        "responsive": True, "doubleClickDelay": 1000}

# #############################################################################
# Map + table with EU-13, EU-15 and EEA-33

fig = make_subplots(rows=2, cols=1, shared_xaxes=False,
    vertical_spacing=0,
    specs=[[{"type": "choropleth"}], [{"type": "table"}]],
    row_heights=[0.65, 0.35],
)
fig.add_trace(
    go.Choropleth(colorscale='Greens',
        hovertext=df.query('geo=="EU-13"')[["Transport mode", "obsValue"]],
        locationmode='country names', locations=EU13,
        marker_line_color='gray', marker_opacity=0.75, marker_line_width=0.5,
        showscale=False, z=[1]*35,
    ),
    row=1, col=1
)
fig.add_trace(
    go.Table(
        header=dict(
            values=dff.columns.tolist(),
            font=dict(size=10),
            align="center"
        ),
        cells=dict(
            values=[dff[k].tolist() for k in dff.columns],
            align = "center",
            fill=dict(color=[["#90ce96", "#e5ecf6", "#e5ecf6"]])
        )
    ),
    row=2, col=1
)


button_EU13  = dict(method= 'update', label='EU-13',
                    args=[{"locations": [EU13],
                           "cells":  dict(
                               values=[dff[k].tolist() for k in dff.columns],
                               fill=dict(color=[["#90ce96", "#e5ecf6", "#e5ecf6"]])
                            )}])
button_EU15  = dict(method= 'update', label='EU-15',
                    args=[{"locations": [EU15],
                           "cells":  dict(
                               values=[dff[k].tolist() for k in dff.columns],
                               fill=dict(color=[["#e5ecf6", "#90ce96", "#e5ecf6"]])
                            )}])
button_EEA33  = dict(method= 'update', label='EEA-33',
                    args=[{"locations": [EEA33],
                           "cells":  dict(
                               values=[dff[k].tolist() for k in dff.columns],
                               fill=dict(color=[["#e5ecf6", "#e5ecf6", "#90ce96"]])
                            )}])
buttons = [button_EU13, button_EU15, button_EEA33]
fig.update_layout(updatemenus=[dict(active=0,
                                    buttons=buttons,
                                    x=0.05,
                                    xanchor="left",
                                    yanchor="top")],
    autosize=True,
    dragmode=False,
    geo=dict(
        scope='europe',
        bgcolor="#F0F0F0",
        projection_scale=1.2,
        center=dict(lat=60, lon=15)
    ),
    margin={"r": 0, "t": 20, "l": 0, "b": 0, "pad": 0, "autoexpand": True},
    paper_bgcolor = "#F0F0F0");

fig.show()
fig.write_html("C:\\Users\\ismae\\Documents\\GitHub\\dataseeds.github.io\\transport-graph-change.html",
               config=CONF)


"""

# #############################################################################
# Map only with EU-13, EU-15 and EEA-33
fig = go.Figure(
    data=[go.Choropleth(
        colorscale='Greens',
        hovertext=df.query('geo=="EU-13"')[["Transport mode", "obsValue"]],
        locationmode='country names', locations=EU13,
        marker_line_color='gray', marker_opacity=0.75, marker_line_width=0.5,
        showscale=False, z=[1]*35)
    ],
    layout=dict(autosize=True, dragmode=False, 
        geo=dict(scope='europe',
            bgcolor="#F0F0F0",
            projection_scale=1.2,
            center=dict(lat=60, lon=15)),
        margin={"r": 0, "t": 20, "l": 0, "b": 0, "pad": 0, "autoexpand": True},
        paper_bgcolor = "#F0F0F0"
    )
)

button_EU13  = dict(method= 'update', label='EU-13',  args=[{"locations": [EU13]}])
button_EU15  = dict(method= 'update', label='EU-15',  args=[{"locations": [EU15]}])
button_EEA33 = dict(method= 'update', label='EEA-33', args=[{"locations": [EEA33]}])
buttons = [button_EU13, button_EU15, button_EEA33]
fig.update_layout(updatemenus=[
    dict(active=0, buttons=buttons, bgcolor="#FFFFFF", direction="down",
         pad={"r": 0, "t": 0, "l": 0, "b": 0}, x=0.1, xanchor="left",
         yanchor="top")]);
fig.show(conf=conf);


# #############################################################################
# Map + table with EU-13, EU-15 and EEA-33
fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
    vertical_spacing=0.03,
    specs=[[{"type": "choropleth"}], [{"type": "table"}]],
    row_heights=[0.85, 0.15]
)
fig.add_trace(
    go.Choropleth(colorscale='Greens',
        hovertext=df.query('geo=="EU-13"')[["Transport mode", "obsValue"]],
        locationmode='country names', locations=EU13,
        marker_line_color='gray', marker_opacity=0.75, marker_line_width=0.5,
        showscale=False, z=[1]*35,
    ),
    row=1, col=1
)
fig.add_trace(
    go.Table(
        header=dict(
            values=df.query('geo=="EU-13"').pivot_table('obsValue', 'geo', 'Transport mode').columns.tolist(),
            font=dict(size=10),
            align="center"
        ),
        cells=dict(
            values=df.query('geo=="EU-13"').pivot_table('obsValue', 'Transport mode'),
            align = "center"
        )
    ),
    row=2, col=1
)


button_EU13  = dict(method= 'update', label='EU-13',
                    args=[{"locations": [EU13], "cells": dict(values=df.query('geo == "EU-13"')['obsValue']) }])
button_EU15  = dict(method= 'update', label='EU-15',
                    args=[{"locations": [EU15], "cells": dict(values=df.query('geo == "EU-15"')['obsValue']) }])
button_EEA33  = dict(method= 'update', label='EEA-33',
                    args=[{"locations": [EEA33], "cells": dict(values=df.query('geo == "EEA-33"')['obsValue']) }])
buttons = [button_EU13, button_EU15, button_EEA33]
fig.update_layout(updatemenus=[dict(active=0, buttons=buttons)], autosize=True,
                  dragmode=False,
                  geo=dict(
                      scope='europe', bgcolor="#F0F0F0", projection_scale=1.2,
                      center=dict(lat=60, lon=15)),
                  margin={"r": 0, "t": 20, "l": 0, "b": 0, "pad": 0, "autoexpand": True},
                  paper_bgcolor = "#F0F0F0");
fig.show()
"""