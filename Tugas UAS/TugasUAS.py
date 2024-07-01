print('TUGAS UAS Percabangan dan perulangan')
# KELOMPOK
# NAMA : ANDRIAN MAULANA(23241020)
# NAMA : ISHMAT SYAFIQ SAUQI(23241001)
# NAMA : IRZA APRIANDI(23241034)
# NAMA : AGUS SETIAWAN(23241016)
# NAMA : IRSYAD HAKKI (23241004)

while True:
    
    print('---------------------------------')
    print('| MENU MAKANAN | MENU MINUMAN   |')
    print('|--------------|----------------|')
    print('| NasiGoreng   | Tuaq Manis     |')
    print('| NasiLindung  | Teh Manis      |')
    print('| MieBangladesh| Es susu        |')
    print('|-------------------------------|')

    NasiGoreng = 15000
    NasiLindung = 20000
    MieBangladesh = 10000
    TuaqManis = 10000
    TehManis = 5000
    esSusu = 5000

    pesananMakanan = input('Masukkan Pesanan makanan : ')

    if pesananMakanan == 'nasi goreng':
        hargaMakanan = NasiGoreng
        print('1 porsi nasi goreng' ,hargaMakanan,'Rp')
    elif pesananMakanan == 'nasi lindung':
        hargaMakanan = NasiLindung
        print('1 porsi nasi lindung' ,hargaMakanan,'Rp')
    elif pesananMakanan == 'mie bangladesh':
        hargaMakanan = MieBangladesh
        print('1 porsi Mie bangladesh' ,hargaMakanan,'Rp')
    else:
        hargaMakanan = 0
        print(' makanan ini tidak tersedia dalam menu kami')
        continue 

    pesananMinuman = input('Pesan minuman? (ya/tidak): ')

    if pesananMinuman == 'ya':
        pesananMinuman = input('Masukkan pesanan minuman : ')
        if pesananMinuman == 'tuaq manis':
            hargaMinuman = TuaqManis
            print('Tuaq Manis satu' ,hargaMinuman,'Rp')
        elif pesananMinuman == 'teh manis':
            hargaMinuman = TehManis
            print('Teh Manis satu' ,hargaMinuman,'Rp')
        elif pesananMinuman == 'es susu':
            hargaMinuman = esSusu
            print('Es Susu satu' ,hargaMinuman,'Rp')
        else:
            hargaMinuman = 0
            print('Pesanan minuman tidak tersedia di dalam menu kami')
            continue
    elif pesananMinuman == 'tidak':
        hargaMinuman = 0
       
    else:
        print('ketik (ya/tidak)')
        continue

    total = hargaMakanan + hargaMinuman

    print('=============================')
    print('Total belanja anda' , total,'Rp')
    print('=============================')

    pesanLagi = input('Mau memesan lagi? (ya/tidak): ')
    if pesanLagi != 'ya':
        break  

print('Terima kasih telah memesan!')
