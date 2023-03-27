def calculations(operation: list, marks: list) -> list:    # sprawdza kolejne wyrażenia z zachowaniem kolejności działań
    for x in range(2, 7, 2):
        count = 0
        while count < len(operation):
            if operation[count] in marks[x - 2:x]:  # sprawdza czy kolejne elementy to wyrażenia arytmetyczne
                try:
                    x1 = float(operation[count - 1])
                    x2 = float(operation[count + 1])
                except ValueError:
                    return [None]
                if x == 2:  # potęgowanie
                    ans = x1 ** x2
                elif x == 4:    # mnożenie
                    if operation[count] == marks[2]:
                        ans = x1 * x2
                    else:
                        try:
                            ans = x1 / x2
                        except ZeroDivisionError:
                            return [None]
                else:  # dodawanie
                    if operation[count] == marks[4]:
                        ans = x1 + x2
                    else:
                        ans = x1 - x2
                operation[count] = ans  # wpisuje wynik w miejsce działania
                operation.pop(count + 1)    # usuwa liczby przed i po działaniu
                operation.pop(count - 1)
            else:
                count += 1
    return operation


def main():     # DZIAŁA
    user_input: str
    operation: list
    operation_part: list
    marks = ['^', '**', '*', '/', '+', '-', '(', ')']   # działania do obliczeń
    user_input = input('Podaj działanie\n-> ')
    if user_input == '':     # warunek końca działania programu
        return True
    for mark in marks:      # zamiana str na liste
        if mark in user_input:
            user_input = user_input.replace(mark, f' {mark} ')  # to jest żeby split miało spacje
    operation = user_input.split()                             # replace zamienia wszystko naraz
    i = 0
    for x in operation:  # zamiana [..., '*', '*', ...] na [..., '**', ...]
        if x == '*':
            index = operation.index(x, i)
            if operation[index + 1] == x:
                operation.pop(index + 1)
                operation[index] = '**'
        i += 1
    bracket = True
    while bracket:   # zastosowanie priorytetu nawiasów
        if '(' in operation and ')' in operation:
            index1 = operation.index('(')
            index2 = operation.index(')')
            if index1 > index2:
                print('Zle postawione nawiasy')
            else:
                operation.pop(index2)
                operation.pop(index1)
                operation_part = calculations(operation[index1:index2 - 1], marks)    # wykonanie działania w nawiasach
                if None in operation_part:
                    operation = operation_part
                    break
                operation[index1:index2 - 1] = operation_part   # wklejenie wyniku w miejsce miedzy nawiasami
        elif '(' in operation and ')' not in operation:
            print("Brak ')'")
        elif '(' not in operation and ')' in operation:
            print("Brak '('")
        else:
            bracket = False
    if None not in operation:
        operation = calculations(operation, marks)  # wykonanie (reszty) działania jeśli wcześniej nie wystąpił błąd
    if len(operation) == 1 and type(operation[0]) == float:
        print(f'{operation[0]}\n')     # estetyka
    else:
        print(f'Coś poszło nie tak\n{operation}\n')
    return False


end = False
while not end:      # działanie w pętli
    end = main()
