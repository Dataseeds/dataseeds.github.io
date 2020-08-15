
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

pd.set_option("display.max_columns", 40)
pd.set_option("display.max_colwidth", 200)

df = pd.read_csv("C:\\Users\\ismae\\Documents\\GitHub\\dataseeds.github.io\\visualizations\\waste\\waste_gen-data.csv")

df = df.drop(columns=["Flag and Footnotes", "NACE_R2", "NACE_R2_LABEL"])
df = df.query('GEO != ["EU27_2020", "EU28"]')
df['Value'] = df['Value'].str.replace(' ', '').replace(':', '0')

df = df.query('HAZARD == "HAZ_NHAZ"')
df = df.query('WASTE_LABEL == "Total waste"')

dfg = df.groupby(['TIME', 'GEO', 'UNIT', 'WASTE'])
df.reset_index(inplace=True)

dff = df.copy().query('TIME == 2016')



# Plotly Graph Objects (GO)
fig = go.Figure(
    data=[
        go.Choropleth(
            colorscale='Greens',
            locationmode='country names',
            locations=dff['GEO_LABEL'],
            marker_line_color='gray',
            marker_opacity=0.75,
            marker_line_width=0.5,
            z=dff['Value'],
        )
    ],
    layout=dict(
        autosize=True,
        geo=dict(
            scope='europe',
            bgcolor="#F0F0F0",
            projection_scale=1.2,
            center=dict(lat=60, lon=15)
        ),
        height=400,
        margin={"r": 0, "t": 20, "l": 0, "b": 0, "pad": 0, "autoexpand": True},
        paper_bgcolor = "#F0F0F0",
        width=500,
    )
)

button_2004 = dict(method= 'update', label='2004',
               args=[{"z": [df.query('TIME == 2004')['Value']]}])
button_2006 = dict(method= 'update', label='2006',
               args=[{"z": [df.query('TIME == 2006')['Value']]}])
button_2008 = dict(method= 'update', label='2008',
               args=[{"z": [df.query('TIME == 2008')['Value']]}])
button_2010 = dict(method= 'update', label='2010',
               args=[{"z": [df.query('TIME == 2010')['Value']]}])
button_2012 = dict(method= 'update', label='2012',
               args=[{"z": [df.query('TIME == 2012')['Value']]}])
button_2014 = dict(method= 'update', label='2014',
               args=[{"z": [df.query('TIME == 2014')['Value']]}])
button_2016 = dict(method= 'update', label='2016', 
               args=[{"z": [df.query('TIME == 2016')['Value']]}])
buttons = [button_2004, button_2006, button_2008, button_2010, button_2012, button_2014, button_2016]
fig.update_layout(updatemenus=[dict(active=3,
                                    buttons=buttons,
                                    bgcolor="#FFFFFF",
                                    direction="down",
                                    pad={"r": 0, "t": 0, "l": 0, "b": 0},
                                    x=0.1,
                                    xanchor="left",
                                    yanchor="top"
                                    )]);
conf = {"autosizable": False,
        "fillFrame": False,
        "displayModeBar": False,
        "showTips": False,
        "showAxisDragHandles": False,
        "scrollZoom": False,
        "responsive": True,
        "doubleClickDelay": 1000}
fig.show(config=conf)


fig.write_html("C:\\Users\\ismae\\Documents\\GitHub\\dataseeds.github.io\\waste-graph.html",
               config=conf)
