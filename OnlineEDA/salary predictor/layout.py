import streamlit as st

st.title("Registration form")

first,last = st.beta_columns(2)                     #### this function return containers objects

first.text_input("First Name")
last.text_input("last Name")

email,mobile= st.beta_columns([3,1])      #### list will distribute the block in the ratio  3 isto 1

email.text_input("Email Address")
mobile.text_input("Mobile")

user,pw,pw2 = st.beta_columns(3)

user.text_input("User Name")
pw.text_input("Password",type = "password")

pw2.text_input("Retype your password",type = "password")

ch, bl, sub = st.beta_columns(3)

ch.checkbox("I agree")

sub.button("Submit")

