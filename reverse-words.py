# Reverse-Words
def reverse_words(sentence):
    words = sentence.split()
    res = ""
    for word in words[::-1]:
        res += word + " "
    return res.strip()