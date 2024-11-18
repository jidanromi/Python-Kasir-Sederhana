data_product = {
    1: "Laptop",
    2: "Mouse",
    3: "Monitor",
    4: "Kursi Gaming",
    5: "Headphone",
    6: "Charger"
}
daftar_harga = {
    1: 2000000,
    2: 100000,
    3: 5000000,
    4: 30000,
    5: 100000,
    6: 70000
}

dict_trx = {}

daftar_pembayaran = {
    1: "Transfer Bank",
    2: "Virtual Account",
    3: "Cash On Delivery",
    4: "Kartu Kredit"
}

print("======== List Product ========")
for i in data_product:
    print("Id Product : ", i, "\t Nama Product : ", 
          data_product[i], "\t \t Harga Product : ", daftar_harga[i])

# Pilih produk
pilih_id = int(input("Pilih ID Product : "))
if pilih_id in data_product:
    pilih_beli = input("Ingin Beli ? (Y/N): ")
    if pilih_beli.lower() == "y":
        nama_penerima = input("Nama Penerima       : ")
        alamat_penerima = input("Alamat Penerima     : ")
        nohp = input("No Hp               : ")
        kurir_pengiriman = input("Ekspedisi Pengiriman : ")
        dict_trx = {
            "nama penerima": nama_penerima,
            "alamat penerima": alamat_penerima,
            "no Hp": nohp,
            "kurir pengiriman": kurir_pengiriman,
            "product id": pilih_id
        }
    else:
        pass

    # Jika ada transaksi, lanjut ke pembayaran
    if len(dict_trx) > 0:
        print("================== Metode Pembayaran ==================")
        for i in daftar_pembayaran:
            print("Id : ", i, "\t Metode Pembayaran : ", daftar_pembayaran[i])
        
        # Pilih metode pembayaran
        pilih_metode = int(input("Pilih ID Metode Pembayaran : "))
        if pilih_metode in daftar_pembayaran:
            print("================== Detail Pesanan ==================")
            print("Nama Penerima        : ", dict_trx["nama penerima"])
            print("Alamat Penerima      : ", dict_trx["alamat penerima"])
            print("No Hp                : ", dict_trx["no Hp"])
            print("Kurir Pengiriman     : ", dict_trx["kurir pengiriman"])
            print("Produk               : ", data_product[pilih_id])
            print("Harga                : Rp", daftar_harga[pilih_id])
            print("Metode Pembayaran    : ", daftar_pembayaran[pilih_metode])
            
            # Konfirmasi pembayaran
            konfirmasi = input("Apakah Anda Yakin Ingin Melakukan Pembayaran ? (Y/N) : ")
            if konfirmasi.lower() == "y":
                print("Anda sudah berhasil melakukan pembayaran")
            else:
                print("Pembayaran dibatalkan.")
        else:
            print("Id metode pembayaran tidak tersedia.")
else:
    print("Id Product tidak tersedia.")
