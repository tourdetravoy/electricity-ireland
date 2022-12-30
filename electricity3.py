from datetime import datetime

import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# Sidebar
return_value = st.sidebar.selectbox(
    'Electricity generated each year',
     ['Total','Wind','Gas', 'Coal', 'Others'])

# Load financial dataset
df1 = pd.read_csv("electricity_ireland_data_2021.csv")

# Body
st.title('Electricity Generation In Ireland')

col1, col2, col3 = st.columns(3)
col1.metric("% Renewable Power 2021", "33.4 %", "-7.9")
col2.metric("% Fossil Fuel 2021", "59.7 %", "2.2")
col3.metric("% Others 2021", "6.9 %", "5.7")

bar_chart = alt.Chart(df1).mark_bar().encode(
x=alt.X('Year:O'),
y=alt.Y('GWh:Q', stack='zero'),
color=alt.Color('Type'),
tooltip=['Year', 'Type', 'GWh'],).properties(
    width=800,
    height=500
).interactive()
st.altair_chart(bar_chart)

st.title('Windpower Generation In Ireland')

col1, col2, col3 = st.columns(3)
col1.metric("Wind 2019", "9,968 GWh", "15.9 %")
col2.metric("Wind 2020", "11,495 GWh", "15.3 %")
col3.metric("Wind 2021", "9,667 GWh", "-15.9 %")

dfwind = df1[(df1['Type']=='Wind')]

bar_chart_wind = alt.Chart(dfwind).mark_bar().encode(
x=alt.X('Year:O'),
y=alt.Y('GWh:Q', stack='zero'),
tooltip=['Year', 'GWh'],).properties(
    width=700,
    height=500
).interactive()
st.altair_chart(bar_chart_wind)

st.title('Natural Gas Generation In Ireland')

col1, col2, col3 = st.columns(3)
col1.metric("Natural Gas 2019", "14,814 GWh", "-0.4 %")
col2.metric("Natural Gas 2020", "15,063 GWh", "1.7 %")
col3.metric("Natural Gas 2021", "13,993 GWh", "-7.1 %")

df_gas = df1[(df1['Type']=='Gas')]

bar_chart_gas = alt.Chart(df_gas).mark_bar().encode(
x=alt.X('Year:O'),
y=alt.Y('GWh:Q', stack='zero'),
tooltip=['Year', 'GWh'],).properties(
    width=700,
    height=500
).interactive()
st.altair_chart(bar_chart_gas)

st.title('Total Generation In Ireland')

col1, col2, col3 = st.columns(3)
col1.metric("Total Generation 2019", "29,649 GWh", "2.2 %")
col2.metric("Total Generation 2020", "30,053 GWh", "1.4 %")
col3.metric("Total Generation 2021", "31,178 GWh", "3.7 %")

area_chart = alt.Chart(df1).mark_area().encode(
x='Year:O',
y='GWh:Q',
color=alt.Color('Type:N'),
tooltip=['Year:O', 'Type', 'GWh'],).interactive().properties(
    width=800,
    height=500
)
st.altair_chart(area_chart)

st.title('Recent Generation In Ireland')

col1, col2, col3 = st.columns(3)
col1.metric("Total Power from Renewables 2021", "10,407 GWh", "-16.2 %")
col2.metric("Total Power from Fossil Fuels 2021", "18,614 GWh", "7.8 %")
col3.metric("Total Power Generated in Ireland 2021", "31,178 GWh", "3.7 %")

normal_chart = alt.Chart(df1).mark_area().encode(
x='Year:O',
y=alt.Y('GWh:Q', stack="normalize"),
color='Type:N',
tooltip=['Year', 'Type', 'GWh'],).interactive().properties(
    width=800,
    height=500
)
st.altair_chart(normal_chart)

st.title('Electricity Ireland 2010 - 2021')

chart = alt.Chart(df1).mark_bar().encode(
x=alt.X('sum(GWh)', stack="zero"),
y='Year:O',
color=alt.Color('Type'),
tooltip=['Year', 'Type', 'GWh'],).interactive().properties(
    width=800,
    height=500
)
st.altair_chart(chart)

df_ff = df1[(df1['Type']=='Gas')&(df1['Type']=='Coal')]

bar_chart_ff = alt.Chart(df_ff).mark_bar().encode(
x=alt.X('Year:O'),
y=alt.Y('GWh:Q', stack='zero'),
tooltip=['Year', 'GWh'],).properties(
    width=700,
    height=500
).interactive()
st.altair_chart(bar_chart_ff)
