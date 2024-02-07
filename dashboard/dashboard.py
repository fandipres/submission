import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import io

day_df = pd.read_csv("day.csv")

# Sidebar
with st.sidebar:
    st.image("https://dicoding-web-img.sgp1.cdn.digitaloceanspaces.com/small/avatar/dos:9f6d4b8c0e937d66e6f83570732bc19820221101111409.png")
    st.title('Fandi Presly Simamora')
    st.write('fandi.simamora@gmail.com')

# Main Content
st.header('Dicoding Collection Dashboard :sparkles:')
st.subheader('Recap Season')

plt.figure(figsize=(8, 6))
sns.barplot(data=day_df.loc[day_df['yr'] == 1], x='season', y='cnt', estimator=sum)
plt.xlabel('Musim')
plt.ylabel('Jumlah Pengguna Sepeda')
plt.title('Penggunaan Sepeda Berdasarkan Musim untuk Tahun 2012')

buffer = io.BytesIO()
plt.savefig(buffer, format='png')
plt.close()
buffer.seek(0)
st.image(buffer)

st.subheader('Rental Bike Trend')

plt.plot(day_df['dteday'], day_df['cnt'])
plt.xlabel('Tanggal')
plt.ylabel('Jumlah Pengguna Sepeda')
plt.title('Tren Penggunaan Sepeda')
plt.xticks(rotation=45)
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))
plt.tight_layout()

buffer = io.BytesIO()
plt.savefig(buffer, format='png')
plt.close()
buffer.seek(0)
st.image(buffer)