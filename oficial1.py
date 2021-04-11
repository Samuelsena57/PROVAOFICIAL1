# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import csv


# read csv file as a list of lists
def read_csv():
    courses = []
    with open('cursos-prouni2.csv', newline='') as inputfile:
        for row in csv.reader(inputfile):
            courses.append(row[0])

    return courses


# Press the green button in the gutter to run the script.
if _name_ == '_main_':
    courses_name = read_csv()
    #print(courses_name)
    print(type(courses_name))
    print(sorted(set(courses_name)))
# See PyCharm help at

# Respostas das pergutas referente a letra 'e' do numero 1, e numero 2.
# resposta do numero 1 letra e = Em minha opniao o isertion_sort e mais rapido com uma quantidade maior de numeros, pois com um valor menor não dar pra se notar.
# resposta do numero 2
# Busca binária
# Ela dividi o valor ao meio, nesta divisão ele valida se o valor que é solicitado é menor ou maior do que o valor feito nessa divisão.
# Busca Linear
# Ele e comparado valor a valor ate achar o valor desejado, nesse contexto pode se dizer que ele trabalha com sorte, pois se ele for o ultimo da lista tera que percorrer toda a lista ate chegar nele.
