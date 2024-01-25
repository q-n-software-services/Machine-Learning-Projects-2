import pandas as pd
from pandas_profiling import ProfileReport
df = pd.read_csv("housing.csv")

profile = ProfileReport(df, '''minimal=True #if you want concise and less information''')
profile.to_file(output_file="housing.html")


