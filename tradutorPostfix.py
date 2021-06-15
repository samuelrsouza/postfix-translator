OPERADOES = set(['+', '-', '*', '/', '(', ')', '^'])

ORD_PRIORIDADE = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}


def infix_para_postfix(expression):
    pilha = []  # inicialmente a pilha começa vazia
    output = ''

    for ch in expression:

        if ch not in OPERADOES:

            output += ch

        elif ch == '(':

            pilha.append('(')

        elif ch == ')':

            while pilha and pilha[-1] != '(':
                output += pilha.pop()

            pilha.pop()

        else:
            while pilha and pilha[-1] != '(' and ORD_PRIORIDADE[ch] <= ORD_PRIORIDADE[pilha[-1]]:
                output += pilha.pop()
            pilha.append(ch)
    while pilha:
        output += pilha.pop()
    return output

expression = input('Digite a expressão infix: ')
print('Expressão infix: ', expression)
print('Expressão postfix: ', infix_para_postfix(expression))