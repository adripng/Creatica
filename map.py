import json
import plotly.express as px
import plotly.graph_objects as go
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
        data["density"] = []
    else:
        data["locations"].append(state)
        data["density"].append(len(database[state]) / total * 100)

#print(data)
# database is currently organized as
# {locations: states, density: density (of endangered animals)}
data["text"] = []
for i, state in enumerate(database):
    if i == 0:
        continue
    print(i, state)
    r = random.randrange(len(database[state]))
    randomInfo = database[state][r]
    intro = "Name: " + randomInfo[4] + "<br>Scientific Name: " + randomInfo[3] + "<br>Type: " + randomInfo[0] + "<br>Order: " + randomInfo[1] + "<br>Family: " + randomInfo[2] + "<br>Status: " + randomInfo[5] + "<br><br>"
    out = wikipedia.search(randomInfo[3])
    while len(out) < 4 or len(randomInfo[3]) == 1 or randomInfo[3] == "Canis lupus":
        r = random.randrange(len(database[state]))
        randomInfo = database[state][r]
        intro = "Name: " + randomInfo[4] + "<br>Scientific Name: " + randomInfo[3] + "<br>Type: " + randomInfo[0] + "<br>Order: " + randomInfo[1] + "<br>Family: " + randomInfo[2] + "<br>Status: " + randomInfo[5] + "<br><br>"
        out = wikipedia.search(randomInfo[3])
    #print(out, randomInfo[3])
    try: 
        summary = wikipedia.summary(randomInfo[3], sentences=4, auto_suggest=False)
        print("found")
        words = summary.split(" ")
        print(words)
        n = 20 # chunk length
        chunks = [words[i:i+n] for i in range(0, len(words), n)]
        joined = [" ".join(chunk) for chunk in chunks]
        summary = "<br>".join(joined)
        print(summary)
        intro += summary
    except: 
        intro += "No information was found on Wikipedia for this species."
    data["text"].append(intro)

# use the wikipedia module (https://stackoverflow.com/questions/4460921/extract-the-first-paragraph-from-a-wikipedia-article-python)
# for i, state in enumerate(database):
#     if i == 0:
#         continue
#     str = "hey how are you doing today i'm doing good what about you yeah i'm doing fine"
#     words = str.split(" ")
#     n = 4
#     chunks = [words[i:i+n] for i in range(0, len(words), n)]
#     joined = [" ".join(chunk) for chunk in chunks]
#     summary = "<br>".join(joined)
#     print(summary)
#     data["text"].append(summary)

print("text", len(data["text"]))
print("locations", len(data["locations"]))
print("density", len(data["density"]))
df = pd.DataFrame(data)
print(df)

fig = px.choropleth(df, geojson=states, locations='locations', locationmode="USA-states", color='density',
    color_continuous_scale="tealrose",
    range_color=(0, 15),
    hover_name='locations',
    hover_data=['text'],
    custom_data=['locations', 'text'],
    scope="usa",
    #title="Threatened or Endangered Species in National Parks Across the US"               
    )
fig.update_traces(marker_line_width=0,
    hovertemplate="<br>".join([
        '<b>%{customdata[0]}</b>',
        '%{customdata[1]}'
    ]),
    marker_opacity=0.8)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.update_geos(
showsubunits=True, subunitcolor="black"
)
fig.write_html("map.html")
fig.show()