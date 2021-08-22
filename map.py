import json
import plotly.express as px
import pandas as pd
import pickle
import random
import wikipedia


with open("gz_2010_us_040_00_5m.json") as file:
    states = json.load(file)

database = pickle.load(open("database.pickle", "rb"))
# database is organized like
# {STATE: [CATEGORY, ORDER, FAMILY, SCIENTIFIC NAME, COMMON NAME]}
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

#print(data)
# database is currently organized as
# {locations: states, nums: density (of endangered animals)}
data["text"] = []
for i, state in enumerate(database):
    if i == 0:
        continue
    print(i, state)
    r = random.randrange(len(database[state]))
    randomInfo = database[state][r]
    intro = "Name: " + randomInfo[4] + "\nScientific Name: " + randomInfo[3] + "\nType: " + randomInfo[0] + "\nOrder: " + randomInfo[1] + "\nFamily: " + randomInfo[2] + "\nStatus: " + randomInfo[5] + "\n\n"
    out = wikipedia.search(randomInfo[3])
    while len(out) < 4 or len(randomInfo[3]) == 1 or randomInfo[3] == "Canis lupus":
        r = random.randrange(len(database[state]))
        randomInfo = database[state][r]
        intro = "Name: " + randomInfo[4] + "\nScientific Name: " + randomInfo[3] + "\nType: " + randomInfo[0] + "\nOrder: " + randomInfo[1] + "\nFamily: " + randomInfo[2] + "\nStatus: " + randomInfo[5] + "\n\n"
        out = wikipedia.search(randomInfo[3])
    print(out, randomInfo[3])
    intro += wikipedia.summary(randomInfo[3], sentences=4, auto_suggest=False)
    print("found")
    data["text"].append(intro)

# use the wikipedia module (https://stackoverflow.com/questions/4460921/extract-the-first-paragraph-from-a-wikipedia-article-python)

print("text", len(data["text"]))
print("locations", len(data["locations"]))
print("nums", len(data["nums"]))
df = pd.DataFrame(data)
print(df)

fig = px.choropleth(df, geojson=states, locations='locations', locationmode="USA-states", color='nums',
    color_continuous_scale="tealrose",
    range_color=(0, 15),
    hover_name='locations',
    hover_data = ['text'],
    scope="usa",
    labels={'unemp':'unemployment rate'},
    title=""               
    )
fig.update_traces(marker_line_width=0, marker_opacity=0.8)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.update_geos(
showsubunits=True, subunitcolor="black"
)
fig.show()