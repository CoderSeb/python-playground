# Skriv ett program för att hitta antal lika värden i 2 givna listor.
array1 = [1, 2, 3, 4]
array2 = [1, 2, 3, 5]
array3 = [11, 22, 33, 44]

"""
Funktionen checkSameElements tar in 2 listor (arrayer) vars värden
jämförs och sedan returneras antalet lika värden i de båda listorna.
"""


def checkSameElements(arr1, arr2):
    result = 0
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                result += 1

    return result


print(checkSameElements(array1, array1))
print(checkSameElements(array1, array2))
print(checkSameElements(array1, array3))
