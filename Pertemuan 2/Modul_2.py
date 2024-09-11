
"""
Created on Tue Sep 10 12:28:01 2024

@author: maulanabry
"""
#A. Load Data dan Library 
# a. Melakukan Import library
import pandas as pd
from pandas.plotting import scatter_matrix  # Update import statement
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 100)
pd.set_option('display.notebook_repr_html', True)

# b. Melakukan Import Data yang dibutuhkan
data = pd.read_csv('D:\\Storage\\Work\\Kuliah\\KULIAH\\SEMESTER 7\\Data Mining\\Praktikum Data Mining\\Tugas\\Praktikum_Data_Mining_2024\\Pertemuan 2\\Eps2-Data-train.csv')

# c. Mengecek isi data
print(data.head())
print("\n")

#B. Dokumentasi Tipe Data 
data = pd.DataFrame(data)
print (data.shape)
print("\n")

print (data.dtypes)
print("\n")

print (data['Age'].dtypes)
print("\n")

#C. Exploratory Data Analysis (EDA)
#1. Statistik sederhana
# Tugas 1: Terjemahkan hasil dari fungsi describe yang baru saja anda lakukan. 
print(data.describe())

print("\n")

#2. Pendekatan Visual
#- Distribusi data pada suatu variable/atribut 
data['Survived'].value_counts().plot(kind='bar')
print(data['Survived'].value_counts())

print("\n")

#- Perbandingan antar variable/atribut
def survival_stacked_bar(variable):
    died = data[data['Survived']==0][variable].value_counts()/len(data[data['Survived']==0])
    survived = data[data['Survived']==1][variable].value_counts()/len(data[data['Survived']==1])
    dataset = pd.DataFrame([died,survived],index=['Meninggal','Selamat'])
    dataset.plot(kind='bar',stacked=True,title='Prosentase')
    return dataset.head()

print(survival_stacked_bar('Sex'))
