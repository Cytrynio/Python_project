lista = [1,4,5,67,8,3,22,34,66,4,2]
#
#
# def sorting (x):
#     n = len(x)
#     for i in range(n):
#         for j in range (0, n - i - 1):
#             if x[j] > x[j+1]:
#                 x[j], x[j+1] = x[j+1], x[j]
#     return x
#
#
#
# print(sorting(lista))
#
#
# def pali(txt):
#     if txt == txt[::-1]:
#         return "Palindrome"
#     else:
#         return  "Not palindrome"
#
# print(pali("abaa"))

# def no_dupli(list):
#     clear_list = []
#     for i in list:
#         if i in clear_list:
#             continue
#         else:
#             clear_list.append(i)
#     return clear_list


# print(no_dupli(lista))


def max_val(list):
    max_value = 0
    for i in list:
        if i > max_value:
            max_value = i
    return max_value

print(max_val(lista))
