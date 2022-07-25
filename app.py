import streamlit as st
from gsheetsdb import connect
import pandas as pd
import numpy as np
import altair as alt
import plotly.figure_factory as ff
import plotly.express as px


# Create a connection object.
conn = connect()

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
# @st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["public_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')



df = pd.DataFrame(rows)



####
# c = alt.Chart(df).mark_circle().encode(
#     x="j",
#     y="m",
#     size="l",
#     color="l",
#     tooltip=["j", "m", "l"])

# st.altair_chart(c, use_container_width=True)




#########
# t0 = df[df.j < 1000]
# t1 = df[(df.j >= 1000) & (df.j < 2500)]
# t2 = df[(df.j >= 2500) & (df.j < 5000)]
# t3 = df[(df.j >= 5000) & (df.j < 7500)]
# t4 = df[(df.j >= 7500) & (df.j < 10000)]
# t5 = df[df.j >= 10000]

# data = [t0.j,t1.j,t2.j,t3.j,t4.j,t5.j]
# group_labels = ['t0','t1','t2','t3','t4','t5']

# fig = ff.create_distplot(
#         data, 
#         group_labels,
#         bin_size=.2)


# st.plotly_chart(fig, use_container_width=True)




# fig = px.density_heatmap(df, x="j", y="i", nbinsx=50, nbinsy=50)


# st.plotly_chart(fig, use_container_width=True)



fig = px.scatter(
    df[df['supply'] > 20],
    x='price', y='supply',
    color="minted",
    size='total_stars',
    hover_data=['h'],
    width=1800,
    height=1400,
    log_x=True)


st.plotly_chart(fig, use_container_width=True)
