import streamlit as st
import pandas as pd


st.title (" Machine Learning Web App")

st.info ("This is a simple web app")

with st.expander("Data") :
    st.write ("This is the data we will be using in this web app")
    df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
    df
    
    st.write ("**X**")
    X = df.drop(columns=['species'])
    X
    st.write ("**y**")
    y = df['species']
    y
    
with st.expander("Data Visualization") :
    st.write ("This is the data visualization")
    st.scatter_chart(data= df , x = 'bill_length_mm' , y = 'body_mass_g' ,color= 'species')