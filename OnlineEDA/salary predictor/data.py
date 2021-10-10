import streamlit as st
import pandas as pd
import numpy as np
import time


a=[1,2,3,4,5,6,7,8]
n=np.array(a)
nd = n.reshape((2,4))
dic={
    "name":["Raj"],
     "age":[20],
     "District":["Azamgarh"]
}

data =  pd.read_csv("Ads_CTR_Optimisation.csv")
print(data)
st.dataframe(n)
st.dataframe(a)
st.dataframe(nd)
st.dataframe(dic)
st.dataframe(data)
st.dataframe(data,width=500,height=1000)

st.json(dic)
st.write(dic)
st.write(a)

@st.cache
def ret_time(a):
    time.sleep(5)
    return time.time()
if st.checkbox("1"):
    st.write(ret_time(1))

if st.checkbox("2"):
    st.write((ret_time(2 )))
