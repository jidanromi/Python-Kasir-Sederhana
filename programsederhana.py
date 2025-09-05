def hitung_angsuran(harga_mobil, dp_persen, tenor_bulan):
    # Hitung DP
    dp = harga_mobil * (dp_persen / 100)
    
    # Hitung sisa hutang
    sisa_hutang = harga_mobil - dp
    
    # Hitung angsuran per bulan
    angsuran_per_bulan = sisa_hutang / tenor_bulan
    
    return dp, sisa_hutang, angsuran_per_bulan


# Input
harga_mobil = 240_000_000   
dp_persen = 20              # DP 20%
tenor_bulan = 18            # Cicilan 1,5 tahun = 18 bulan

# Hitung
dp, sisa_hutang, angsuran_per_bulan = hitung_angsuran(harga_mobil, dp_persen, tenor_bulan)

# Output
print("=== Perhitungan Kredit Mobil ===")
print(f"Harga Mobil         : Rp {harga_mobil:,}")
print(f"Down Payment (DP)   : Rp {dp:,}")
print(f"Sisa Hutang         : Rp {sisa_hutang:,}")
print(f"Tenor               : {tenor_bulan} bulan")
print(f"Angsuran per Bulan  : Rp {angsuran_per_bulan:,.0f}")
