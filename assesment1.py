"""
Buat fungsi dengan menampilkan bilangan cacah kelipatan 3 atau 7 sebanyak N, serta menampilkan huruf Z saat bilangan tersebut kelipatan 3 dan 7.
Contoh :
N = 13
Output : 3, 6, 7, 9, 12, 14, 15, 18, Z, 24, 27, 28, 30
"""


def print_numbers(N):
    count = 0
    number = 0

    while count < N:
        number += 1
        if number % 3 == 0 or number % 7 == 0:
            count += 1
            if number % 3 == 0 and number % 7 == 0:
                print("Z", end=" ")
            else:
                print(number, end=" ")


if __name__ == "__main__":
    print_numbers(13)
