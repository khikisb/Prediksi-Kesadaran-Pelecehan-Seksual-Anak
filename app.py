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
    #Predicting
    if q1 == 'Agree':
        q1 = 1
    elif q1 == 'Disagree':
        q1 = 0
    
    if q2 == 'Agree':
        q2 = 1
    elif q2 == 'Disagree':
        q2 = 0
    
    if q3 == 'Agree':
        q3 = 1
    elif q3 == 'Disagree':
        q3 = 0
        
    if q4 == 'Agree':
        q4 = 1
    elif q4 == 'Disagree':
        q4 = 0
        
    if q5 == 'Yes':
        q5 = 1
    elif q5 == 'No':
        q5 = 0    
        
    if q6 == 'Yes':
        q6 = 1
    elif q6 == 'No':
        q6 = 0
        
    if q7 == 'Yes':
        q7 = 1
    elif q7 == 'No':
        q7 = 0 
        
    if q8 == 'Yes':
        q8 = 1
    elif q8 == 'No':
        q8 = 0
        
    prediction = model.predict(pd.DataFrame([[q1,q2,q3,q4,q5,q6,q7,q8]], columns=["Children are safe among family members such as grandparents, uncles, aunts, cousins", "Children are mainly abused by strangers in our society", "Male children dont need sexual abuse prevention knowledge", "Teaching sexual abuse prevention in school is not necessary. It will make children curious about sex", "Do you know what child grooming is?", "Do you know what signs to look for to identify if your child has been abused?", "Do you think children need post abuse counseling for recovering?", "Do you think you should take legal action against the abuser of your child?"]))
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
