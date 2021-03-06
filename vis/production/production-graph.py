
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from plotly.subplots import make_subplots

# src: https://ec.europa.eu/eurostat/tgm/table.do?tab=table&init=1&plugin=0&language=en&pcode=t2020_rl100&tableSelection=1

# #############################################################################
# Read and clean the dataset
df = pd.read_csv(
    "C:\\Users\\ismae\\Documents\\GitHub\\dataseeds.github.io\\vis\\production\\resources-data.csv")

df.drop(columns=["Flag and Footnotes"], inplace=True)
df.rename(columns={"GEO_LABEL": "Country",
                   "UNIT": "Unit"}, inplace=True)
df.replace({"Euro per kilogram": "Euro per kg",
            "Euro per kilogram, chain linked volumes (2010)": "Euro per kg CLV (2010)",
            "Purchasing power standard (PPS) per kilogram": "PPS per kg",
            "Index, 2000=100": "Index 2000=100",
            "Germany (until 1990 former territory of the FRG)": "Germany"}, inplace=True)
df = df.query('GEO != ["EU27_2020", "EU28"]')
df['Value'] = df['Value'].replace({" ": "", ":": "0"}).astype(
    float).round(2).replace(0, "n.d.")
df.reset_index(inplace=True, drop=True)


dff = df.query('Unit=="Euro per kg CLV (2010)" & TIME==2019')

conf = {"autosizable": False, "displayModeBar": False, "doubleClickDelay": 1000,
        "fillFrame": False, "showTips": False, "showAxisDragHandles": False,
        "scrollZoom": False, "responsive": True}


# #############################################################################
# Map + table
fig = make_subplots(rows=2, cols=1, shared_xaxes=False,
                    vertical_spacing=0, row_heights=[0.35, 0.65],
                    specs=[[{"type": "choropleth"}], [{"type": "table"}]],
                    shared_yaxes=False)
fig.add_trace(
    go.Choropleth(colorscale='BuGn', locationmode='country names',
                  locations=dff['Country'], marker_line_color='gray',
                  marker_opacity=0.75, marker_line_width=0.5, showscale=False,
                  z=dff['Value'], hoverinfo='z+location'
                  ), row=1, col=1
)
dfp = df.query('TIME==2019').pivot_table('Value', 'Country',
                                         'Unit', lambda x: x.iloc[0]).reset_index()
fig.add_trace(
    go.Table(
        header=dict(align="center", font_size=10, fill_color="rgba(98, 192, 165, 0.46)",
                    values=dfp.columns.tolist()),
        cells=dict(align="center", values=[
                   dfp[k].tolist() for k in dfp.columns]),
    ),
    row=2, col=1
)

buttons = []
for year in df['TIME'].unique():
    dfp = df.query('TIME==@year').pivot_table('Value', 'Country',
                                              'Unit', lambda x: x.iloc[0]).reset_index()
    buttons.append(
        dict(method='update', label=str(year),
             args=[{"cells": dict(values=[dfp[k].tolist() for k in dfp.columns]),
                    "z": [df.query('TIME==@year & Unit=="Euro per kg CLV (2010)"')['Value']]}])
    )

fig.update_layout(updatemenus=[dict(active=0, buttons=buttons, bgcolor="#FFFFFF",
                                    direction="down",
                                    pad={"r": 0, "t": 0, "l": 0, "b": 0},
                                    x=0.03, xanchor="left", yanchor="top")],
                  autosize=True, dragmode=False,
                  geo=dict(
                      scope='europe', bgcolor="#F0F0F0", projection_scale=1.2,
                      center=dict(lat=60, lon=15)
),
    margin={"r": 0, "t": 20, "l": 0, "b": 0,
            "pad": 0, "autoexpand": True},
    paper_bgcolor="#F0F0F0",
    height=1300)

fig.show(config=conf)

fig.write_html("C:\\Users\\ismae\\Documents\\GitHub\\dataseeds.github.io\\pages\\production-graph.html",
               config=conf)
