import streamlit as st


st.set_page_config(
    page_title="Tentang Pengembang",
    page_icon="👋",
)

st.title("Halo Semuanya !👋")

st.write('Kamu Bisa menemukan Source Code Project ini')

tab1, tab2, tab3 = st.tabs(["Okhi Sahrul Barkah", "Farid Ghozali", "Afirza Lucky Pradana"])

with tab1:
   st.write("Belum Ada Foto")

with tab2:
   st.write("Belum Ada Foto")
    
with tab3:
   st.write("Belum Ada Foto")

link = '[Di GitHub](https://github.com/khikisb/Prediksi-Kesadaran-Pelecehan-Seksual-Anak)'
st.markdown(link, unsafe_allow_html=True)
