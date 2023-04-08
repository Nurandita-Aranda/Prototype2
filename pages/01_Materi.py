import streamlit as st

st.title("Gaia Library")
st.subheader("Apa yang mau kamu pelajari hari ini?")
tab_1, tab_2, tab_3, tab_4, tab_5 = st.tabs(["Kimia Dasar","Analisis Jenis", "Titrimetri", "Kimia Organik", "Analisis Fisik"])
with tab_1:
    st.caption('Pilih materi yang kamu mau')
    tombol1 = st.button("Tabel Periodik")
    if tombol1:
        st.image("https://lh3.googleusercontent.com/e8HVbXWwyWvtPrM3GjrjjoLAlJKKCEv5DfWpwsX39TTnSj_zyoSDvL2S1o9slY4Kuq5BLeX2DS113df-UO1nRP_sknP9nvXF2i1tU9VElLoKulfZAsyMere2KWW2vB7G63lhIhHVsbx53XpB9VwMLKWl5ilmp3xZ_Uv_wFjpSd6Ir7cxMSn4wJc4pIDoc4hFV3F_kQEB3A4vjr6HonXsr-8CyvlqOc5mGqnvry3tk1czmIB5AooYBnyaROlLtby_IxNFzFN2esUERSyl0Iq82LNI-Li_v7GHae_K5GVsyqyVnwB_rYYEC9HgLRhk1FKtbaMnHgwHwaJ--fpcxtLTr-DYDNV2o_92jSJ1uNC0rA5_5dgnzk6UWBjdOQZ6fMBUuajjVIieU6nuDJgyqGpEaq_CfrHcf9uWTzWrn2gaCD9-dvOlpO0GGnz45Q4EsUReZcCawNsB9BKSf44CCK0SB537baDEtsts5gF17V7FYTg2M2tFKkqaDvmfL6mrRhZhGGMt5ddWzLfr7CaPDiWjJSgb_m6MS5SzJzaS2FT_j4VIVwp_lK2m4-uZGSX69Y3R00uDOndmiDyvHKyx0arQA2rgz86R0rStg54VFyGvVV2NndVx-2Ft-IfuDhmGUdjP-QVhqHgy54vWMuq2GbRFRnu3ZLwbnXCeDHHwdWkM_Xc5BZXVp-GbNnebp_nSZuKq8mzvGw0GJYdbbaLtkiK85CpKrCmrL6gyloHJ_2ob2UegUJzwY7mcXHOZaPhPRemDHopM7kYj1hHca3yA6YqSPdvmrIaa1xsj6IL6QyqFf4S8VY00UA-giVPHm0YWB3srVaKJKef6D_zfvNHqa0MJiQEWlV2wpcPZyVJTNzE1bqlHWOM0qPl7aqwg_D8DShngunWf4pMDb1Dj4NiE3byEzliFVwoNyw7CUuK-5hleos-4oQwxKQ=w1539-h866-s-no?authuser=0",width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
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