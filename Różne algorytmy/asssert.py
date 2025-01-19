# def dzielenie(x,y):
#     # assert y != 0, "Y == 0"
#     if x== 0 or y == 0:
#         raise ZeroDivisionError("Dzielenie przez 0")
#     print(x/y)
#
# try:
#     dzielenie(5,0)
# except:
#     print("Debilu nie przez 0")
#     raise



# num = 0
#
# while num <= 10:
#     print(num)
#     num += 1


def samogloska(str):
    amount = 0
    vowels = "aeiouAEIOU"
    for char in str:
        if char in vowels:
            amount +=1
    return amount

print(samogloska("Dupa blada jasna panna"))