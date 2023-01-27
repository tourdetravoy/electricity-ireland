from datetime import datetime

import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# Sidebar
# return_value = st.sidebar.selectbox(
   # 'Electricity generated each year',
   #  ['Total','Wind','Gas', 'Coal', 'Others'])

# Load electricity dataset
df1 = pd.read_csv("electricity_ireland_data_2021.csv")

# Body
st.title('Electricity Generation In Ireland')

col1, col2, col3 = st.columns(3)
col1.metric("% Renewable Power 2022", "37.1 %", "3.7")
col2.metric("% Fossil Fuel 2022", "60.2 %", "0.5")
col3.metric("% Others 2022", "2.7 %", "-3.0")

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

col1, col2, col3, col4 = st.columns(4)
col1.metric("Wind 2019", "9,968 GWh", "15.9 %")
col2.metric("Wind 2020", "11,495 GWh", "15.3 %")
col3.metric("Wind 2021", "9,887 GWh", "-12.0 %")
col4.metric("Wind 2022", "11,224 GWh", "13.5 %")

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

col1, col2, col3, col4 = st.columns(4)
col1.metric("Natural Gas 2019", "14,814 GWh", "-0.4 %")
col2.metric("Natural Gas 2020", "15,063 GWh", "1.7 %")
col3.metric("Natural Gas 2021", "13,993 GWh", "-7.1 %")
col4.metric("Natural Gas 2022", "15,435 GWh", "11.1 %")

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
col4.metric("Total Generation 2022", "32.105 GWh", "3.2 %")

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

col1, col2, col3 = st.columns(3)
col1.metric("Total Power from Renewables 2022", "11,924 GWh", "3.7 %")
col2.metric("Total Power from Fossil Fuels 2022", "19,326 GWh", "3.8 %")
col3.metric("Total Power Generated in Ireland 2022", "32,105 GWh", "2.7 %")

normal_chart = alt.Chart(df1).mark_area().encode(
x='Year:O',
y=alt.Y('GWh:Q', stack="normalize"),
color='Type:N',
tooltip=['Year', 'Type', 'GWh'],).interactive().properties(
    width=800,
    height=500
)
st.altair_chart(normal_chart)

st.title('Electricity Ireland 2010 - 2022')

chart = alt.Chart(df1).mark_bar().encode(
x=alt.X('sum(GWh)', stack="zero"),
y='Year:O',
color=alt.Color('Type'),
tooltip=['Year', 'Type', 'GWh'],).interactive().properties(
    width=800,
    height=500
)
st.altair_chart(chart)

df_ff = df1[(df1['Type']=='Gas')&(df1['Type']=='Coal')&(df1['Type']=='Oil')]

bar_chart_ff = alt.Chart(df_ff).mark_bar().encode(
x=alt.X('Year:O'),
y=alt.Y('GWh:Q', stack='zero'),
tooltip=['Year', 'GWh'],).properties(
    width=700,
    height=500
).interactive()
st.altair_chart(bar_chart_ff)
