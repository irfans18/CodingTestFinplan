"""
Buat fungsi pencarian ‘sang gajah’, ‘serigala’, ‘harimau’.
Dengan contoh masukan dan keluaran sebagai berikut :

	Input	: Berikut adalah kisah sang gajah. Sang gajah memiliki teman serigala bernama DoeSang. Gajah sering dibela oleh serigala ketika harimau mendekati gajah.
Output	: sang gajah - sang gajah - serigala - serigala - harimau
"""


def search_animals(text):
    words = text.lower().split()
    output = []

    for word in words:
        if word == "sang" or word == "gajah":
            output.append("sang gajah")
        elif word == "serigala":
            output.append("serigala")
        elif word == "harimau":
            output.append("harimau")

    return " - ".join(output)


if __name__ == "__main__":
    text = "Berikut adalah kisah sang gajah. Sang gajah memiliki teman serigala bernama DoeSang. Gajah sering dibela oleh serigala ketika harimau mendekati gajah."
    result = search_animals(text)
    print("input :", text)
    print("\n", result)
