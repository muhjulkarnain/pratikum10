"""membuat file dan menulis file kosong"""
file = open(r"D:\dataMhs.txt", "w+")
"""head"""
print("""DATA MAHASISWA
==================================""")


""" Masukan input """
repeat ="y"
while repeat =="y" or repeat == "y" :
    nim = str(input ("Masukan NIM : "))
    nama = str(input("Masukan NAMA : "))
    alamat = str(input("Masukan ALAMAT : "))
    """ menuliskan input ke dalam file """
    file.write(nim+" | "+nama+" | "+alamat+"\n")
    repeat = str(input("ulangi ?(y/n))"))
    if repeat == "n" or repeat == "N" :
        break
    elif repeat =="y" or repeat == "Y" :
        print("Masukan lagi!")
        continue
file.seak(0, 0)
data = file.read ()
""" output """
print("""=================================
     DATA
-----------------------------------""")
print(data)
print("----------------------------------")

"""menutup file"""

file.close()
