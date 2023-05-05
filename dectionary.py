import string
import random

template_mahasiswa ={
    'nama':'nama',
    'nim':'00000000',
    'fakultas':'fakultas',
    'prodi':'prodi',
}

data_mahasiswa={}
while True:
    mahasiswa = dict.fromkeys(template_mahasiswa.keys())
    mahasiswa['nama'] = input("Nama Mahasiswa = ")
    mahasiswa['nim'] = input("NIM Mahasiswa = ")
    mahasiswa['fakultas'] = input("Fakultas = ")
    mahasiswa['prodi']= input("Program studi = ")
    key = ''.join((random.choice(string.ascii_uppercase)for i in range(6)))
    print(f"\n {'KEY':<10} {'nama':<10} {'nim':<10} {'fakultas':<10} {'prodi':<10}")
    print("="*50)
    data_mahasiswa.update({key:mahasiswa})
    for mahasiswa in data_mahasiswa:
        key = mahasiswa

        nama = data_mahasiswa[key]['nama']
        nim = data_mahasiswa[key]['nim']
        fakultas = data_mahasiswa[key]['fakultas']
        prodi = data_mahasiswa[key]['prodi']
    
        print(f"{key:<10} {nama:<10} {nim:<10} {fakultas:<10} {prodi:<10}")
    print("\n")
    selesai = input("Masukan Data Mahasiswa(y/n)")
    if selesai == "n":
        break
    print("PROGRAM SELESAI")
