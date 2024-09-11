
"""
Created on Tue Sep 10 12:28:01 2024

@author: maulanabry
"""
#A. Load Data dan Library 
# a. Melakukan Import library
import pandas as pd
from pandas.plotting import scatter_matrix  # Update import statement
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 100)
pd.set_option('display.notebook_repr_html', True)

# b. Melakukan Import Data yang dibutuhkan
data = pd.read_csv('D:\\Storage\\Work\\Kuliah\\KULIAH\\SEMESTER 7\\Data Mining\\Praktikum Data Mining\\Tugas\\Praktikum_Data_Mining_2024\\Pertemuan 2\\Eps2-Data-train.csv')


#A. Persentase Passangers yang selamat berdasarkan Passangers Class
pclass_survival = data.groupby('Pclass')['Survived'].mean() * 100
pclass_survival_df = pclass_survival.reset_index()
pclass_survival_df.columns = ['Pclass', 'Survival Percentage']

# Grafik
plt.figure(figsize=(8, 5))
sns.barplot(x='Pclass', y='Survival Percentage', data=pclass_survival_df, palette='viridis')
plt.title('Persentase Passengers yang Survived berdasarkan Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Pesertase Keselamatan (%)')
plt.ylim(0, 100)
plt.show()

#B. Mengelopokkan jumlah passangers berdasarkan kisaran umur.
# Buat kategori umur (bins) dan label untuk kategori tersebut
bins = [0, 12, 18, 30, 50, 80]  # Rentang umur yang ingin dikelompokkan
labels = ['0-12', '13-18', '19-30', '31-50', '51-80']  # Label untuk rentang umur

# Tambahkan kolom 'AgeGroup' ke DataFrame
data['AgeGroup'] = pd.cut(data['Age'], bins=bins, labels=labels, right=False)

# Hitung jumlah passenger per rentang umur
age_group_counts = data['AgeGroup'].value_counts().sort_index()

# Grafik
plt.figure(figsize=(10, 6))
sns.barplot(x=age_group_counts.index, y=age_group_counts.values, palette='viridis')
plt.title('Jumlah Passengers Berdasarkan Kisaran Umur')
plt.xlabel('Kisaran Umur')
plt.ylabel('Jumlah Passengers')
plt.show()

#C. Jumlah passangers yang selamat berdasarkan titik keberangkatan
# Hitung jumlah passangers yang selamat berdasarkan titik keberangkatan
survival_by_embarked = data[data['Survived'] == 1]['Embarked'].value_counts()

# Grafik
plt.figure(figsize=(8, 5))
sns.barplot(x=survival_by_embarked.index, y=survival_by_embarked.values, palette='viridis')
plt.title('Jumlah passangers yang Selamat Berdasarkan Titik Keberangkatan')
plt.xlabel('Titik Keberangkatan')
plt.ylabel('Jumlah passangers yang Selamat')
plt.show()

#D. Distribusi gender passangers berdasarkan kelas passangers (Pclass)
# Hitung jumlah passenger berdasarkan gender dan kelas
gender_class_counts = data.groupby(['Pclass', 'Sex']).size().unstack()

# Plotting
plt.figure(figsize=(10, 6))
gender_class_counts.plot(kind='bar', stacked=True, colormap='viridis')
plt.title('Distribusi Gender passanger  Berdasarkan Passanger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Jumlah Penumpang')
plt.legend(title='Gender')
plt.xticks(rotation=0)
plt.show()

#E. Persentase keselamatan passanger berdasarkan titik keberangkatan
# Hitung persentase keselamatan berdasarkan titik keberangkatan
embarked_survival_rate = data.groupby('Embarked')['Survived'].mean() * 100

# Ubah menjadi DataFrame untuk keperluan plotting
embarked_survival_df = embarked_survival_rate.reset_index()
embarked_survival_df.columns = ['Embarked', 'Survival Percentage']

# Plotting
plt.figure(figsize=(8, 5))
sns.barplot(x='Embarked', y='Survival Percentage', data=embarked_survival_df, palette='viridis')
plt.title('Persentase Keselamatan passanger  Berdasarkan Titik Keberangkatan')
plt.xlabel('Titik Keberangkatan')
plt.ylabel('Persentase Keselamatan (%)')
plt.ylim(0, 100)
plt.show()

#Tugas 3
# Cek missing value sebelum penanganan
print("Missing values sebelum penanganan:")
print(data.isnull().sum())

# 1. Mengisi nilai Age yang hilang dengan mean
data['Age'].fillna(data['Age'].mean(), inplace=True)

# 2. Menghapus kolom Cabin karena banyak missing value
data.drop(columns=['Cabin'], inplace=True)

# 3. Mengisi nilai Embarked yang hilang dengan modus
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)

# Cek missing value setelah penanganan
print("\nMissing values setelah penanganan:")
print(data.isnull().sum())

