import random
import timeit

def selection_sort(list_func):
    n = len(list_func)
    for i in range(0, n):
        index_min = i
        for j in range(i+1, n):
            if list_func[j] < list_func[index_min]:
                index_min = j
        list_func[i], list_func[index_min] = list_func[index_min], list_func[i]
    return list_func

def bubble_sort(lista):
    n = len(lista)
    for i in range (n - 1):
        for j in range(n - 1):
            if lista[j] > lista [j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def insertion_sort(lista):
    n = len(lista)
    for i in range (1, n):
        insert_value = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > insert_value:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = insert_value
    return lista

if __name__ == '__main__':

    soma1 = 0
    soma2 = 0
    soma3 = 0

    for i in range(1, 4):
        lista = random.sample(range(100_000), 10_000)

        print()
        print(f'final de loop {i}')
        print(f'Unordered: {lista}')

        ordered_list = selection_sort(lista)
        start_time = timeit.default_timer()
        print(f'Selection_sort:   {ordered_list}')
        selection_sort(lista)
        tempo1 = timeit.default_timer() - start_time
        print(f' tempo:{timeit.default_timer() - start_time}')

        #ordered_list2 = bubble_sort(lista)
        #print(f'Bubble sort:   {ordered_list2}')

        print()
        print(f'Unordered: {lista}')

        ordered_list = bubble_sort(lista)
        start_time = timeit.default_timer()
        print(f'bublle_sort:   {ordered_list}')
        selection_sort(lista)
        tempo2 = timeit.default_timer() - start_time
        print(f' tempo:{timeit.default_timer() - start_time}')

        #ordered_list3 = insertion_sort(lista)
        #print(f'Insertion sort:   {ordered_list3}')

        print()
        print(f'Unordered: {lista}')

        ordered_list = insertion_sort(lista)
        start_time = timeit.default_timer()
        print(f'insertion_sort:   {ordered_list}')
        selection_sort(lista)
        tempo3 = timeit.default_timer() - start_time
        print(f' tempo:{timeit.default_timer() - start_time}')

        soma1 = tempo1 + soma1
        soma2 = tempo2 + soma2
        soma3 = tempo3 + soma3

media1 = soma1 / 3
media2 = soma2 / 3
media3 = soma3 / 3
print()


print(f'valor de selection_sort: {media1}', f'valor de bubble_sort: {media2}', f'valor insertion_sort: {media3}')

