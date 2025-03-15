
lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']

listaA = [1, 2, 3, 4, 5, 6, 7]
listaB = [1, 2, 3, 4]

# def zipper(list1, list2):
#     cities_and_captains = list(zip(list1, list2))
#     return cities_and_captains


# final_list = zipper(lista1, lista2)
# print(final_list)

def zipper2(list1, list2):
    interval = min(len(list1), len(list2))
    print(interval)
    return [(list1[i], list2[i]) for i in range(interval)]


print(zipper2(lista1, lista2))

# def sum_lists(list1, list2):
#     interval = min(len(list1), len(list2))
#     return [(list1[i] + list2[i]) for i in range(interval)]


# print(sum_lists(listaA, listaB))
