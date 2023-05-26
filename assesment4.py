"""
Buat fungsi pengecekan bilangan cacah terkecil yang tidak ada dari data yang diinputkan. Dengan contoh input dan output sebagai berikut :
Contoh 1
Input : [5, 2, 8, 4, 3, 10]
Output : 6
Contoh 2
Input : [2, 3, 4, 6]
Output : 5
Contoh 3
Input : [8, 6, 7, 12]
Output : 9

"""


def find_smallest_positive_missing(numbers):
    smallest = 1

    for num in sorted(numbers):
        if num == smallest:
            smallest += 1
        elif num > smallest:
            return smallest

    return smallest


if __name__ == "__main__":
    numbers = [5, 2, 8, 4, 3, 10]
    result = find_smallest_positive_missing(numbers)
    print(result)
