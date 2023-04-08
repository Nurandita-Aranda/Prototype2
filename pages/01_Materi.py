import streamlit as st

st.title("Gaia Library")
st.subheader("Apa yang mau kamu pelajari hari ini?")
tab_1, tab_2, tab_3, tab_4, tab_5 = st.tabs(["Kimia Dasar","Analisis Jenis", "Titrimetri", "Kimia Organik", "Analisis Fisik"])
with tab_1:
    st.caption('Pilih materi yang kamu mau')
    tombol1 = st.button("Tabel Periodik")
    if tombol1:
        st.image("https://lh3.googleusercontent.com/7wwHLTc5-pYmcqKILkpztKuL6gOg1ncJ5O2c_PxrFzIF-K8rGygBfKtlj5oE3eXn_qcV0mPo0rxkYXRQBeB9XABXKXUgzjbIf0EqbGIL_KHqLB89Hm1HnM3MOB72LnagoIpWn1Hts-RFK-E89nQWECpFjKnL51qCbHTokFMzSKmF9_1F2ISVlLhzHWBu8DYQyBJo6X0-2BfSF7pgsQaXFBvCf-zttyPR9wJsz4u9oCRRmnYUphKXB8L66EwKI2Zivd_xgJuSK55amr4yNJOXK9P1ceXTx9cWNuwVH2TtBqMzWZp7l8r_SQGFqC1_j80lhkvb-Je9a_2ivmLPYge-I8np6eX8hYVhFvQZ5kW0Ly4EAyvnAZbmL50fSIhS2PvSW6c00AVD00QUxgGxl46WOUwGGtpO3uDGv8qsMDnQZ83UExPDaepq4--77E5bIX4zTPyxK3Md6YzfiFeLhrD2gE-rqmTIyjN1-bwcUB0rxlQLTLzJpbULpwhO004qcrTOn3U4x8uK4E8oCwutVAGiogxPvARfr64N4OqLXxtoNEhAXMaUn8ew5r6jx7-CgMRvwp2nfKmRR8XEk24t0kSzJvWP5HdoYJahQLqdeDgmI1OEvr_Zs0DkZqnHUwRzggJhPxl9mzEQie6tW9YL50oxmilGSmr2Aijcz8YHph-01xjfUPRxp_LFkPvpM1cyz3mzUM2xzh_fAlTm6jfBdmBuA89VrVBXk3gsaIXITqF8Kq7tLubPIOhE3G5On4JYz1DyYZNiU_l5zeCR3zLyTXn1_T1QGuDlOUsND8RsSFuxC22u7rtR92l8HE1EtcP84_uOJIO1S-sqwUhhrnRN0N5Z-Vk_rBOLF7Lu8TmTXw0A0kRUWnW9IGGbJnUxC-y-MSa8pRbBXEI-KQg39nJw8VIQG-CuieNSpdJ-CBc2riqC8iP1tLKWnA=w1539-h866-s-no?authuser=0",width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
        with col1:
            tombol_11 = st.button('Gol. I')
        with col2:
            tombol_12 = st.button('Gol. II')
        with col3:
            tombol_13 = st.button('Gol. III')
        with col4:
            tombol_14 = st.button('Gol. IV')
        with col5:
            tombol_15 = st.button('Gol. V')
        with col6:
            tombol_16 = st.button('Gol. VI')
        with col7:
            tombol_17 = st.button('Gol. VII')
        with col8:
            tombol_18 = st.button('Gol.VIII')
   
with tab_2:
    st.caption('Pilih materi yang kamu mau')
    tombol1 = st.button("Identifikasi zat dengan cara kering")
    tombol2 = st.button("Pembuatan Larutan")
    tombol3 = st.button("Identifikasi kation golongan I-V")
    tombol4 = st.button("Identifikasi Anion")
with tab_3:
    st.caption('Pilih materi yang kamu mau')
    tombol1 = st.button("Pemilihan Indikator")
    tombol2 = st.button("Titrasi asam basa")
    tombol3 = st.button("Titrasi Redoks")
with tab_4:
    st.caption('Pilih materi yang kamu mau')
    tombol1 = st.button("Pendahuluan")
    tombol2 = st.button("Alkana & Sikloalkana")
    tombol3 = st.button("Alkena & Siklodiena")
    tombol4 = st.button("Alkuna")
    tombol5 = st.button("Stereokimia")
    tombol6 = st.button("Senyawa Aromatik")
with tab_5:
    st.caption('Pilih materi yang kamu mau')
