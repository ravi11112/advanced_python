import streamlit as st
import seaborn as sns
import pandas as pd 

#to run the streamlit just use the below command
#streamlit run c:/Users/Admin/steafmlit/main.py
#c:/Users/Admin/steafmlit/main.py  not this ...........

#now add title and subheader in this 
st.title("data science")
st.subheader("learning the data science with streamlit.")

#upload a file from local device and read the data 
upload=st.file_uploader("upload a file ")
if upload is not None :
    data=pd.read_csv(upload)


#now read the data from head and tail method 
if upload is not None:
  if  st.checkbox("preview the file"):
         if st.button("head"):
             st.write(data.head())
         if st.button("tail"):
             st.write(data.tail())


#now lets see the dublicates and remove this 

if upload is not None:
    data1=st.radio("know the colomn and rows",("rows","colomns"))
    #this data1 only for radio
    if data1=="rows":
      st.text("no of rows")
      st.write(data.shape[0])
      #in above csv file select rows by 0
    if data1=="colomns":
      st.text("no of colomn")
      st.write(data.shape[1])
      #in above csv file select colomn by 1


if upload is not None:
    if st.checkbox("the data type of colomn"):
        st.text("dtypes are")      
        st.write(data.dtypes)
    if st.checkbox("describe the dataset"):
        st.write(data.describe())
        st.text("whole data are")
        st.write(data)
    if st.checkbox("drop the dublicates"):
        st.write(data.drop_duplicates,inplace=True)
