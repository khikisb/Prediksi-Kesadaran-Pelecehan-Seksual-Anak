import pandas as pd
import numpy as np
import seaborn as sns
import pickle
import streamlit as st
import matplotlib.pyplot as plt

# load the model from disk
model = pickle.load(open('model_file.pkl', 'rb'))

# Define the prediction function
def predict(q1, q2, q3, q4, q5, q6, q7, q8):
    #Predicting the price of the carat
    if q1 == 'Agree':
        q1 = 1
    elif q1 == 'Disagree':
        q1 = 0
    
    prediction = model.predict(pd.DataFrame([[q1]], columns=["Children are safe among family members such as grandparents, uncles, aunts, cousins"]))
    return prediction

st.set_page_config(
    page_title="Prediksi Kesadaran Pelecehan Seksual Anak",
    page_icon="👋",
)

st.title("")
st.sidebar.success("Pilih Halaman Yang Ingin Anda Tuju.")


st.title("Prediksi Kesadaran Pelecehan Seksual Anak")
st.header('Jawablah Semua Pertanyaan Berikut :')

q1 = st.selectbox('"Apakah anak-anak aman di antara anggota keluarga seperti kakek nenek, paman, bibi, sepupu"', ['Aggree', 'Disagree'])
q2 = st.selectbox('"'"Anak-anak terutama dilecehkan oleh orang asing di masyarakat kita"'"', ['Aggree', 'Disagree'])
q3 = st.selectbox('Anak laki-laki tidak membutuhkan pengetahuan pencegahan pelecehan seksual', ['Aggree', 'Disagree'])
q4 = st.selectbox('"Mengajarkan pencegahan pelecehan seksual di sekolah tidak perlu. Itu akan membuat anak penasaran dengan seks"', ['Aggree', 'Disagree'])
q5 = st.selectbox('"Apakah kamu tahu apa itu perawatan anak?"', ['Yes', 'No'])
q6 = st.selectbox('"Tahukah Anda tanda-tanda apa yang harus dicari untuk mengidentifikasi jika anak Anda telah dilecehkan?"', ['Yes', 'No'])
q7 = st.selectbox('Apakah menurut Anda anak-anak memerlukan konseling pasca-pelecehan untuk pulih?', ['Yes', 'No'])
q8 = st.selectbox('"Apakah menurut Anda Anda harus mengambil tindakan hukum terhadap pelaku kekerasan terhadap anak Anda?"', ['Yes', 'No'])

if st.button('Prediksi'):
    prediksi = predict(q1, q2, q3, q4, q5, q6, q7, q8)
    st.success(f'Kamu Memiliki Kesadaran {prediksi}')
