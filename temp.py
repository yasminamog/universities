# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import streamlit as st
st.title("Showing diff uk universities")

import pandas as pd
import plotly.express as px
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder

df = pd.read_excel("uk_universities.xlsx")



if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df.head(40))
    
st.header("This is AgGrid Table")
gd = GridOptionsBuilder.from_dataframe(df)
gd.configure_pagination(enabled=True)
gd.configure_default_column(editable=True,groupable=True)
sel_mode = st.radio('Selection Type', options = ['Single'])
gd.configure_selection(selection_mode=sel_mode,use_checkbox=True)
gridoptions = gd.build()
grid_table = AgGrid(df,gridOptions=gridoptions)
sel_row = grid_table["selected_rows"]
st.write(sel_row)




st.header('The World Ranking of Different Universties at UK')
fig=px.bar(df, x='University_name', y='World_rank')
st.plotly_chart(fig)




st.header("Student Satisfaction Across Different Universities at UK")
fig1=px.box(df, y='Student_satisfaction')
st.plotly_chart(fig1)

st.header("CWUR Score and UG Average Fees Across 50 Universities at UK")
fig2=px.scatter(df.head(50), x='CWUR_score', y='UG_average_fees_(in_pounds)', color='University_name')
st.plotly_chart(fig2)


st.header("PG Average Fees Across 10 Universities at UK")
fig3=px.histogram(df.head(10), x="University_name", y="PG_average_fees_(in_pounds)", color="University_name")
st.plotly_chart(fig3)

option = st.selectbox(
    'Which University you think its overpriced?',
    ('Imperial College London', 'London School of Economics and Political Science', 'University of Warwick'))

st.write('You selected:', option)


st.header("The number of Enrolled Students")
fig4=px.histogram(df.head(10), x="Student_enrollment")
st.plotly_chart(fig4)



