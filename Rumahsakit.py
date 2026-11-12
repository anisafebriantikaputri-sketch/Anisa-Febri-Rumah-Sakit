print("=" * 65)
print("     RS SEHAT MEDIKA - INPUT MANUAL KEPARAHAN PASIEN OPNAME")
print("=" * 65)

daftar_penyakit = {
    1: "Serangan Jantung",
    2: "Stroke Akut",
    3: "Kecelakaan Berat (Trauma)",
    4: "Demam Berdarah (DBD)",
    5: "Tifus Parah",
    6: "Pneumonia / Infeksi Paru",
    7: "Gagal Ginjal Kronis",
    8: "Asma Bronkial Ringan",
    9: "Diare Akut Dehidrasi Ringan",
    10: "Infeksi Saluran Kemih (ISK)"
}

print("\n--- PILIH 10 JENIS DIAGNOSIS PENYAKIT ---")
for nomor, nama in daftar_penyakit.items():
    print(f"{nomor:2d}. {nama}")

print("-" * 65)
nama_pasien = input("Masukkan Nama Pasien\t\t: ")
print(nama_pasien)

try:
    pilihan = int(input("Pilih nomor diagnosis (1-10)\t: "))
    print(pilihan)
    skor_keparahan = int(input("Masukkan Skor Keparahan (Skala 1-10): "))
    print(skor_keparahan)
except ValueError:
    pilihan = 0
    skor_keparahan = 0

input_bpjs = input("Menggunakan Asuransi BPJS? (y/t)\t: ").strip().lower()
print(input_bpjs)
punya_bpjs = True if input_bpjs == 'y' else False

print("\n" + "=" * 65)
print("                    HASIL ANALISIS RUMAH SAKIT")
print("=" * 65)

if pilihan in daftar_penyakit:
    nama_penyakit = daftar_penyakit[pilihan]

    print(f"Nama Pasien      : {nama_pasien}")
    print(f"Diagnosis        : {nama_penyakit}")
    print(f"Skor Keparahan   : {skor_keparahan} / 10 (Input Mandiri)")
    print(f"Status BPJS      : {'AKTIF (BPJS)' if punya_bpjs else 'UMUM / MANDIRI'}")
    print("-" * 65)

    if skor_keparahan >= 8:
        print("Tindakan Medis   : WAJIB masuk RUANG ICU (Penanganan Intensif Kritis).")
    elif skor_keparahan >= 5 and skor_keparahan < 8:
        if punya_bpjs:
            print("Tindakan Medis   : Diopname di Bangsal Kelas 2 (Ditanggung BPJS).")
        else:
            print("Tindakan Medis   : Diopname di Kamar VIP / Kelas 1 (Umum).")
    elif skor_keparahan > 0 and skor_keparahan < 5:
        print("Tindakan Medis   : Cukup RAWAT JALAN (Diberikan resep obat & kontrol poli).")
    else:
        print("Tindakan Medis   : Skor keparahan tidak valid (Harus antara 1 - 10).")
else:
    print("Status Error     : Nomor diagnosis yang Anda masukkan tidak valid (Pilih 1-10).")

print("=" * 65)