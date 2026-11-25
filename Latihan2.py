data_mahasiswa = [
    {"nama": "Andi", "nilai": 80},
    {"nama": "Budi", "nilai": 55},
    {"nama": "Citra", "nilai": 75},
    {"nama": "Deni", "nilai": 45},
]

for mahasiswa in data_mahasiswa:

    if mahasiswa["nilai"] >= 60:
        mahasiswa["hasil"] = "lulus"
    else:
        mahasiswa["hasil"] = "tidak lulus"

print("nama\tnilai\thasil")
print("------------------------")

for mahasiswa in data_mahasiswa:
    print(
        f"{mahasiswa["nama"]}\t"
        f"{mahasiswa["nilai"]}\t"
        f"{mahasiswa["hasil"]}"
    )