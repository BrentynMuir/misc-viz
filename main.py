import pandas as pd
import streamlit as st
import plotly.express as px

xls = pd.ExcelFile('assets/example_data.xlsx')
ed_df = pd.read_excel(xls, 'Export Data')

st.title('Example Dashboard')
st.subheader('subheader')
st.dataframe(ed_df)
advesaries = ed_df['advesaryName'].drop_duplicates()
# adv_choice = st.sidebar.selectbox('Filter by adversary:', advesaries)

fig = px.scatter(
    ed_df,
    title="Main Table",
    width=500,
    height=500,
    x="investmentScore (x)",
    y="militaryScore (y)",
    size="confidenceScore (z)",
    color="advesaryName",
    range_x=[0, 100],
    range_y=[0, 100],
    hover_name="uniqueName"
)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Plotly theme.
    st.plotly_chart(fig, theme=None, use_container_width=True)
