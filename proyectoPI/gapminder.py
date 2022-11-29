import plotly.express as px
import streamlit as st
import pandas as pd

df =px.data.gapminder()

st.write(df)

year_options = df['year'].unique().tolist()
year = st.selectbox('Which year would yo like to see? ', year_options, 0)
df = df[df['year']==year]

fig = px.scatter(df, x="gdpPercap", y="lifeExp", size="pop",
color= "continet", hover_name="continient", log_x="True", size_max=55, range_x=[100,100000], range_y=[25,50])

fig.update_layout(width=400)
st.write(fig)