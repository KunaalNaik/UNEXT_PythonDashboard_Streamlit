# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 22:06:07 2023

@author: DELL
"""
import streamlit as st #web app 
import pandas as pd # data manipulation
#import matplotlib.pyplot as plt
#import seaborn as sns

st.set_page_config(layout="wide")
#pd.options.plotting.backend = "plotly"

st.title("Enrollee Job Change EDA")
st.subheader("using Python and Streamlit 🚀 📈")

## Side Bar
st.sidebar.text('')
st.sidebar.text('')
st.sidebar.text('')
### Side Bar Title
st.sidebar.markdown("**Side Bar** 👇")


## Main Dashboard

### Read Data
df = pd.read_csv('case1.csv')

#### Get Metrics
enrollee_count = df.shape[0]
change_sum = df['change'].sum()
change_percentage = change_sum/enrollee_count
has_rel_exp = df[df['relevent_experience'] == 'Has Rel Exp']['change'].sum()


## Define KPI Cards
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

## Display KPI Cards
kpi1.metric(label = "Count of Enrollees",
            value = '{:,}'.format(enrollee_count))

kpi2.metric(label = "Job Changes",
            value = '{:,}'.format(change_sum))

kpi3.metric(label = "Change %",
            value = "{0:.2%}".format(change_percentage) )

kpi4.metric(label = "Rel Exp Job Change",
            value = "{:,}".format(has_rel_exp) )


## Categorical Features - Summarise and Display
st.markdown("### Categorical Features 📈")

chart1, chart2, chart3, chart4 = st.columns(4)

chart1.bar_chart(df['gender'].value_counts())
chart2.bar_chart(df['relevent_experience'].value_counts())
chart3.bar_chart(df['enrolled_university'].value_counts())
chart4.bar_chart(df['education_level'].value_counts())

#st.dataframe(df)