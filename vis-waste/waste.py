

import numpy as np
import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)


df = pd.read_csv("waste_gen-data.csv")
df = df.drop(columns=["Flag and Footnotes", "NACE_R2", "NACE_R2_LABEL"])
df['Value'] = df['Value'].str.replace(' ', '').replace(':', '0')

# df['Value'] = df['Value'].astype(np.int64)

dfg = df.groupby(['TIME', 'GEO', 'UNIT', 'WASTE'])
print(df[:5])
df.reset_index(inplace=True)

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Waste", style={'text-align': 'center'}),
    
    html.Div([
        dcc.Dropdown(id="select_year",
                     options=[{"label": str(year), "value": year} for year in df['TIME'].unique()],
                     multi=False,
                     value=2016,
                     style={'width': "30%", 'display': 'inline-block'}),
        dcc.Dropdown(id="select_waste",
                 options=[{"label": str(waste), "value": waste} for waste in df['WASTE_LABEL'].unique()],
                 multi=False,
                 value="Total waste",
                 style={'width': "70%", 'display': 'inline-block'})  
    ]),
    
    html.Br(),

    dcc.Graph(id='waste_map', figure={}, style={"width": "100%", "height": "100%"})
])


# Connect the Plotly graphs with Dash Components
@app.callback(
    [
        # Output(component_id='output_container', component_property='children'),
        Output(component_id='waste_map', component_property='figure')
    ],
    [
        Input(component_id='select_year', component_property='value'),
        Input(component_id='select_waste', component_property='value')
    ]
)

def update_graph(selected_year, selected_waste):
    dff = df.copy()
    dff = dff[dff["TIME"] == selected_year]
    dff = dff[dff["HAZARD"] == "HAZ_NHAZ"]
    dff = dff[dff["WASTE_LABEL"] == selected_waste]
    dff = dff.query('GEO != ["EU27_2020", "EU28"]')

    # Plotly Express
    fig = px.choropleth(
        color='Value',
        color_continuous_scale="Reds",
        data_frame=dff,
        hover_data=['Value'],
        locationmode='country names', # "ISO-3" "country names" "geojson-id"
        locations='GEO_LABEL',
        labels={"WASTE": "WASTE"},
        scope="europe"
    )
    fig.update_traces(showlegend=False)
    fig.update_layout(autosize=True)
    fig.write_html("testt.html")


    # template='plotly_dark'

    # Plotly Graph Objects (GO)
    fig = go.Figure(
    data=[
        go.Choropleth(
            locationmode='country names',
            locations=dff['GEO_LABEL'],
            z=dff['Value'].astype(float),
            colorscale='Reds',
            marker_line_color='gray',
        )
    ])
    fig.update_layout(
        height=700,
        title_text = '2011 US Agriculture Exports by State',
        title_xanchor="center",
        title_x=0.5,
        title_font=dict(size=24),
        geo=dict(
            scope='europe'
        ),
        margin={"r": 0, "t": 50, "l": 0, "b": 0}
    )

    return [fig]


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=False, host="0.0.0.0")