# Hindi to English Translator Dictionary

translator = {
    "namaste": "hello",
    "pani": "water",
    "kitab": "book",
    "dost": "friend",
    "ghar": "home",
    "khana": "food",
    "school": "school",
    "paisa": "money",
    "samay": "time",
    "pyar": "love"
}

while True:
    user = input("enter your words")

    words = user.lower()
    print(translator.get(words))