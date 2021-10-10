import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from  plotly import   graph_objs as go
from sklearn.linear_model import LinearRegression
import numpy as np




st.title("Salary Predictor")

nav = st.sidebar.radio("Navigation",["Home","Prediction","Contribute"])
data =pd.read_csv("salaryData.csv")
lr = LinearRegression()
x = np.array(data['YearsExperience']).reshape(-1,1)
lr.fit(x,np.array(data["Salary"]))


if nav=="Home":
    st.image("impact-on-take-home-salary.jpg",width=800)
    if st.checkbox("Show table"):
        st.table(data)

    graph=st.selectbox("What kind of Graph?",["Non-Interactive","Interactive"])
    val = st.slider("Filter by years",0,20)
    data = data.loc[data["YearsExperience"]>=val]
    if graph=="Non-Interactive":
        plt.figure(figsize=(10,5))
        plt.scatter(data["YearsExperience"],data["Salary"])
        plt.ylim(0)
        plt.xlabel("Years of Experience")
        plt.ylabel("Salary")
        plt.tight_layout()
        st.pyplot()



    if graph=="Interactive":
        layout = go.Layout(
            xaxis = dict(range = [0,16]),
            yaxis = dict(range = [0,210000])
        )
        fig = go.Figure(data = go.Scatter(x = data["YearsExperience"],y=data["Salary"],mode = "markers"))
        st.plotly_chart(fig)
if nav=="Prediction":
         st.header("Know your salary")
         val = st.number_input("Enter you Number",0.00,20.00,step=0.10)
         val = np.array(val).reshape(1,-1)
         pred = lr.predict(val)[0]


         if st.button("Predict"):
             st.success(f"your predicted salary is {round(pred)}")
if nav=="Contribute":
    st.header("Contribute to our dataset")
    ex = st.number_input("Enter your experience",0.0,20.0)
    sal = st.number_input("Enter your experience",0.0,100000.0,step=1000.0)

    if st.button("submit"):
        to_add =  {"YearsExperience":[ex],"Salary":[sal]}
        to_add = pd.DataFrame(to_add)
        to_add.to_csv("salaryData.csv",mode = 'a',header = False,index = False)
        st.success("Submitted")






