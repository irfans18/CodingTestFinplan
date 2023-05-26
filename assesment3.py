"""
Buatlah fungsi pengecekan kata sandi, dengan ketentuan sebagai 
Kata sandi minimal 8 karakter
Kata sandi maksimal 32 karakter
Karakter awal tidak boleh angka
Harus memiliki angka
Harus memiliki huruf kapital dan huruf kecil

Contoh
Input : 5andiwara
Output : Karakter awal tidak boleh angka

Input : sandiwar4
Output : Harus memiliki huruf kapital dan huruf kecil

Input : Sandiwar4
Output : Kata sandi valid

"""


def check_password(password):
    if len(password) < 8:
        return "Kata sandi minimal 8 karakter"
    elif len(password) > 32:
        return "Kata sandi maksimal 32 karakter"
    elif password[0].isdigit():
        return "Karakter awal tidak boleh angka"
    elif not any(char.isdigit() for char in password):
        return "Harus memiliki angka"
    elif not any(char.isupper() for char in password) or not any(
        char.islower() for char in password
    ):
        return "Harus memiliki huruf kapital dan huruf kecil"
    else:
        return "Kata sandi valid"


if __name__ == "__main__":
    password = "5andiwara"
    result = check_password(password)
    print(result)
