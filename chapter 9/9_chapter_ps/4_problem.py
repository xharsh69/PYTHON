 


with open("f_words.txt", "r") as f:
    r = f.read()

words = ["fuck", "bitch"]

for word in words:
    w = len(word)
    r = r.replace(word, "#" * w)

with open("f_words.txt", "w") as f:
    f.write(r)