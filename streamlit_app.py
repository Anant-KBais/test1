import streamlit as st

st.set_page_config(
   page_title="noogle",
   page_icon="🧊",
   layout="wide",
   initial_sidebar_state="expanded",
)
import pandas as pd
from streamlit_gsheets import GSheetsConnection
url = st.text_input("enter share link")
# url = "https://docs.google.com/spreadsheets/d/1JDy9md2VZPz4JbYtRPJLs81_3jUK47nx6GYQjgU8qNY/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url)
st.dataframe(data)
import numpy
st.write(data.describe(include='all'))
st.selectbox("Select chart type", ("area chart", "line chart", "bar chart", "scatter chart","map",))
st.selectbox("select X axis", (data.columns))
st.selectbox("select Y axis",(data.columns))
st.write(pd.__version__)
import pandas
import streamlit as st
st.write(pandas.__version__)
