UangBelanja = int(input( " Masukan Uang Belanja Anda : " ))
TotalBelanja = int(input( " Masukan Total Biaya Belanja Anda : " ))

if TotalBelanja > 70000:
    DiskonToko = TotalBelanja * (10/100)
else : DiskonToko = 0

print( " Anda Menerima DIskon Belanja Sebesar : %.0f"% DiskonToko)

KembalianBelanja = UangBelanja - TotalBelanja + DiskonToko

print( " Total Kembalian Uang Belanja Anda : %.0f"% KembalianBelanja)