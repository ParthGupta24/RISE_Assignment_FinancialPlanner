import streamlit as st
import datetime
import pandas as pd
import numpy as np
import datagen

cats = ['Beginner', 'Amateur', 'Intermediate', 'Advanced']
conts = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Australia']
doms = ['Technology', 'Finance', 'Travel', 'Food', 'Sports']
costs = [1000, 1500, 2200, 3700]
vars = [50, 90, 176, 407]
bases = dict(zip(cats, costs))
devs = dict(zip(cats, vars))

st.set_page_config("Dashboard")

if st:
    st.success("Portal Successfully initiated...")
else:
    st.error("Portal didn't initiate due to some error. Please reload the page...")

st.title("Planner Dashboard")
desc = st.write('''
        ### Welcome to the Finance Dashboard and Investment Planner
        *You can visualize your finances using the Dashboard*\n
        *Please use the Planner platform to generate an appropriate investment plan for your requirements*
        ''')

sidebar = st.sidebar
datagener = sidebar.expander("Dataset generator")
scol1, scol2 = datagener.columns(2)
rows = scol1.slider("No. of Rows:", min_value=100, max_value=2000, value=500)
dataset_gen = scol2.button("Generate a mock dataset")
if dataset_gen:
    datagen.main(continents=conts, status=cats, categories=doms, amount_baselines=bases, amount_devs=devs, n=rows)
user_lvl = sidebar.radio("User Level", cats)
target = sidebar.selectbox("Target Continent", conts)
interests = sidebar.multiselect("Interests", doms)
budget = sidebar.slider("Investment Budget", 0, 10000)

start_date = st.date_input("Project Start Date", 'today')
activities = st.expander("View all activites")
df = pd.DataFrame(pd.read_csv('dataset.csv'), columns=['Category', 'Amount', 'Status', 'Continent'])
activities.dataframe(df)
col1, col2 = st.columns(2)
df_display = df.loc[df['Continent'] == target,:]
df_display = df_display.loc[df_display['Status'] == user_lvl,:]
ind = list()
for i in interests:
    ind.extend(list(np.where(df_display['Category'] == i)[0]))
    ind.sort()
df_display['Date'] = start_date
df_display = df_display.values[ind]
df_display = pd.DataFrame(df_display, columns=['Category', 'Amount', 'Status', 'Continent', 'Date'])
df_display = pd.DataFrame(df_display, columns=['Date', 'Category', 'Amount', 'Status'])

if len(interests) > 0:
    col1.dataframe(df_display)
    for i in interests:
        col2.write(i.capitalize())
        col2.line_chart(df_display.loc[df['Category']==i, :],y='Amount')

    button = st.button('Generate Report')
    if button:
        if budget == 0:
            st.write("The Investment Budget is zero. Please consider increasing it")
        else:
            st.markdown(f'''
                        ## Planner report\n\n
                        * Daily budget = {budget/30}\n
                        * Continent = {target}\n
                        * Domains : {interests}
                        ''')