# or        1
# and       2
# not       3
# True      4
# False     5
# (         6
# )         7
# no valido -1

def lexico(codigo):
    estado = 0
    tokens = []
    palabra = ''
    i = 0
    n = len(codigo)
    while i < n or estado != 0:
        c = codigo[i] if i < n else ''
        if estado == 0:
            if c.isalpha():
                estado = 1
                i = i + 1
                palabra = palabra + c
                continue
            elif c == '(':
                estado = 3
                i = i + 1
                continue
            elif c == ')':
                estado = 4
                i = i + 1
                continue
            elif c.isspace():
                i = i + 1
                continue
            else:
                i = i + 1
        elif estado == 1:
            if c.isalnum():
                estado = 1
                i = i + 1
                palabra = palabra + c
                continue
            else:
                estado = 2
                continue
        elif estado == 2:
            if palabra == 'or':
                tokens.append(1)
            elif palabra == 'and':
                tokens.append(2)
            elif palabra == 'not':
                tokens.append(3)
            elif palabra == 'True':
                tokens.append(4)
            elif palabra == 'False':
                tokens.append(5)
            else:
                tokens.append(-1)
            palabra = ''
            estado = 0
            continue
        elif estado == 3:
            tokens.append(6)
            estado = 0
            continue
        elif estado == 4:
            tokens.append(7)
            estado = 0
            continue
    return tokens
    
codigo = ''
print(lexico(codigo))