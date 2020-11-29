

import pandas as pd
df = pd.read_csv("Resources/cities.csv", index_col=0)
df.to_html("cities_table")
