import pprint

import pandas as pd
import json

df = pd.read_csv('../../data/visualisation_bases/places_pivot.csv', encoding='utf8', sep=',')
#df['year'] = df['year'].astype(str)
df = df.rename(columns={"Ausstellungsort": "place", "COUNTA von Ausstellungsort": "value"})
result = df.to_json(orient="records")
parsed = json.loads(result)
json_string = json.dumps(parsed, ensure_ascii=False)
with open('../../data/visualisation_bases/places_pivot.json', 'w') as f:
    f.write(json_string)