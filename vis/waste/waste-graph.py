
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

pd.set_option("display.max_columns", 40)
pd.set_option("display.max_colwidth", 200)

df = pd.read_csv(
    "C:\\Users\\ismae\\Documents\\GitHub\\dataseeds.github.io\\vis\\waste\\waste_gen-data.csv")

df = df.drop(columns=["Flag and Footnotes", "NACE_R2", "NACE_R2_LABEL"])
df = df.query('GEO != ["EU27_2020", "EU28"]')
df['Value'] = df['Value'].str.replace(' ', '').replace(':', '0')

df = df.query('HAZARD == "HAZ_NHAZ"')
df = df.query('WASTE_LABEL == "Total waste"')

dfg = df.groupby(['TIME', 'GEO', 'UNIT', 'WASTE'])
df.reset_index(inplace=True)

dff = df.copy().query('TIME == 2016')


CONF = {"autosizable": False, "displayModeBar": False, "doubleClickDelay": 1000,
        "fillFrame": False, "showTips": False, "showAxisDragHandles": False,
        "scrollZoom": False, "responsive": True}

# #############################################################################
# Map
fig = go.Figure(go.Choropleth(colorscale='BuGn', locationmode='country names',
                              locations=dff['GEO_LABEL'],
                              marker_line_color='gray', marker_opacity=0.75,
                              marker_line_width=0.5, showscale=True,
                              z=dff['Value'])
                )

buttons = []
for year in df['TIME'].unique():
    buttons.append(
        dict(method='update', label=str(year),
             args=[{"z": [df.query('TIME == @year')['Value']]}])
    )

fig.update_layout(updatemenus=[dict(active=6, buttons=buttons, bgcolor="#FFFFFF",
                                    direction="down",
                                    pad={"r": 0, "t": 0, "l": 0, "b": 0},
                                    x=0.03, xanchor="left", yanchor="top")],
                  autosize=True, dragmode=False,
                  geo=dict(
                      scope='europe', bgcolor="#F0F0F0", projection_scale=1.2,
                      center=dict(lat=60, lon=15)),
                  margin={"r": 0, "t": 20, "l": 0, "b": 0,
                          "pad": 0, "autoexpand": True},
                  paper_bgcolor="#F0F0F0", height=450)

fig.show(config=CONF)

fig.write_html("C:\\Users\\ismae\\Documents\\GitHub\\dataseeds.github.io\\pages\\waste-graph.html",
               config=CONF)
