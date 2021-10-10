import streamlit as st
import pandas as pd
import numpy as np
a=[1,2,3,4,5,6,7,8]
n=np.array(a)
nd=n.reshape((2,4))
data=pd.read_csv("Ads_CTR_Optimisation.csv")
print(data)
st.dataframe(n)
st.dataframe(nd)
st.dataframe(data)
st.json(data)


st.title("Hello PyCharm")
st.header("type your name")
st.text_input(" ")

