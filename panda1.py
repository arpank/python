import pandas as pd
import Quandl as qa

df = Quandl.get("WIKI/GOOGL")

print(df.head())