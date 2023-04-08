import streamlit as st

st.title("Chimeía Grandprix")
st.subheader("Siap mengetes kemampuanmu dan menjadi yang terbaik?")
st.caption("pilih level mu")
tombol_1= st.button ("easy")
if tombol_1:
    option= st.selectbox(
        "pilih salah satu",
        ("kimia dasar","analisis jenis","kimia organik"))
            
tombol_2= st.button ("medium")
if tombol_2:
    option= st.selectbox(
        "pilih salah satu",
        ("kimia dasar","analisis jenis","kimia organik"))
            
tombol_3= st.button("hard")
if tombol_3:
    option= st.selectbox(
        "pilih salah satu",
        ("kimia dasar","analisis jenis","kimia organik"))