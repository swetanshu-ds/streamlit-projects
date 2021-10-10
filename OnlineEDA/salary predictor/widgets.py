import streamlit as st
st.title("Widgets")
if st.button("press me"):
    st.write("I am using pycharm")

name = st.text_input("Name")
st.write(name)

address = st.text_area("Enter your address")
st.write(address)

date =  st.date_input("enter a date")
st.write(date)

time=st.time_input("enter a time")
st.write(time)


if st.checkbox("you accept the pizza"):
    st.write("then eat it")


st.radio("Colors",["red","green","blue"],index = 0)

st.radio("pizza variety",["onion","garlic","pepporoni"],index = 1)

st.selectbox("Burgers",["cheese","italian ","mexican"],index = 0)


v1= st.multiselect("Colors",["red","green","blue"])
st.write(v1)

st.slider("height")

st.slider("height",min_value=-123,max_value=234)


st.slider("height",min_value=-123,max_value=234,value=200)


st.slider("height",min_value=-123,max_value=234,value=200,step=2)

st.number_input("numbers")

st.number_input("numbers",min_value=-123,max_value=234,value=200,step=2)

img = st.file_uploader("Upload a pdf file")

st.image(img)


