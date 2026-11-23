import math


def luas_persegi_panjang(panjang, lebar):
    """Menghitung luas persegi panjang: panjang x lebar."""
    return panjang * lebar


def volume_balok(panjang, lebar, tinggi):
    """Menghitung volume balok: panjang x lebar x tinggi."""
    return panjang * lebar * tinggi


def luas_lingkaran(jari_jari):
    """Menghitung luas lingkaran: pi x r^2."""
    return math.pi * jari_jari ** 2


def volume_bola(jari_jari):
    """Menghitung volume bola: 4/3 x pi x r^3."""
    return (4 / 3) * math.pi * jari_jari ** 3


def input_angka(pesan):
    """Meminta input angka dan mengulang sampai nilainya valid dan positif."""
    while True:
        try:
            nilai = float(input(pesan))
            if nilai > 0:
                return nilai
            print("Nilai harus lebih dari 0.")
        except ValueError:
            print("Masukkan angka yang valid.")


def main():
    print("=" * 40)
    print("PROGRAM HITUNG BANGUN RUANG DAN DATAR".center(40))
    print("=" * 40)
    print("a. Luas persegi panjang")
    print("b. Volume balok")
    print("c. Luas lingkaran")
    print("d. Volume bola")
    print("e. Keluar")

    while True:
        pilihan = input("\nPilih menu [a-e]: ").strip().lower()

        if pilihan == "a":
            p = input_angka("Panjang: ")
            l = input_angka("Lebar: ")
            print(f"Luas persegi panjang = {luas_persegi_panjang(p, l):.2f}")

        elif pilihan == "b":
            p = input_angka("Panjang: ")
            l = input_angka("Lebar: ")
            t = input_angka("Tinggi: ")
            print(f"Volume balok = {volume_balok(p, l, t):.2f}")

        elif pilihan == "c":
            r = input_angka("Jari-jari: ")
            print(f"Luas lingkaran = {luas_lingkaran(r):.2f}")

        elif pilihan == "d":
            r = input_angka("Jari-jari: ")
            print(f"Volume bola = {volume_bola(r):.2f}")

        elif pilihan == "e":
            print("Program selesai, terima kasih.")
            break

        else:
            print("Pilihan tidak valid, masukkan a, b, c, d, atau e.")


if __name__ == "__main__":
    main()