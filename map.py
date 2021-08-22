import json
import plotly.express as px
import pandas as pd

with open(gz_2010_us_040_00_5m.json) as response:
    states = json.load(response)

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
    dtype={"fips": str})

fig = px.choropleth(df, geojson=states, locations='fips', color='unemp',
    color_continuous_scale="Viridis",
    range_color=(0, 12),
    scope="usa",
    labels={'unemp':'unemployment rate'},                 
    )
fig.update_traces(marker_line_width=0, marker_opacity=0.8)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.update_geos(
showsubunits=True, subunitcolor="black"
)
fig.show()