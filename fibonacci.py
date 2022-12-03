"""
Zadanie 1

Ciag Fibonacciego
0, 1, 1, 2, 3, 5, 8, 13, 21, ...

f(x) = f(x-1) + f(x-2)
f(1) = 0
f(2) = 1

x >= 1

f(1) = 0

f(x) = x + 1

f(3) = 4

a(x) = wartosc x-ego elementu ciagu fibonacciego
a(3) = a(3-1) + a(3-2) = a(2) + a(1)

"""


def get_fibonacci_value_for_n(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return get_fibonacci_value_for_n(n - 1) + get_fibonacci_value_for_n(
            n - 2)


def ciag_f_iter(element_ciagu):
    dwa_wstecz = 0
    jeden_wstecz = 1

    if element_ciagu == 1:
        return 0
    elif element_ciagu == 2:
        return 1
    else:
        for i in range(element_ciagu - 2):
            suma = dwa_wstecz + jeden_wstecz
            dwa_wstecz = jeden_wstecz
            jeden_wstecz = suma
        return suma


def main():
    while True:
        nr_elementu = int(input('Podaj element ciagu \n'))
        if nr_elementu > 99:
            break
        print(ciag_f_iter(nr_elementu))


if __name__ == '__main__':
    main()
