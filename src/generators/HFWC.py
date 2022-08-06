"""
Zaaimplementuj funkcję generującą even_numbers(n: int) zwracającą kolejne liczby parzyste,
nie podzielne przez 3 do wartości maksymalnej, włącznie podanej jako argument
funkcji na przykład:
    - even_numbers(7) powinna zwracać kolejno: [2, 4]
    - even_numbers(15) powinna zwracać kolejno: [2, 4, 8, 10, 14]
"""
number = 20


# 1. sposób
def even_numbers(n):
    for i in range(0, n):
        yield i + 1


for even in even_numbers(number):
    if even % 2 == 0:
        if even % 3 != 0:
            print(even)

print('-_'*70)

# 2. sposób


def even_numbers(n):
    for i in range(0, n+1):
        if i % 2 == 0:
            if i % 3 != 0:
                print(i)
        yield i


for even in even_numbers(number):
    pass
