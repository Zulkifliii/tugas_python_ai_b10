# Tugas 3 - Dasar Python
# Nama: Zulkifli

# -- 1. Variabel dan Tipe Data --
nama = "Zulkifli"
umur = 21
nilai_rata = 87.5
lulus = True
mata_kuliah = ["Python", "AI", "Matematika", "Statistik", "Basis Data"]

print("=" * 40)
print("1. Deklarasi Variabel")
print("=" * 40)
print("Nama:", nama, "| tipe:", type(nama))
print("Umur:", umur, "| tipe:", type(umur))
print("Nilai rata-rata:", nilai_rata, "| tipe:", type(nilai_rata))
print("Status lulus:", lulus, "| tipe:", type(lulus))
print("Mata kuliah:", mata_kuliah, "| tipe:", type(mata_kuliah))

# -- 2. Manipulasi String --
print("\n" + "=" * 40)
print("2. Manipulasi String")
print("=" * 40)

sapaan = "Halo"
gabung = sapaan + " " + nama + "!"
print("Hasil gabung:", gabung)
print("Jumlah karakter nama:", len(nama))
print("Nama kapital:", nama.upper())
print("Nama kecil:", nama.lower())

# -- 3. Operasi Matematika --
print("\n" + "=" * 40)
print("3. Operasi Matematika")
print("=" * 40)

nilai1 = 25
nilai2 = 7

print("nilai1 =", nilai1, "| nilai2 =", nilai2)
print("Tambah:", nilai1 + nilai2)
print("Kurang:", nilai1 - nilai2)
print("Kali:", nilai1 * nilai2)
print("Bagi:", round(nilai1 / nilai2, 2))
print("Bagi bulat:", nilai1 // nilai2)
print("Sisa bagi:", nilai1 % nilai2)

# -- 4. List Buah --
print("\n" + "=" * 40)
print("4. Daftar dan Akses Elemen")
print("=" * 40)

buah = ["Apel", "Mangga", "Jeruk", "Pisang", "Anggur"]
print("List awal:", buah)
print("Buah pertama:", buah[0])
print("Buah ke-3:", buah[2])
print("Buah terakhir:", buah[-1])

buah.append("Semangka")
print("Setelah ditambah:", buah)

buah.remove("Jeruk")
print("Setelah Jeruk dihapus:", buah)

buah.pop()
print("Setelah pop:", buah)

# -- 5. Input User --
print("\n" + "=" * 40)
print("5. Input dari User")
print("=" * 40)

nama_user = input("Nama kamu: ")
umur_user = int(input("Umur kamu: "))

print("\nHalo, nama saya", nama_user, "dan umur saya", str(umur_user) + " tahun.")