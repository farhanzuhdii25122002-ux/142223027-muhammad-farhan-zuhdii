
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dashboard Analisis Data Produksi")

# Load data
df = pd.read_csv("anime_dataset.csv")

st.subheader("Data")
st.dataframe(df)

# Statistik
st.subheader("Statistik")
st.write(df.describe())

# Grafik Produksi
st.subheader("Grafik Produksi")
fig, ax = plt.subplots()
ax.plot(df[df.columns[0]], df[df.columns[1]])
st.pyplot(fig)

# Grafik Cacat
if len(df.columns) > 2:
    st.subheader("Grafik Cacat")
    fig2, ax2 = plt.subplots()
    ax2.plot(df[df.columns[0]], df[df.columns[2]])
    st.pyplot(fig2)
