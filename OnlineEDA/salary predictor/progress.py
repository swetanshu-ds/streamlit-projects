import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time

plt.style.use("ggplot")

data = {
    "num":[i for i in range(1,11)],
    "square":[i**2 for i in range(1,11)],
    "twice":[i*2 for i in range(1,11)],
    "thrice":[i*3 for i in range(1,11)]
}

rad = st.sidebar.radio("Navigation",["Home","About us"])

if rad=="Home":

            df=pd.DataFrame(data = data)

            col=st.sidebar.multiselect("select a pizza",df.columns)

            plt.plot(df['num'],df[col])

            st.pyplot()

if rad == "About us":
    progress=st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        progress.progress(i+1)
    st.balloons()



    st.write("you got it")
    st.error("Error")
    st.success("Show success")
    st.info("Information")
    st.exception(RuntimeError("this is an error"))
    st.warning("this is a warn")

