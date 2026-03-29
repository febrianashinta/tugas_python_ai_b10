# struktur_data.py

# =========================
# List – akses & manipulasi
# =========================
data_list = [10, "apel", 3.14, "python", 42, "data"]

print("List awal:", data_list)
print("Elemen pertama:", data_list[0])
print("Elemen terakhir:", data_list[-1])
print("Slicing [1:5:2]:", data_list[1:5:2])

# Operasi manipulasi
data_list.append("baru")
print("Setelah append:", data_list)

data_list.insert(2, "inserted")
print("Setelah insert:", data_list)

data_list.extend([99, "extend"])
print("Setelah extend:", data_list)

removed = data_list.pop()  # hapus elemen terakhir
print("Pop elemen terakhir:", removed, "->", data_list)

data_list.remove("apel")
print("Setelah remove 'apel':", data_list)

# =========================
# Tuple – immutability & unpacking
# =========================
data_tuple = (1, 2, 3, 4, 5)
print("\nTuple:", data_tuple)
print("Panjang tuple:", len(data_tuple))
print("Akses indeks ke-2:", data_tuple[2])

a, b, *rest = data_tuple
print("Unpacking -> a:", a, "b:", b, "rest:", rest)

# =========================
# Set – keunikan & operasi himpunan
# =========================
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7}

print("\nSet A:", set_a)
print("Set B:", set_b)
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference A-B:", set_a - set_b)
print("Symmetric Difference:", set_a ^ set_b)

# Duplikat otomatis hilang
set_c = {1, 1, 2, 2, 3}
print("Set dengan duplikat:", set_c)

# =========================
# Dictionary – key/value dasar
# =========================
mahasiswa = {
    "nama": "Budi",
    "nim": "123456",
    "angkatan": 2022,
    "kota": "Batam"
}

print("\nDictionary awal:", mahasiswa)

# Tambah key baru
mahasiswa["jurusan"] = "Informatika"
print("Setelah tambah key:", mahasiswa)

# Ubah nilai key
mahasiswa["kota"] = "Jakarta"
print("Setelah ubah nilai:", mahasiswa)

# Hapus key
del mahasiswa["angkatan"]
print("Setelah hapus key:", mahasiswa)

print("Keys:", mahasiswa.keys())
print("Values:", mahasiswa.values())
print("Items:", mahasiswa.items())

print("Iterasi dictionary:")
for k, v in mahasiswa.items():
    print(f"{k}: {v}")

# =========================
# Nested structures
# =========================
buku_list = [
    {"judul": "Python Dasar", "penulis": "Andi", "tahun": 2019},
    {"judul": "Data Science", "penulis": "Budi", "tahun": 2021},
    {"judul": "AI Modern", "penulis": "Citra", "tahun": 2023},
    {"judul": "Machine Learning", "penulis": "Dewi", "tahun": 2018},
]

print("\nJudul semua buku:")
for buku in buku_list:
    print(buku["judul"])

tahun_filter = 2020
buku_terbaru = [b["judul"] for b in buku_list if b["tahun"] >= tahun_filter]
print(f"Buku terbit >= {tahun_filter}:", buku_terbaru)

# =========================
# Comprehension & utilitas
# =========================
angka = list(range(1, 21))
genap = [x for x in angka if x % 2 == 0]
kuadrat = [x**2 for x in angka]

print("\nList angka genap:", genap)
print("List kuadrat:", kuadrat)

dict_paritas = {x: ("genap" if x % 2 == 0 else "ganjil") for x in range(1, 11)}
print("Dict comprehension paritas:", dict_paritas)

kalimat = "Belajar Python itu menyenangkan"
huruf_unik = {c.lower() for c in kalimat if c.isalpha()}
print("Set comprehension huruf unik:", huruf_unik)

# =========================
# Keanggotaan & pencarian sederhana
# =========================
print("\nApakah 10 ada di list angka?", 10 in angka)
print("Apakah 'python' ada di data_list?", "python" in data_list)

if "python" in data_list:
    print("Posisi 'python' di data_list:", data_list.index("python"))
else:
    print("'python' tidak ditemukan")
