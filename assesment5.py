"""
Buat pola berikut sesuai inputan N, dengan N adalah bilangan ganjil

*catatan : nilai lebih jika pakai rekursif
Contoh 1
Input : 5
Output : 
XXXXX
XOOXX
XOXOX
XXOOX
XXXXX
Contoh 2
Input : 3
XXX
XXX
XXX
Output : 5
Contoh 3
Input : 7
Output : 
XXXXXXX
XOOOOXX
XOOOXOX
XOOXOOX
XOXOOOX
XXOOOOX
XXXXXXX
Contoh 3
Input : 2
Output :
Harus bilangan ganjil


"""


def print_pattern(N):
    if N % 2 == 0:
          print("Harus bilangan ganjil")
          return 0
      #   return "Harus bilangan ganjil"

    pattern = [["X"] * N for _ in range(N)]
    k=N-2
    for i in range(1, N - 1):
        for j in reversed(range(1, N-1)):
      #   for j in range(N-2, 1, -1):
            if j== k:
               pattern[i][k] = "X"
            else:
               pattern[i][j] = "O"
            
        k=k-1

    for row in pattern:
        print("".join(row))

if __name__ == "__main__":
     print_pattern(5)
