ket='''selamat datang diaplikasi perhitungan
       silahkan pilih menu yang akan anda jalankan
1. menghitung luas persegi
2. menghitung luas lingkaran
3. menghitung luas segitiga'''


pilihan =input(ket)

match pilihan:
    case"1":
        print("kamu memilih 1 untuk menghitung luas persegi")
        sisi= float(input("masukan sisi"))
        luas= sisi*sisi
        print("luas persegi yang sisinya ",sisi,"adalah ,luasP")
    case"2":
        print("kamu memilih 2 untuk menghitung luas lingkaran")
        jari= float(input("masukan jari-jari: "))
        luas=3.14*jari*jari
        print("luas lingkaran yang jari-jarinya",jari,"adalah",int(luas))
    case"3":
        print("kamu memilih 3 untuk menghitung luas segitiga")
        alas= int(input("masukan alas : "))
        tinggi= int(input("masukan tinggi : "))
        luas= 0.5*alas*tinggi 
        print("luas segitiga yang alasnya ",alas,"dan tingginya",tinggi,"adalah",int(luasS))
    case _:
        print("anda salah memilih")