import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("ggplot")

data = {
    "num":[i for i in range(1,11)],
    "square":[i**2 for i in range(1,11)],
    "twice":[i*2 for i in range(1,11)],
    "thrice":[i*3 for i in range(1,11)]
}



df=pd.DataFrame(data = data)

col=st.sidebar.selectbox("select a pizza",df.columns)

plt.plot(df['num'],df[col])

st.pyplot()


col=st.sidebar.multiselect("select a pizza",df.columns)

plt.plot(df['num'],df[col])

st.pyplot()

rad = st.sidebar.radio("Navigation",["Home","About us"])

if rad=="Home":

    df = pd.DataFrame(data=data)

    col = st.sidebar.multiselect("select a pizza", df.columns)

    plt.plot(df['num'],df[col])

    st.pyplot()

if rad == "About us":
    st.write("You got it")