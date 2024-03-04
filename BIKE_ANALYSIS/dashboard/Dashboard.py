import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Atur gaya menjadi 'dark' untuk seaborn
sns.set(style='dark')

# Baca dataset
day_df = pd.read_csv("https://raw.githubusercontent.com/R4ffaell/Bike-Sharing-Dataset/main/day.csv")
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Konfigurasi halaman Streamlit
st.set_page_config(page_title="Capital Bikeshare: Dasbor Penyewaan Sepeda",
                   page_icon="bar_chart:",
                   layout="wide")

# HEADER
st.header('Dasbord Penyewaan Sepeda 🚲')

# SIDEBAR
with st.sidebar:
    st.title(' Dasbord Penyewaan Sepeda 🚲')
    st.markdown('***oleh Anakta Raffaell Tambunan***')
    st.markdown('### Galeri Foto Sepeda')
    st.image('https://surabaya.go.id/uploads/pictures/2022/5/66629/original_IMG_0300.jpg?1652597239', width=150)
    st.image('https://upload.wikimedia.org/wikipedia/commons/6/6f/Alexander_Vinokourov%2C_Olympic_Road_Race_London_-_July_2012.jpg', width=150)
    st.image('https://radarkukar.com/wp-content/uploads/2022/12/WhatsApp-Image-2022-12-18-at-18.03.42.jpeg', width=150)
    st.image('https://akcdn.detik.net.id/community/media/visual/2019/11/10/8ba7d8fa-9aa9-4473-ae0a-db61f389a942_43.jpeg?w=250&q=', width=150)
    st.image('https://radarkukar.com/wp-content/uploads/2022/12/WhatsApp-Image-2022-12-18-at-18.03.42.jpeg', width=150)



# Tampilkan contoh data yang disediakan
st.write("Data yang disediakan:")
st.write(day_df)


# Pemetaan musim
season_mapping = {1: 'Musim Semi', 2: 'Musim Panas', 3: 'Musim Gugur', 4: 'Musim Dingin'}
season_rentals = day_df.groupby('season')['cnt'].sum().reset_index()
season_rentals['season'] = season_rentals['season'].map(season_mapping)

# Tampilkan peminjaman musiman
st.write("Total Peminjaman Tiap Musiman:")
st.write(season_rentals)

# Plot jumlah peminjaman berdasarkan musim
plt.figure(figsize=(3, 2))
sns.barplot(data=season_rentals, x='season', y='cnt', palette='viridis')
plt.title('Jumlah Peminjaman Berdasarkan Musim')
plt.xlabel('Musim')
plt.ylabel('Jumlah Peminjaman')
plt.xticks(rotation=45)
season_rentals_plot = plt.gcf()

# Pertanyaan 2: Apa hubungan antara suhu dan jumlah peminjaman?
temp_rentals = day_df.groupby('temp')['cnt'].mean().reset_index()

# Plot hubungan antara suhu dan jumlah peminjaman menggunakan plot batang
plt.figure(figsize=(3, 2))  # Ukuran plot lebih kecil
sns.barplot(data=temp_rentals, x='temp', y='cnt', color='blue')
plt.title('Hubungan antara Suhu dan Jumlah Peminjaman')
plt.xlabel('Suhu (Celsius)')
plt.ylabel('Rata-Rata Jumlah Peminjaman')
plt.xticks(rotation=45)
temp_rentals_plot = plt.gcf()

# Tampilkan plot menggunakan st.pyplot() dengan objek gambar eksplisit
st.write("Jumlah Peminjaman berdasarkan Musim:")
st.pyplot(season_rentals_plot)

# Subjudul untuk kesimpulan
st.subheader("Kesimpulan")
st.write("Berdasarkan data di gambar, dapat ditarik kesimpulan bahwa musim dengan jumlah sewa paling tinggi adalah musim gugur, baik dari hari holiday maupun weekday. Dalam konteks peminjaman sepeda, musim gugur mungkin memiliki cuaca yang lebih nyaman bagi pengguna sepeda, serta adanya perayaan atau acara yang mendorong meningkatnya permintaan penyewaan sepeda. Selain itu, kemungkinan adanya pemandangan alam yang menarik pada musim gugur juga dapat menjadi faktor penentu dalam meningkatnya jumlah penyewaan sepeda. Pengguna sepeda mungkin lebih cenderung untuk menjelajahi daerah tertentu saat cuaca masih nyaman namun pemandangan alam sedang mencapai puncak keindahannya pada musim gugur.")


# Jeda space untuk memisahkan antara kesimpulan dengan bagian pertanyaan nomor dua
st.write("\n\n")
st.write("\n\n")
st.write("\n\n")
st.write("\n\n")

# Tampilkan plot menggunakan st.pyplot() dengan objek gambar eksplisit
st.write("Hubungan antara Suhu dan Jumlah Peminjaman:")

# Urutkan day_df berdasarkan 'mnth.name'
day_df_sorted = day_df.sort_values(by='mnth')

# Plot cnt dan temp sebagai plot terpisah
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(6, 6))  # Ukuran plot lebih kecil

# Plot jumlah peminjaman (cnt)
axes[0].bar(day_df_sorted['mnth'], day_df_sorted['cnt'], color='blue')
axes[0].set_title('Jumlah Peminjaman')
axes[0].set_xlabel('Bulan')
axes[0].set_ylabel('Jumlah')
axes[0].tick_params(axis='x', rotation=45)

# Plot suhu rata-rata (temp) dengan batang
axes[1].bar(day_df_sorted['mnth'], day_df_sorted['temp'], color='red')
axes[1].set_title('Suhu Rata-Rata')
axes[1].set_xlabel('Bulan')
axes[1].set_ylabel('Suhu')
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()

# Tampilkan plot menggunakan st.pyplot() dengan objek gambar eksplisit
st.pyplot(fig)

#subheader
st.subheader("Kesimpulan")
st.write("Berdasarkan gambar diatas, dapat dilihat bahwa jumlah temperatur dan juga jumlah penyewa adalah sebanding, yang artinya semakin temperatur naik maka jumlah penyewa juga meningkat, tetapi ini tidak terjadi 100% yang dimana terdapat bulan yang dimana temperatur meningkat tapi jumlah penyewa tidak meningkat. Namun demikian, perlu diingat bahwa korelasi antara temperatur dan jumlah penyewa sepeda tidak selalu bersifat langsung dan linier. Ada berbagai faktor lain yang juga mempengaruhi minat orang untuk menyewa sepeda, seperti kondisi lalu lintas, promosi atau diskon yang ditawarkan oleh penyedia layanan, serta preferensi pribadi.")