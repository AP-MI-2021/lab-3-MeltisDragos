def citire_lista():
    l = []
    a = int(input("Dati Numarul de elemente: "))
    for i in range(a):
        l.append(float(input("l[" + str(i+1) + "]=")))
    return l


def sir_crescator(l):
    '''
    Determina daca un sir este crescator
    :param lst: numere intregi
    :return: true sau false
    '''
    for i in range(1, len(l)):
        if l[i-1] > l[i]:
            return False
    return True


def test_sir_crescator():
    assert sir_crescator([12, 23, 34]) == True
    assert sir_crescator([12, 2, 34]) == False
    assert sir_crescator([1, 4, 6, 13, 4, 23, 4]) == False


test_sir_crescator()


def get_longest_sorted_asc(l):
    '''
    Determina cea mai lunga secventa de numere consecutive
    :param lst: numere intregi
    :return: numere intregi
    '''
    auxlist = []
    for i in range(len(l)):
        for j in range(len(l)):
            if sir_crescator(l[i:j+1]) and len(l[i:j+1]) >= len(auxlist):
                auxlist = l[i:j+1]
    return auxlist


def test_get_longest_sorted_asc():
    assert get_longest_sorted_asc([12, 23, 34, 3, 4, 5, 6, 7]) == [3, 4, 5, 6, 7]
    assert get_longest_sorted_asc([1, 4, 6, 13, 4, 23, 4]) == [1, 4, 6, 13]


test_get_longest_sorted_asc()


def ParteIntreagaEgalaCuParteaFrac(x):
    '''
    Determina daca partea fractionala a unui numar este egala cu partea intreaga
    :param x: numar float
    :return: DA sau NU
    '''
    k = str(x)
    if int(k.split(".")[1]) == int(k.split(".")[0]):
        return True
    return False


def test_ParteIntreagaEgalaCuParteaFrac():
    assert ParteIntreagaEgalaCuParteaFrac(101.101) == True
    assert ParteIntreagaEgalaCuParteaFrac(123.321) == False
    assert ParteIntreagaEgalaCuParteaFrac(10.1) == False


test_ParteIntreagaEgalaCuParteaFrac()


def  get_longest_equal_int_real(l):
    '''
    gaseste cea mai lunga secventa de numere cu aprtea intreaga egala cu partea fractionala
    :param l: o lista de numere de tip float
    :return: cea mai lunga secventa de numere
    '''
    auxlist = []
    for i in range(len(l)):
        for j in range(len(l)):
            if len(l[i:j + 1]) >= len(auxlist):
                a = 0
                for p in range(len(l[i:j + 1])):
                    if ParteIntreagaEgalaCuParteaFrac(l[i:j + 1][p]) == False:
                        a = a + 1
                if a == 0:
                    auxlist = l[i:j + 1]
    return auxlist


def test_get_longest_equal_int_real():
    assert get_longest_equal_int_real([101.101, 23.23, 12.32, 12.12, 23.23, 34.34]) == [12.12, 23.23, 34.34]
    assert get_longest_equal_int_real([12.23, 23.23, 12.12, 45.45]) == [23.23, 12.12, 45.45]


test_get_longest_equal_int_real()


def printMeniu():
    print("1.Citire date")
    print("2.Determina cea mai lunga secventa de numere consecutive")
    print("3.Determina cea mai lunga secventa de numere care au partea întreagă egală cu partea fracționară.")
    print("4.Iesire")


if __name__ == '__main__':
    lst = []
    while True:
        printMeniu()
        x = input("Dati optiunea ")
        if x == "1":
            lst = citire_lista()
        elif x == "2":
            print(get_longest_sorted_asc(lst))
        elif x == "3":
            print(get_longest_equal_int_real(lst))
        elif x == "4":
            break
        else: print("Eroare.Dati alta valoare.")