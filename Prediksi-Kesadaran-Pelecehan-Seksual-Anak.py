import pandas as pd
import pickle
import streamlit as st

# load the model from disk
model = pickle.load(open('model_file.pkl', 'rb'))

# Define the prediction function
def predict(q1, q2, q3, q4, q5, q6, q7, q8):
    #Predicting
    if q1 == 'Setuju':
        q1 = 1
    elif q1 == 'Tidak Setuju':
        q1 = 0
    
    if q2 == 'Setuju':
        q2 = 1
    elif q2 == 'Tidak Setuju':
        q2 = 0
    
    if q3 == 'Setuju':
        q3 = 1
    elif q3 == 'Tidak Setuju':
        q3 = 0
        
    if q4 == 'Setuju':
        q4 = 1
    elif q4 == 'Tidak Setuju':
        q4 = 0
        
    if q5 == 'Iya Tahu':
        q5 = 1
    elif q5 == 'Tidak Tahu':
        q5 = 0    
        
    if q6 == 'Iya Tahu':
        q6 = 1
    elif q6 == 'Tidak Tahu':
        q6 = 0
        
    if q7 == 'Iya Perlu':
        q7 = 1
    elif q7 == 'Tidak Perlu':
        q7 = 0 
        
    if q8 == 'Iya Tentu':
        q8 = 1
    elif q8 == 'Tidak':
        q8 = 0
        
    prediction = model.predict(pd.DataFrame([[q1,q2,q3,q4,q5,q6,q7,q8]], columns = ['"Children are safe among family members such as grandparents, uncles, aunts, cousins"',
       '"Children are mainly abused by strangers in our society"',
       'Male children dont need sexual abuse prevention knowledge',
       '"Teaching sexual abuse prevention in school is not necessary. It will make children curious about sex"',
       'Do you know what child grooming is?',
       'Do you know what signs to look for to identify if your child has been abused?',
       'Do you think children need post abuse counseling for recovering?',
       'Do you think you should take legal action against the abuser of your child?']))
    return prediction

st.set_page_config(
    page_title="Prediksi Kesadaran Pelecehan Seksual Anak",
    page_icon="👋",
)

st.title("")
st.sidebar.success("Pilih Halaman Yang Ingin Anda Tuju.")


st.title("Prediksi Kesadaran Pelecehan Seksual Anak")

tab1, tab2, tab3, tab4 = st.tabs(["Deskripsi Data", "Tab Pre - Processing", "Tab Modeling", "Tab Implementasi"])

with tab1:
   st.image("TabDD1.png")

with tab2:
   st.image("TabPP1.png")
    
with tab3:
   st.image("TM1.png")
   st.image("TM2.png")

with tab4:
   st.image("TI1.png")
   st.image("TI2.png")
    
st.header('Jawablah Semua Pertanyaan Berikut :')

q1 = st.selectbox('Apakah anak-anak aman di antara anggota keluarga seperti kakek nenek, paman, bibi, sepupu', ['Setuju', 'Tidak Setuju'])
q2 = st.selectbox('Anak-anak paling sering dilecehkan oleh orang asing di masyarakat kita', ['Setuju', 'Tidak Setuju'])
q3 = st.selectbox('Anak laki-laki tidak membutuhkan pengetahuan pencegahan pelecehan seksual', ['Setuju', 'Tidak Setuju'])
q4 = st.selectbox('Mengajarkan pencegahan pelecehan seksual di sekolah tidak perlu. Itu akan membuat anak penasaran dengan seks', ['Setuju', 'Tidak Setuju'])
q5 = st.selectbox('Apakah anda tahu apa itu perawatan anak?', ['Iya Tahu', 'Tidak Tahu'])
q6 = st.selectbox('Tahukah anda tanda-tanda apa yang harus dicari untuk mengidentifikasi jika anak Anda telah dilecehkan', ['Iya Tahu', 'Tidak Tahu'])
q7 = st.selectbox('Apakah menurut Anda, anak-anak memerlukan konseling pasca-pelecehan untuk pulih?', ['Iya Perlu', 'Tidak Perlu'])
q8 = st.selectbox('Apakah menurut Anda, Anda harus mengambil tindakan hukum terhadap pelaku kekerasan terhadap anak Anda?', ['Iya Tentu', 'Tidak'])

if st.button('Prediksi'):
    prediksi = predict(q1, q2, q3, q4, q5, q6, q7, q8)
    st.success(f'Tingkat Kesadaran Pelecehan Seksual Terhadap Anak, yaitu {prediksi}')
