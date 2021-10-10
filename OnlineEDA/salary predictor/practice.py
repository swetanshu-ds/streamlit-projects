import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from plotly import graph_objs as go

st.title("salary pred")

nav =  st.sidebar.radio("Navigation",['Home',"Prediction","Contribute"])
data = pd.read_csv("salaryData.csv")
print(data["YearsExperience"])


if nav=="Home":
    st.image("impact-on-take-home-salary.jpg")
    if st.checkbox("Show me the table"):
        st.table(data)
    graph = st.selectbox("what graph",["Inter","Non Inter"])

    if graph =="Inter":

        plt.scatter(data["YearsExperience"],data["Salary"])
        plt.ylim(0)
        plt.xlabel("Years of exper")
        plt.ylabel("Salary")
        plt.tight_layout()
        st.pyplot()

    if graph == "Non Inter":
         layout = go.Layout(
             xaxis = dict(range =[0,16]),
             yaxis = dict(range = [0,210000])
         )
         fig = go.Figure(data=go.Scatter(x=data["YearsExperience"], y=data["Salary"], mode="markers"))
         st.plotly_chart(fig)

if nav=="Prediction":
    st.write("Pred")


if nav=="Contribute":
    st.write("Contribute")