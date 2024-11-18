menu = {
    1: ("Nasi goreng", 25000),
    2: ("Nasi Jagung", 15000),
    3: ("Mie ayam", 10000),
    4: ("French fries", 5000),
    5: ("Jasmine tea", 4000),
}

print("======== Daftar Menu ========")
for key, value in menu.items():
    print(f"{key}. {value[0]} \t Harga: {value[1]}")
print("Pembelian di atas Rp100.000,- mendapatkan diskon 15%")
print("====================================================")

# Input pilihan menu berdasarkan angka
pilih = int(input("Pilih menu (1-5): "))
if pilih not in menu:
    print("Menu tidak valid!")
else:
    jumlah = int(input("Jumlah pesanan: "))
    nama_menu, harga = menu[pilih]
    bayar = jumlah * harga

    # Perhitungan diskon jika pembelian lebih dari Rp100.000
    if bayar > 100000:
        diskon = bayar * 15 / 100
        total = bayar - diskon
    else:
        total = bayar

    print("================= Detail Pembayaran =================")
    print("Menu yang dipesan        : ", nama_menu)
    print("Jumlah yang dipesan      : ", jumlah)
    print("Total Biaya              : ", bayar)
    print("Total yang harus dibayar : ", total)
