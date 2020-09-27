
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from plotly.subplots import make_subplots

pd.set_option("display.max_columns", 40)
pd.set_option("display.max_colwidth", 200)

df = pd.read_csv(
    "C:\\Users\\ismae\\Documents\\GitHub\\dataseeds.github.io\\vis\\waste\\waste_gen-data.csv")

df = df.drop(columns=["Flag and Footnotes", "NACE_R2", "NACE_R2_LABEL"])
df = df.query('GEO != ["EU27_2020", "EU28"]')
df['Value'] = df['Value'].str.replace(' ', '').replace(':', '0')

df = df.rename(columns={'GEO_LABEL': 'Country'})

df = df.query('HAZARD == "HAZ_NHAZ"')
df = df.query('WASTE_LABEL == "Total waste"')

df.replace({"Kosovo (under United Nations Security Council Resolution 1244/99)": "Kosovo",
            "Germany (until 1990 former territory of the FRG)": "Germany"}, inplace=True)

dfg = df.groupby(['TIME', 'GEO', 'UNIT', 'WASTE'])
df.reset_index(inplace=True)


COUNTRIES_DICT = {
    "Albania": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/albania-waste-prevention-fact-sheet/view",
    "Austria": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/austria-waste-prevention-fact-sheet/view",
    "Belgium": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/belgium/view",
    "Bosnia and Herzegovina": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/bosnia-herzegovina-waste-prevention-fact-sheet/view",
    "Bulgaria": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/bulgaria-waste-prevention-fact-sheet/view",
    "Croatia": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/croatia-waste-prevention-country-fact-sheet/view",
    "Cyprus": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/cyprus-waste-prevention-country-fact-sheet/view",
    "Czechia": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/czechia-waste-prevention-fact-sheet/view",
    "Denmark": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/denmark-fact-sheet-waste-prevention-oct2016/view",
    "Estonia": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/estonia-waste-prevention-fact-sheet/view",
    "Finland": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/finland-waste-prevention-country-fact-sheet/view",
    "France": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/france-waste-prevention-country-fact-sheet/view",
    "Germany": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/germany-waste-prevention-fact-sheet/view",
    "Greece": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/greece-fact-sheet-waste-prevention-oct2016/view",
    "Hungary": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/hungary-waste-prevention-fact-sheet/view",
    "Iceland": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/iceland-fact-sheet-waste-prevention-oct2016/view",
    "Ireland": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/ireland-waste-prevention-fact-sheet-2/view",
    "Italy": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/italy-waste-prevention-fact-sheet/view",
    "Kosovo": "#",
    "Latvia": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/latvia-waste-prevention-waste-sheet/view",
    "Liechtenstein": "#",
    "Lithuania": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/lithuania-waste-prevention-fact-sheet/view",
    "Luxembourg": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/luxembourg-waste-prevention-country-fact-sheet/view",
    "Malta": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/malta-waste-prevention-country-fact-sheet/view",
    "Montenegro": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/montenegro-waste-prevention-fact-sheet/view",
    "Netherlands": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/the-netherlands-waste-prevention-fact-sheet/view",
    "North Macedonia": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/north-macedonia-waste-prevention-fact-sheet/view",
    "Norway": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/norway-waste-prevention-fact-sheet/view",
    "Poland": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/poland-waste-prevention-fact-sheet/view",
    "Portugal": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/portugal-waste-prevention-fact-sheet/view",
    "Romania": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/romania-waste-prevention-fact-sheet/view",
    "Serbia": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/serbia-waste-prevention-fact-sheet/view",
    "Slovakia": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/slovakia-waste-prevention-fact-sheet/view",
    "Slovenia": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/slovenia-waste-prevention-fact-sheet/view",
    "Spain": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/spain-waste-prevention-fact-sheet/view",
    "Sweden": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/sweden-waste-prevention-country-fact-sheet/view",
    "Turkey": "#",
    "United Kingdom": "https://www.eea.europa.eu/themes/waste/waste-prevention/countries/uk-scotland-waste-prevention-fact-sheet/view"
}

df["Report"] = df["Country"].replace(COUNTRIES_DICT)
df["Report"] = df.apply(lambda row: "<a href='%s'>%s</a>" % (
    row['Report'], row['Country']), axis=1)
df['Values'] = df['Value'].apply(lambda x: "%.2fM" % (int(x)/10e5))

dff = df.copy().query('TIME == 2016')


CONF = {"autosizable": False, "displayModeBar": False, "doubleClickDelay": 1000,
        "fillFrame": False, "showTips": False, "showAxisDragHandles": False,
        "scrollZoom": False, "responsive": True}

# #############################################################################
# Map + table
fig = make_subplots(rows=2, cols=1, shared_xaxes=False,
                    vertical_spacing=0, row_heights=[0.3, 0.7],
                    specs=[[{"type": "choropleth"}], [{"type": "table"}]],
                    shared_yaxes=False)
fig.add_trace(
    go.Choropleth(colorscale='BuGn', locationmode='country names',
                  locations=dff['Country'], marker_line_color='gray',
                  marker_opacity=0.75, marker_line_width=0.5, showscale=False,
                  z=dff['Value'], hoverinfo='z+location'
                  ), row=1, col=1
)
dfp = df.query('TIME==2016')[['Report', 'Values']]
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
    dfp = df.query('TIME==@year')[['Report', 'Values']]

    buttons.append(
        dict(method='update', label=str(year),
             args=[{"z": [df.query('TIME == @year')['Value']],
                    "cells": dict(values=[dfp[k].tolist() for k in dfp.columns])
                    }])
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
                  paper_bgcolor="#F0F0F0", height=1800)


fig.show(config=CONF)

fig.write_html("C:\\Users\\ismae\\Documents\\GitHub\\dataseeds.github.io\\pages\\waste-graph.html",
               config=CONF)
