def liczba_samo(str):
    num = 0
    samogloska = "aeiouAEIOU"
    for char in str:
        if char in samogloska:
           num += 1
    return num

text = "samowola"
print(liczba_samo(text))