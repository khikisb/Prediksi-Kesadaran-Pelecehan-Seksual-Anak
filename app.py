import pandas as pd
import numpy as np
import seaborn as sns
import pickle
import streamlit as st
import matplotlib.pyplot as plt

# load the model from disk
model = pickle.load(open('model_file.pkl', 'rb'))

# Define the prediction function
def predict(q1):
    #Predicting the price of the carat
    if q1 == 'Agree':
        q1 = 1
    elif q1 == 'Disagree':
        q1 = 0
    
    prediction = model.predict(pd.DataFrame([[q1]], columns=["Children are safe among family members such as grandparents, uncles, aunts, cousins"]))
    return prediction

st.set_page_config(
    page_title="Prediksi Harga Berlian",
    page_icon="👋",
)

st.title("")
st.sidebar.success("Pilih Halaman Yang Ingin Anda Tuju.")


st.title('Prediksi Harga Berlian')
st.image('')
st.header('Jawablah Semua Pertanyaan Berikut :')

q1 = st.selectbox('"Children are safe among family members such as grandparents, uncles, aunts, cousins"', ['Aggree', 'Disagree'])

if st.button('Prediksi Harga Belian'):
    price = predict(q1)
    st.success(f'Harga Berlian Tersebut adalah {price} USD')
