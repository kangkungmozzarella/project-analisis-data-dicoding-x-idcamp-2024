import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul Dashboard
st.title("Bike Sharing Dashboard - Interaktif")

# Membaca data
day_df = pd.read_csv("data/day.csv")
day_df['dteday'] = pd.to_datetime(day_df['dteday'])  # Convert to datetime

# Menampilkan dataset
st.write("Data Bike Sharing:")
st.write(day_df.head())

# Menambahkan Filter Rentang Tanggal
st.sidebar.header("Filter Data")
start_date = st.sidebar.date_input('Start date', day_df['dteday'].min())
end_date = st.sidebar.date_input('End date', day_df['dteday'].max())

# Filter berdasarkan tanggal
filtered_df = day_df[(day_df['dteday'] >= pd.to_datetime(start_date)) & (day_df['dteday'] <= pd.to_datetime(end_date))]

# Filter Suhu
temp_range = st.sidebar.slider('Temperature Range (Normalized)', 0.0, 1.0, (0.1, 0.9))
filtered_df = filtered_df[(filtered_df['temp'] >= temp_range[0]) & (filtered_df['temp'] <= temp_range[1])]

# Filter Kelembaban
humidity_range = st.sidebar.slider('Humidity Range (Normalized)', 0.0, 1.0, (0.1, 0.9))
filtered_df = filtered_df[(filtered_df['hum'] >= humidity_range[0]) & (filtered_df['hum'] <= humidity_range[1])]

# Menampilkan hasil filter
st.subheader(f"Data dari {start_date} hingga {end_date}")
st.write(filtered_df.head())

# Visualisasi Total Rentals vs Temperature dengan Filter
st.subheader('Total Rentals vs Temperature (dengan filter)')
fig, ax = plt.subplots()
sns.scatterplot(x=filtered_df['temp'], y=filtered_df['cnt'], ax=ax)
ax.set_title('Total Rentals vs Temperature')
ax.set_xlabel('Temperature (Normalized)')
ax.set_ylabel('Total Rentals')
st.pyplot(fig)

# Visualisasi Total Rentals vs Humidity dengan Filter
st.subheader('Total Rentals vs Humidity (dengan filter)')
fig, ax = plt.subplots()
sns.scatterplot(x=filtered_df['hum'], y=filtered_df['cnt'], ax=ax)
ax.set_title('Total Rentals vs Humidity')
ax.set_xlabel('Humidity (Normalized)')
ax.set_ylabel('Total Rentals')
st.pyplot(fig)

# Histogram untuk Suhu
st.subheader('Distribution of Temperature (Histogram)')
fig, ax = plt.subplots()
sns.histplot(filtered_df['temp'], bins=20, kde=True, ax=ax)
ax.set_title('Distribution of Temperature')
ax.set_xlabel('Temperature (Normalized)')
st.pyplot(fig)

# Histogram untuk Kelembaban
st.subheader('Distribution of Humidity (Histogram)')
fig, ax = plt.subplots()
sns.histplot(filtered_df['hum'], bins=20, kde=True, ax=ax)
ax.set_title('Distribution of Humidity')
ax.set_xlabel('Humidity (Normalized)')
st.pyplot(fig)

# Visualisasi Total Rentals Berdasarkan Hari Kerja vs Libur
st.subheader('Total Rentals on Working Days vs Holidays')
fig, ax = plt.subplots()
sns.boxplot(x='workingday', y='cnt', data=filtered_df, ax=ax)
ax.set_title('Total Rentals on Working Days vs Holidays')
ax.set_xlabel('Working Day (0 = Holiday, 1 = Working Day)')
ax.set_ylabel('Total Rentals')
st.pyplot(fig)
