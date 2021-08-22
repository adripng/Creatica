import json
import plotly.express as px
import pandas as pd
import pickle

with open("gz_2010_us_040_00_5m.json") as file:
    states = json.load(file)

database = pickle.load(open("database.pickle", "rb"))
total = 0
for state in database:
    total += len(database[state])

data = {}
for state in database:
    total += len(database[state])
    if "locations" not in data:
        data["locations"] = []
        data["nums"] = []
    else:
        data["locations"].append(state)
        data["nums"].append(len(database[state]) / total * 100)
print(data)

data["text"] = []

df = pd.DataFrame(data)
# df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
#     dtype={"fips": str})
print(df)

fig = px.choropleth(df, geojson=states, locations='locations', locationmode="USA-states", color='nums',
    color_continuous_scale="tealrose",
    range_color=(0, 15),
    hover_name='locations',
    hover_data = 'text',
    scope="usa",
    labels={'unemp':'unemployment rate'},                 
    )
fig.update_traces(marker_line_width=0, marker_opacity=0.8)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.update_geos(
showsubunits=True, subunitcolor="black"
)
fig.show()