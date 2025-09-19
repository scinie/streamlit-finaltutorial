import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as pt
import seaborn as sns

st.title ("Captain America!")

df = pd.DataFrame({"A": [1,2,3,4],  "B": [5,6,7,8]})

st.write ("st.write:")
st.write(df)

st.write ("st.table:")
st.table(df)

st.write ("st.dataframe:")
st.dataframe(df)

chart_data = pd.DataFrame(np.random.randn(20,3), columns = ['a', 'b', 'c'])

st.write("Line chart")
st.line_chart(chart_data)

st.write("Area chart")
st.area_chart(chart_data)

st.write("Bar chart")
st.bar_chart(chart_data)

map_data = pd.DataFrame (np.random.randn(1000,2)/[50,50] + [52, 13], columns = ["lat", "lon"])
st.map(map_data)

x = st.slider('x')
st.write(x, 'square is', x*x)

x = np.linspace(0, np.pi *2, 100)
t = st.slider("t", 0.0, 10.0, 1.0)
x0 = st.slider("x0", 0.0, np.pi*2, 0.0)
y = np.sin(x*t+x0)

st.line_chart(pd.DataFrame({"x":x, "y":y}))

function_name = st.selectbox("Function",["sin", "cos", "tan"])
function_dict = {"sin":np.sin, "cos":np.cos, "tan": np.tan}




with tabs
col1, col2 = st.columns (2)

with col1:
    with st.expander("Function settings"):
        st.write("This is a sidebar")
        x = np.linspace(0, np.pi *2, 100)
        t = st.slider("t", 0.0, 10.0, 1.0)
        x0 = st.slider("x0", 0.0, np.pi*2, 0.0)
        y = np.sin(x*t+x0)

        function_name = st.selectbox("Function",["sin", "cos", "tan"])
        function_dict = {"sin":np.sin, "cos":np.cos, "tan": np.tan}

with col2:
    if st.checkbox("Show line chart"): 
        y = function_dict[function_name](x*t+x0)
        st.line_chart (pd.DataFrame({f"{function_name}(x*t+x0)":y},))
