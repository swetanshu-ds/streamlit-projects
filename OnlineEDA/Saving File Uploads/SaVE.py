import streamlit as st

import  os
import pandas as pd
from PIL import Image
st.title("Upload and save to differnet location")

menu = ["Home","Dataset","About"]

choice=st.sidebar.selectbox("Menu",menu)

if choice =="Home":
    st.subheader("Upload Images")
    image_file = st.file_uploader("Upload an image",['img','jpg','jpeg'])
    if image_file is not None:
        file_details = {"FileName":image_file.name,"File_size":image_file.size,"File_type":image_file.type}
        st.write(file_details)
        st.image(image_file)
        with open(os.path.join("NewDir",image_file.name),"wb") as f:
            f.write(image_file.getbuffer())
        st.success("File Saved")


elif choice =="Dataset":
    st.subheader("Dataset")
    data_file = st.file_uploader("Upload Your File",["csv"])
    if data_file is not None:
        file_details = {"file_name":data_file.name,"file_type":data_file.type,"file_size":data_file.size}
        st.write(file_details)
        df = pd.read_csv(data_file)
        st.dataframe(df)
        with open(os.path.join("NewDir",data_file.name),"wb") as f:
            f.write(data_file.getbuffer())
        st.success("Saved :{} in NewDir".format(data_file.name))
else:
   st.write("Thankyou for seeing")