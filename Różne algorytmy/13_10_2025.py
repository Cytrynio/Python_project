lista = [1,[2,3],4,5,[6,7,8],9]

def extract_to_list(nested_data):
    new_list = []
    for i in nested_data:
        if type(i) == list:
            for j in i:
                new_list.append(j)
        else:
               new_list.append(i)
    return new_list

print(extract_to_list(lista))