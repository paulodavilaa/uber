import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy import signal
import streamlit as st

df = pd.read_csv("C:\\Users\\saade\\OneDrive\\Documents\\A00829380\\AMPROJ\\final_df.csv")

hotel = st.sidebar.selectbox(
    'Seleccione un hotel.',
     df["name"].drop_duplicates())

df = df[df["name"] == hotel]
df["ratingf"] = signal.savgol_filter(df["rating"],101,7)
df.loc[df["ratingf"] > 5, "ratingf"] = 5
df.loc[df["ratingf"] < 0, "ratingf"] = 0
df["sentimentf"] = signal.savgol_filter(df["sentiment"],101,7)
df.loc[df["sentimentf"] > 1, "sentimentf"] = 1
df.loc[df["sentimentf"] < 0, "sentimentf"] = 0

# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])
# Add traces
fig.add_trace(
    go.Scatter(
        x=df["date"],
        y=df["ratingf"],
        name="rating"),
    secondary_y=False,
)
fig.add_trace(
    go.Scatter(
        x=df["date"],
        y=df["sentimentf"],
        name="sentiment"),
    secondary_y=True,
)
# Add figure title
fig.update_layout(
    title_text=hotel,
    template="simple_white",
    width=800,
    height=400
)
# Set x-axis title
fig.update_xaxes(
    title_text="Date",
    showgrid=True,
    fixedrange=True)
# Set y-axes titles
fig.update_yaxes(
    title_text="Rating",
    secondary_y=False,
    showgrid=True,
    range=[0,5],
    fixedrange=True)

fig.update_yaxes(
    title_text="Sentiment",
    secondary_y=True,
    showgrid=True,
    range=[0,1],
    fixedrange=True)




st.write(fig)
