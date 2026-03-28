# Tugas 5 - Fungsi dan Kelas
# Nama: Zulkifli

# ---- FUNGSI ----

def greet(nama: str) -> str:
    return "Halo, " + nama + "!"

def tambah(a: float, b: float = 0.0) -> float:
    hasil = a + b
    return hasil

def rata_rata(angka: list) -> float:
    if len(angka) == 0:
        return 0.0
    total = sum(angka)
    rata = total / len(angka)
    return round(rata, 2)


# ---- KELAS STUDENT ----

class Student:
    def __init__(self, nama: str, nim: str):
        self.nama = nama
        self.nim = nim
        self.nilai = []

    def tambah_nilai(self, skor: float):
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        if self.rata_nilai() >= threshold:
            return "LULUS"
        return "TIDAK LULUS"

    def __str__(self):
        return "Student(nama='" + self.nama + "', nim='" + self.nim + "', rata=" + str(self.rata_nilai()) + ", status=" + self.status() + ")"


# ---- DEMO ----

if __name__ == "__main__":

    print("=== FUNCTIONS ===")

    print(greet("Nindy"))

    print("tambah(5, 7) =", tambah(5, 7))
    print("tambah(10) =", tambah(10))

    print("rata_rata([80, 90, 100]) =", rata_rata([80, 90, 100]))
    print("rata_rata([]) =", rata_rata([]))

    print()
    print("=== CLASS STUDENT ===")

    mhs1 = Student("Zulkifli", "2321037")
    mhs1.tambah_nilai(80)
    mhs1.tambah_nilai(75)
    mhs1.tambah_nilai(90)

    mhs2 = Student("Nindy", "2521038")
    mhs2.tambah_nilai(60)
    mhs2.tambah_nilai(55)
    mhs2.tambah_nilai(65)

    print(mhs1)
    print("Rata-rata:", mhs1.rata_nilai())
    print("Status:", mhs1.status())

    print()

    print(mhs2)
    print("Rata-rata:", mhs2.rata_nilai())
    print("Status:", mhs2.status())