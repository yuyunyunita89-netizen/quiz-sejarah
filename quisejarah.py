import random

# Soal-soal quiz
soal = [
    {"soal": "Siapa yang memimpin pasukan Mongol?", "option": ["Genghis Khan", "Alexander Agung", "Napoleon Bonaparte", "Julius Caesar"], "jawaban": 1},
    {"soal": "Perang Dunia II terjadi pada tahun?", "option": ["1939-1945", "1914-1918", "1945-1950", "1950-1955"], "jawaban": 2},
    {"soal": "Siapa yang menemukan Amerika?", "option": ["Christopher Columbus", "Vasco da Gama", "Ferdinand Magellan", "Amerigo Vespucci"], "jawaban": 3},
]

# Fungsi untuk menampilkan soal
def tampilkan_soal(soal):
    print(soal["soal"])
    for i, option in enumerate(soal["option"]):
        print(f"{i+1}. {option}")

# Fungsi untuk memeriksa jawaban
def periksa_jawaban(soal, jawaban):
    if jawaban == soal["jawaban"]:
        return True
    else:
        return False

# Fungsi untuk menjalankan quiz
def jalankan_quiz(soal):
    skor = 0
    for i, s in enumerate(soal):
        print(f"\nSoal {i+1}:")
        tampilkan_soal(s)
        jawaban = int(input("Masukkan jawaban (1-4): ")) - 1
        if periksa_jawaban(s, jawaban):
            skor += 1
            print("Jawaban benar!")
        else:
            print(f"Jawaban salah. Jawaban yang benar adalah {s['option'][s['jawaban']]}")
    print(f"\nSkor akhir: {skor}/{len(soal)}")

# Jalankan quiz
jalankan_quiz(soal)
print("Try programiz.pro")