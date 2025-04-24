import streamlit as st

# Input User
berat_badan = st.number_input("Berat Badan (kg)", min_value=30.0, max_value=200.0, step=1.0)
usia = st.number_input("Usia", min_value=10, max_value=100, step=1)
jenis_kelamin = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
aktivitas = st.selectbox("Tingkat Aktivitas", ["Sedentari (minim aktivitas)","Aktif ringan (olahraga ringan 1-3x/minggu)", "Aktif sedang (olahraga sedang 3-5x/minggu)","Sangat aktif (olahraga berat tiap hari)"])

# Hitung kebutuhan protein
def hitung_protein(berat, aktivitas):
    faktor = {"Sedentari (minim aktivitas)": 0.8," Aktif ringan (olahraga ringan 1-3x/minggu)": 1.2,"Aktif sedang (olahraga sedang 3-5x/minggu)": 1.5,"Sangat aktif (olahraga berat tiap hari)": 2.0}
    return round(berat * faktor[aktivitas], 1)

if berat_badan:
    kebutuhan = hitung_protein(berat_badan, aktivitas)
    st.subheader("Kebutuhan protein harianmu: **{kebutuhan} gram**")

    # Visualisasi: Bar Chart
    labels = ['Protein dibutuhkan']
    values = [kebutuhan]

    fig, ax = plt.subplots()
    ax.bar(labels, values, color='skyblue')
    ax.set_ylabel('Gram')
    ax.set_title('Visualisasi Kebutuhan Protein Harian')
    st.pyplot(fig)


if usia <1:
    return"Data usia tidak tersedia dalam AKG"
elif 1 <= usia <= 8:
    return 19
elif 9 <= usia <= 13:
    return 34
elif 14 <= usia <= 18:
    if jenis_kelamin.lower() == 'perempuan':
        return 46
elif usia >= 19:
    if jenis_kelamin.lower() == 'perempuan':
        return 56
else:
    return"Usia tidak valid."
