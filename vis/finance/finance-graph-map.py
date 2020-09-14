
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

df = df.rename(columns={'MS_name': 'Country',
                        'Total_Amount_planned': 'Planned',
                        'total_eligible_cost_decided_(selected)': 'Decided',
                        'total_eligible_spending': 'Spent'})

data = df.query('year == 2020').groupby(['Country'])[
    ["Planned", "Decided", "Spent"]].sum()

data = data.apply(lambda x: x/10e5)
data["decided"] = data.apply(lambda x: str(
    int(100*(x.Decided/x.Planned))), axis=1)
data["spent"] = data.apply(lambda x: str(
    int(100*(x.Spent/x.Planned))), axis=1)
data = data.reset_index()

data[["Planned", "Decided", "Spent"]] = data[[
    "Planned", "Decided", "Spent"]].astype(int)

conf = {"autosizable": False,
        "fillFrame": False,
        "displayModeBar": False,
        "showTips": False,
        "showAxisDragHandles": False,
        "scrollZoom": False,
        "responsive": True,
        "doubleClickDelay": 1000}


def make_hover_text(x):
    txt = "Total planned: {:,d} (100%) <br>".format(x.Planned)
    txt += "Decided: {:,d} ({}%) <br>".format(x.Decided, x.decided)
    txt += "Spent: {:,d} ({}%) <br>".format(x.Spent, x.spent)
    txt = txt.replace(',', '.')
    return txt


data["text"] = data.apply(lambda x: make_hover_text(x), axis=1)


# Plotly Graph Objects (GO)
# Map + table
fig = go.Figure(go.Choropleth(colorscale='BuGn', hoverinfo='location+text',
                              locationmode='country names', locations=data['Country'],
                              marker_line_color='gray', marker_opacity=0.75,
                              marker_line_width=0.5, showscale=False,
                              text=data["text"], z=data['spent']
                              ))

fig.update_layout(autosize=True, dragmode=False,
                  geo=dict(
                      scope='europe', bgcolor="#F0F0F0", projection_scale=1.2,
                      center=dict(lat=60, lon=15)),
                  margin={"r": 0, "t": 20, "l": 0, "b": 0,
                          "pad": 0, "autoexpand": True},
                  paper_bgcolor="#F0F0F0",
                  height=400)

fig.show(config=conf)


fig.write_html("C:\\Users\\ismae\\Documents\\GitHub\\dataseeds.github.io\\pages\\finance-map.html",
               config=conf)
