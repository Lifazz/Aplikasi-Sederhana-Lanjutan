BuahJerukPerkilo = 15000 
BuahApelPerkilo = 30000
BuahManggaPerkilo = 20000
BuahManggisPerkilo = 7000
BuahDurianPerkilo = 50000

JumlahJeruk = 3
JumlahApel = 2
JumlahMangga = 0
JumlahManggis = 5
JumlahDurian = 2

JumlahBuahJeruk = BuahJerukPerkilo * JumlahJeruk
JumlahBuahApel = BuahApelPerkilo * JumlahApel
JumlahBuahMangga = BuahManggaPerkilo * JumlahMangga
JumlahBuahManggis = BuahManggisPerkilo * JumlahManggis
JumlahBuahDurian = BuahDurianPerkilo * JumlahDurian

Total = JumlahBuahJeruk + JumlahBuahApel + JumlahBuahMangga + JumlahBuahManggis + JumlahBuahDurian

print( " Total Buah Yang Harus Di Bayar : ")

print( " Jeruk 3 Kilo : %.0f"% JumlahBuahJeruk)
print( " Apel 2 Kilo : %.0f"% JumlahBuahApel)
print( " Mangga 0 Kilo : %.0f"% JumlahBuahMangga)
print( " Manggis 5 Kilo : %.0f"% JumlahBuahManggis)
print( " Durian 2 Kilo : %.0f"% JumlahBuahDurian)

print( "Total Belanja Buah Yang Harus Dibayar : %.0f"% Total)