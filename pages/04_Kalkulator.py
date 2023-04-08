import streamlit as st

st.title("Chemiskulator")
st.subheader("Kalkulator buat kamu yang suka kimia")
st.caption("Apa yang mau kamu hitung hari ini?")
tab_1, tab_2, tab_3, tab_4, tab_5 = st.tabs(["BM atau MR","Molaritas", "% Kadar", "Normalitas", "PPM"])
with tab_1:
    st.header("Blom ada isi")
    
with tab_2:
    option = st.selectbox(
        "Pilih salah satu",
        ("Diketahui Mol zat terlarut & Volume","Diketahui massa, MR, & volume"))
    if option == "Diketahui Mol zat terlarut & Volume":
        Mol = st.number_input("Masukkan nilai mol terlarut")
        Volume = st.number_input("Masukkan jumlah volume larutan (mL)")
        tombol_1 = st.button("Hitung")
        if tombol_1:
            nilai_molaritas1 = Mol/Volume
            st.success(f"nilai molaritas adalah {nilai_molaritas1}")
    if option =="Diketahui massa, Mr, & volume":
        Massa = st.number_input("Masukkan nilai massa terlarut (gram)")
        Mr = st.number_input("Masukkan nilai Mr terlarut (gram/mol)")
        volume = st.number_input("Masukkan jumlah volume larutan (mL)")
        tombol_2 = st.button("Yuk Hitung")
        if tombol_2:
            nilai_molaritas2 = Massa*1000/(Mr*volume)
            st.success(f"nilai molaritas adalah {nilai_molaritas2}")
        
with tab_3:
    option = st.selectbox(
        "Pilih salah satu",
        ("% Kadar (v/v)","% Kadar (b/v)","% Kadar (b/b)"))
    
with tab_4:
    option = st.selectbox(
        "Pilih salah satu",
        ("Diketahui molaritas & valensi","Diketahui massa, BE,& volume larutan", "Diketahui massa,Mr,& volume larutan"))
    if option == "Diketahui molaritas & valensi":
        Molaritas = st.number_input("Masukkan nilai molaritas")
        Valensi = st.number_input("Masukkan nilai valensi")
        tombol_1 = st.button("Ayo Hitung")
        if tombol_1:
            nilai_normalitas1 = Molaritas*Valensi
            st.success(f"nilai normalitas adalah {nilai_normalitas1}")
    if option == "Diketahui massa, BE,& volume larutan":
        Massa1 = st.number_input("Masukkan nilai massa (gram)")
        BE = st.number_input("Masukkan nilai BE")
        volume1 = st.number_input("Masukkan nilai volume larutan (liter)")
        tombol_2 = st.button("Ayo Hitung")
        if tombol_2:
            nilai_normalitas2 = Massa1/(BE*volume1)
            st.success(f"nilai normalitas adalah {nilai_normalitas2}")
    if option == "Diketahui massa,Mr,& volume larutan":
        Massa2 = st.number_input("Masukkan nilai massa (mg)")
        Mr = st.number_input("Masukkan nilai Mr")
        volume2 = st.number_input("Masukkan nilai volume larutan (mL)")
        tombol_3 = st.button("Ayo Hitung")
        if tombol_3:
            nilai_normalitas3 = Massa2*1000/(Mr*volume2)
            st.success(f"nilai normalitas adalah {nilai_normalitas3}")
with tab_5:
    st.title("Belum ada isi")
