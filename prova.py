def mitjanaRang(num_elements):
    suma=0
    for i in range(num_elements):
        suma = i + suma

    return suma / num_elements

mitjana = mitjanaRang(10)
print(mitjana)