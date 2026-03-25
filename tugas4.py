print("        TUGAS 4 - STRUKTUR DATA PYTHON")
print("        Zulkifli | Institut Teknologi Batam")

# 1. LIST

# campuran: nama, angka, bool, dsb
data_list = ["Zulkifli", 21, "Batam", 3.75, True, "Informatika"]

print("List awal :", data_list)
print("Elemen pertama :", data_list[0])
print("Elemen terakhir:", data_list[-1])

# slicing [start:stop:step]
print("Slicing [1:5:2]:", data_list[1:5:2])

# append()
print("\n-- append('Python') --")
print("Sebelum:", data_list)
data_list.append("Python")
print("Sesudah :", data_list)

# insert()
print("\n-- insert(2, 'Teknik') --")
print("Sebelum:", data_list)
data_list.insert(2, "Teknik")
print("Sesudah :", data_list)

# extend()
print("\n-- extend([99, 'extra']) --")
print("Sebelum:", data_list)
data_list.extend([99, "extra"])
print("Sesudah :", data_list)

# pop()
print("\n-- pop() --")
print("Sebelum:", data_list)
elemen_pop = data_list.pop()
print("Sesudah :", data_list)
print("Elemen yang di-pop:", elemen_pop)

# remove()
print("\n-- remove('Teknik') --")
print("Sebelum:", data_list)
data_list.remove("Teknik")
print("Sesudah :", data_list)

# 2. TUPLE

biodata = ("Zulkifli", 21, "Institut Teknologi Batam", "Informatika", "Batam")

print("Tuple :", biodata)
print("Panjang tuple:", len(biodata))
print("Akses index ke-2:", biodata[2])

# unpacking - pakai *rest buat sisa elemen
nama, umur, *rest = biodata
print(f"\nUnpacking -> nama: {nama}, umur: {umur}, rest: {rest}")

# 3. SET

matkul_semester3 = {"Kalkulus", "Struktur Data", "Basis Data", "Jaringan", "Python"}
matkul_semester4 = {"Python", "Basis Data", "Kecerdasan Buatan", "Web Dev", "Statistika"}

print("Set A (sem 3):", matkul_semester3)
print("Set B (sem 4):", matkul_semester4)

# coba masukin duplikat, otomatis hilang
coba_duplikat = {"Python", "Python", "Basis Data", "Basis Data", "AI"}
print("\nSet dengan duplikat input:", coba_duplikat)
print("(duplikat otomatis dihapus oleh set)")

print("\nUnion (|)               :", matkul_semester3 | matkul_semester4)
print("Intersection (&)        :", matkul_semester3 & matkul_semester4)
print("Difference A-B (-)      :", matkul_semester3 - matkul_semester4)
print("Symmetric Difference (^):", matkul_semester3 ^ matkul_semester4)

# 4. DICTIONARY

mahasiswa = {
    "nama"    : "Zulkifli",
    "nim"     : "2321037",
    "angkatan": 2023,
    "kota"    : "Batam"
}

print("Data awal:", mahasiswa)

# tambah kunci baru
mahasiswa["jurusan"] = "Informatika"
print("\nSetelah tambah 'jurusan':", mahasiswa)

# ubah nilai
mahasiswa["kota"] = "Batam - Kepulauan Riau"
print("Setelah ubah 'kota'    :", mahasiswa)

# hapus kunci
del mahasiswa["angkatan"]
print("Setelah hapus 'angkatan':", mahasiswa)

print("\nkeys()  :", list(mahasiswa.keys()))
print("values():", list(mahasiswa.values()))
print("items() :", list(mahasiswa.items()))

print("\nIterasi key: value ->")
for k, v in mahasiswa.items():
    print(f"  {k}: {v}")

# 5. STRUKTUR BERSARANG (list of dict)

daftar_buku = [
    {"judul": "Clean Code",              "penulis": "Robert C. Martin", "tahun": 2008},
    {"judul": "Python Crash Course",     "penulis": "Eric Matthes",     "tahun": 2015},
    {"judul": "Artificial Intelligence", "penulis": "Stuart Russell",   "tahun": 2020},
    {"judul": "Deep Learning",           "penulis": "Ian Goodfellow",   "tahun": 2016},
    {"judul": "Fluent Python",           "penulis": "Luciano Ramalho",  "tahun": 2022},
]

print("Semua judul buku:")
for buku in daftar_buku:
    print(f"  - {buku['judul']} ({buku['tahun']})")

# filter buku terbit >= 2016 pakai list comprehension
tahun_filter = 2016
buku_baru = [b["judul"] for b in daftar_buku if b["tahun"] >= tahun_filter]
print(f"\nBuku terbit >= {tahun_filter}:")
for judul in buku_baru:
    print(f"  - {judul}")

# 6. COMPREHENSION

angka_1_20 = list(range(1, 21))

# list comprehension - bilangan genap
genap = [x for x in angka_1_20 if x % 2 == 0]
print("Bilangan genap (1-20):", genap)

# list comprehension - kuadrat
kuadrat = [x**2 for x in angka_1_20]
print("Kuadrat (1-20)       :", kuadrat)

# dict comprehension - pemetaan genap/ganjil 1-10
peta_genap_ganjil = {x: ("genap" if x % 2 == 0 else "ganjil") for x in range(1, 11)}
print("\nDict genap/ganjil (1-10):", peta_genap_ganjil)

# set comprehension - huruf unik dari kalimat
kalimat = "Institut Teknologi Batam kampus kebanggaan saya"
huruf_unik = {c.lower() for c in kalimat if c.isalpha()}
print(f"\nHuruf unik dari kalimat '{kalimat}':")
print(" ", sorted(huruf_unik))

# 7. KEANGGOTAAN & PENCARIAN

buah = ["mangga", "apel", "pisang", "durian", "rambutan", "jeruk"]
buah_favorit_set = {"mangga", "durian", "nangka"}

# cek in pada list
cari = "durian"
if cari in buah:
    posisi = buah.index(cari)
    print(f"'{cari}' ADA di list, posisi index: {posisi}")
else:
    print(f"'{cari}' TIDAK ADA di list")

# cek yang tidak ada
cari2 = "nanas"
if cari2 in buah:
    print(f"'{cari2}' ADA di list, posisi index: {buah.index(cari2)}")
else:
    print(f"'{cari2}' TIDAK ADA di list")

# cek in pada set
cari3 = "nangka"
if cari3 in buah_favorit_set:
    print(f"'{cari3}' ADA di set buah favorit")
else:
    print(f"'{cari3}' TIDAK ADA di set buah favorit")

cari4 = "apel"
if cari4 in buah_favorit_set:
    print(f"'{cari4}' ADA di set buah favorit")
else:
    print(f"'{cari4}' TIDAK ADA di set buah favorit")
