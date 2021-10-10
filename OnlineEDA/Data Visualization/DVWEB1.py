import PyPDF2
import pandas as pd
import streamlit as st
import docx2txt
from PyPDF2 import PdfFileReader
#import pdfplumber
st.title("Upload your files")

menu = ["Home","DataSet","DocumentsFiles","About"]
choice = st.sidebar.selectbox("Menu",menu)
if choice == "Home":
    st.subheader("Home")

    image_file = st.file_uploader("Upload Images",type = ["img","png","jpg","jpeg"])

    if image_file is not None:
        ##  to see details
        st.write(type(image_file))
        ## Methods/Attributes
        ## st.write(dir(image_file))
        file_details = {"filename":image_file.name,"filetype":image_file.type,"filesize":image_file.size}
        st.write(file_details)
        st.image(image_file)


elif choice == "DataSet":
    st.subheader("DataSet")
    data_file =st.file_uploader("Upload CSV",type = ["csv"])
    if data_file is not None:
        st.write(type(data_file))
        file_details = {"filename": data_file.name, "filetype": data_file.type, "filesize": data_file.size}
        st.write(file_details)
        df = pd.read_csv((data_file))
        st.dataframe(df)

elif choice == "DocumentsFiles":
    st.subheader("DocumentsFiles")
    docx_file = st.file_uploader("Upload docx",type = ['pdf','docx','txt'])
    if st.button("See Details"):
        if docx_file is not None:
            file_details = {"filename": docx_file.name, "filetype": docx_file.type, "filesize": docx_file.size}
            st.write(file_details)
            if docx_file.type == "text/plain":
                # text=docx_file.read()
                # st.write(text)  ### works but gives bytes also

                text = str(docx_file.read(),"utf-8")
                st.write(text)

            elif docx_file.type == "application/pdf":
            ### try:
            ###    with pdfplumber.open(docx_file) as pdf:
            ###        pages = pdf.pages[4]
            ###        st.write(pages.extract_text())
            ### except:
            ###     st.write("None")
            ###  using PyPDF2

              pdfreader = PdfFileReader(docx_file)
              count = pdfreader.numPages
              all_text = ""
              for i in range(count):
                  page = pdfreader.getPage(i)
                  all_text =   all_text+page.extractText()

              st.write(all_text)





            else:
                text = docx2txt.process(docx_file)
                st.write(text)
                #st.text(text)


else:
    st.subheader("About")
    st.write("Web App for seeing the contents of any specified data type file")
    st.header("Thankyou")
    st.header("see you again")





