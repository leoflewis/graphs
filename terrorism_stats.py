import pandas as pd
import plotly.express as px
df = pd.read_csv('eu_terrorism_fatalities_by_year.csv')
fig = px.line(df, x ='iyear', y ='fatalities', title="EU Terrorism fatalities by year")
fig.show()
