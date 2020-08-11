

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

    dcc.Dropdown(id="select_year",
                 options=[{"label": str(year), "value": year} for year in df['TIME'].unique()],
                 multi=False,
                 value=2016,
                 style={'width': "30%"}
                 ),
    dcc.Dropdown(id="select_waste",
                 options=[{"label": str(waste), "value": waste} for waste in df['WASTE_LABEL'].unique()],
                 multi=False,
                 value="Total waste",
                 style={'width': "60%"}
                 ),
    
    html.Br(),

    dcc.Graph(id='waste_map', figure={})
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

    # Plotly Express
    fig = px.choropleth(
        color_continuous_scale="Viridis",
        color='Value',
        data_frame=dff,
        hover_data=['Value'],
        locationmode='country names', # "ISO-3" "country names" "geojson-id"
        locations='GEO_LABEL',
        labels={"WASTE": "WASTE"},
        scope="europe"
    )
    fig.update_traces(showlegend=False)
    
    # template='plotly_dark'

    # Plotly Graph Objects (GO)
    # fig = go.Figure(
    #     data=[go.Choropleth(
    #         locationmode='USA-states',
    #         locations=dff['state_code'],
    #         z=dff["Pct of Colonies Impacted"].astype(float),
    #         colorscale='Reds',
    #     )]
    # )
    #
    # fig.update_layout(
    #     title_text="Bees Affected by Mites in the USA",
    #     title_xanchor="center",
    #     title_font=dict(size=24),
    #     title_x=0.5,
    #     geo=dict(scope='usa'),
    # )

    return fig


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)