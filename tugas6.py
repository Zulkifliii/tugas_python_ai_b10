# Tugas 6 - NumPy, Pandas, dan OOP
# Nama: Zulkifli

import numpy as np
import pandas as pd

np.random.seed(42)


# ---- NUMPY ----

nilai_ujian = np.array([78, 85, 60, 92, 55, 88, 73, 65, 90, 70])

rata = np.mean(nilai_ujian)
median = np.median(nilai_ujian)
std = np.std(nilai_ujian)
minimum = np.min(nilai_ujian)
maksimum = np.max(nilai_ujian)


# ---- PANDAS ----

data_mhs = {
    "nama": ["Zulkifli", "Nindy", "Budi", "Sari", "Dewi"],
    "nim": ["2321037", "2321038", "2321039", "2321040", "2321041"],
    "nilai": nilai_ujian[:5]
}

df = pd.DataFrame(data_mhs)
df["status"] = df["nilai"].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")


# ---- KELAS GRADEBOOK ----

class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        return round(self.df["nilai"].mean(), 2)

    def pass_rate(self, threshold: float = 70.0) -> float:
        lulus = len(self.df[self.df["nilai"] >= threshold])
        return round(lulus / len(self.df) * 100, 2)

    def save_summary(self, path: str):
        with open(path, "a") as f:
            f.write("\n=== RINGKASAN GRADEBOOK ===\n")
            f.write("Jumlah data: " + str(len(self.df)) + "\n")
            f.write("Rata-rata nilai: " + str(self.average()) + "\n")
            f.write("Persentase lulus: " + str(self.pass_rate()) + "%\n")

    def __str__(self):
        return "GradeBook(jumlah=" + str(len(self.df)) + ", rata=" + str(self.average()) + ")"


# ---- DEMO ----

if __name__ == "__main__":

    print("=== NUMPY ===")
    print("Data nilai:", nilai_ujian)
    print("Rata-rata:", rata)
    print("Median:", median)
    print("Std deviasi:", round(std, 2))
    print("Nilai min:", minimum)
    print("Nilai max:", maksimum)

    print()
    print("=== PANDAS ===")
    print(df.head())
    print("Jumlah baris:", len(df))
    print("Jumlah lulus:", len(df[df["status"] == "LULUS"]))
    print("Jumlah tidak lulus:", len(df[df["status"] == "TIDAK LULUS"]))

    # Tulis ringkasan ke file
    with open("ringkasan_tugas6.txt", "w") as f:
        f.write("=== RINGKASAN STATISTIK NUMPY ===\n")
        f.write("Rata-rata : " + str(rata) + "\n")
        f.write("Median    : " + str(median) + "\n")
        f.write("Std Dev   : " + str(round(std, 2)) + "\n")
        f.write("Min       : " + str(minimum) + "\n")
        f.write("Max       : " + str(maksimum) + "\n")
        f.write("\n=== RINGKASAN DATAFRAME ===\n")
        f.write("Jumlah baris      : " + str(len(df)) + "\n")
        f.write("Jumlah lulus      : " + str(len(df[df["status"] == "LULUS"])) + "\n")
        f.write("Jumlah tidak lulus: " + str(len(df[df["status"] == "TIDAK LULUS"])) + "\n")

    print()
    print("=== OOP: GRADEBOOK ===")
    gb = GradeBook(df)
    print(gb)
    print("Average:", gb.average())
    print("Pass rate:", gb.pass_rate(), "%")
    gb.save_summary("ringkasan_tugas6.txt")
    print("Ringkasan disimpan ke ringkasan_tugas6.txt")
