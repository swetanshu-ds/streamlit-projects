import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

data1=pd.read_csv("Ads_CTR_Optimisation.csv")
st.line_chart(data1)
st.area_chart(data1)

print(data1)



data =pd.DataFrame(
    np.random.randn(100,3),
    columns=['a','b','c']
)

st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)
plt.scatter(data['a'],data['b'])
st.pyplot()
plt.title("scatter")
chart = alt.Chart(data).mark_circle().encode(
    x= "a",y="b",tooltip = ['a','b']
)
st.altair_chart(chart,use_container_width=True)
st.graphviz_chart("""
digraph{
watch ->me
me->  raj
raj-> watch
watch->me
}

""")


st.map()


st.image("udemy.jpg")

st.video("https://www.youtube.com/watch?v=7RUylQDHQMk&t=94s")

