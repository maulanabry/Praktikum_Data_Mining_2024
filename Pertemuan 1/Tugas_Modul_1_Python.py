# 2. Lakukan perintah python sederhana pada IDE yang anda gunakan untuk menampilkan nama 
# dan NPM anda seperti berikut: 
# NPM   : [NPM ANDA] 
# Nama   : [NAMA ANDA] 

# A. Mendefinisikan variabel untuk NPM dan Nama
npm = 21082010038
nama = "Maulana Bryan Syahputra"

# B. Memanggil variabel NPM dan Nama 
print(f"NPM   : {npm}")
print(f"Nama  : {nama}")


print(f"\n")

# 3. Lakukan perintah python sederhana untuk melakukan operasi matematika sederhana. Jika 
# anda akan membeli produk X dengan harga produk X adalah Rp 500.000,00 , maka: 
# a. Jika produk diberikan diskon 35%, maka berapa total yang perlu dibayarkan? 
# b. Jika harga produk X belum ditambah pajak dan besar pajak sebesar 15%, maka berapa 
# total yang perlu dibayarkan?  

#Langkah 0. Mendefinisikan harga awal produk x pada variabel harga_Produk
harga_Produk = 500000.00

#a. Menghitung produk jika diberikan diskon 35%
#Langkah 1. Membuat variabel diskon untuk menyimpan nilai diskon
diskon = 35/100 #Merubah diskon menjadi decimal

#Langkah 2. Menghitung total harga,  mengurangi harga dengan diskon
total_Harga1 = harga_Produk * (1-diskon)

#Langkah 3. Menampilkan harga setelah diskon
print(f"Total yang perlu dibayarkan setelah diskon 35%: Rp {total_Harga1:,.2f}")

#b. Menghitung total harga produk jika ditambahkan pajak sebesar 15%
#Langkah 4. Membuat variabel pajak untuk menyimpan nilai pajak
pajak = 15/100 #Merubah pajak menjadi decimal

#Langkah 5. Menghitung total harga dari diskon,  menambah harga dengan pajak
total_Harga2 = total_Harga1 * (1+pajak)

#Langkah 6. Menampilkan harga setelah pajak
print(f"Total yang perlu dibayarkan setelah pajak 15%: Rp {total_Harga2:,.2f}")
