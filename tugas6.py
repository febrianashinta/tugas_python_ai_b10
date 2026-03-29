import numpy as np
import pandas as pd
import os

# (Opsional) set seed agar hasil acak konsisten
np.random.seed(42)

# === NUMPY ===
# Buat array nilai ujian (10 data acak antara 50–100)
nilai_ujian = np.random.randint(50, 101, size=10)

# Hitung statistik
rata2 = np.mean(nilai_ujian)
median = np.median(nilai_ujian)
std_dev = np.std(nilai_ujian)
nilai_min = np.min(nilai_ujian)
nilai_max = np.max(nilai_ujian)

print("=== NUMPY ===")
print("Data nilai ujian:", nilai_ujian)
print(f"Rata-rata: {rata2:.2f}")
print(f"Median: {median}")
print(f"Standar deviasi: {std_dev:.2f}")
print(f"Nilai minimum: {nilai_min}")
print(f"Nilai maksimum: {nilai_max}")

# === PANDAS ===
# Buat DataFrame
data = {
    "nama": ["Rina", "Budi", "Sari", "Andi", "Dewi"],
    "nim": ["A001", "A002", "A003", "A004", "A005"],
    "nilai": nilai_ujian[:5]  # ambil 5 nilai pertama dari array
}
df = pd.DataFrame(data)

# Tambahkan kolom status
df["status"] = df["nilai"].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")

print("\n=== PANDAS ===")
print(df.head())

# === FILE I/O ===
# Ringkasan statistik
ringkasan = []
ringkasan.append("=== RINGKASAN STATISTIK ===")
ringkasan.append(f"Rata-rata: {rata2:.2f}")
ringkasan.append(f"Median: {median}")
ringkasan.append(f"Standar deviasi: {std_dev:.2f}")
ringkasan.append(f"Nilai minimum: {nilai_min}")
ringkasan.append(f"Nilai maksimum: {nilai_max}")
ringkasan.append("\n=== RINGKASAN DATAFRAME ===")
ringkasan.append(f"Jumlah baris: {len(df)}")
ringkasan.append(f"Jumlah LULUS: {(df['status'] == 'LULUS').sum()}")
ringkasan.append(f"Jumlah TIDAK LULUS: {(df['status'] == 'TIDAK LULUS').sum()}")

with open("ringkasan_tugas6.txt", "w") as f:
    f.write("\n".join(ringkasan))

# === OOP: GRADEBOOK ===
class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        return self.df["nilai"].mean()

    def pass_rate(self, threshold: float = 70.0) -> float:
        total = len(self.df)
        passed = (self.df["nilai"] >= threshold).sum()
        return (passed / total) * 100

    def save_summary(self, path: str):
        summary = []
        summary.append("=== GRADEBOOK SUMMARY ===")
        summary.append(f"Jumlah data: {len(self.df)}")
        summary.append(f"Rata-rata nilai: {self.average():.2f}")
        summary.append(f"Persentase lulus: {self.pass_rate():.2f}%")
        with open(path, "a") as f:
            f.write("\n".join(summary) + "\n")

    def __str__(self):
        return f"GradeBook dengan {len(self.df)} data, rata-rata nilai {self.average():.2f}"

if __name__ == "__main__":
    print("\n=== OOP: GRADEBOOK ===")
    gb = GradeBook(df)
    print(gb)
    print("Rata-rata nilai:", gb.average())
    print("Persentase lulus:", gb.pass_rate())
    gb.save_summary("ringkasan_tugas6.txt")
