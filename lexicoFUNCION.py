
# def       1
# pass      2
# :         3
# ,         4
# =         5
# (         6
# )         7
# Newline   8
# VARIABLE  9
# NUMERO    10
def lexico(codigo):
    estado = 0
    tokens = []
    palabra = ''
    i = 0
    n = len(codigo)
    while i < n or estado != 0:
        c = codigo[i] if i < n else ''
        if estado == 0:
            if c.isalpha() or c == '_':
                estado = 1
                i = i + 1
                palabra = palabra + c
                continue
            elif c.isdigit():
                estado = 9
                i = i + 1
                palabra = palabra + c
                continue
            elif c == '\n':
                i = i + 1
                if len(tokens) > 0 and tokens[-1] != 8:
                    estado = 3
                continue
            elif c == ':':
                estado = 4
                i = i + 1
                continue
            elif c == ',':
                estado = 5
                i = i + 1
                continue
            elif c == '=':
                estado = 6
                i = i + 1
                continue
            elif c == '(':
                estado = 7
                i = i + 1
                continue
            elif c == ')':
                estado = 8
                i = i + 1
                continue
            elif c.isspace():
                i = i + 1
                continue
            else:
                i = i + 1
        elif estado == 1:
            if c.isalnum() or c == '_':
                estado = 1
                i = i + 1
                palabra = palabra + c
                continue
            else:
                estado = 2
                continue
        elif estado == 2:
            if palabra == 'def':
                tokens.append(1)
            elif palabra == 'pass':
                tokens.append(2)
            else:
                tokens.append(9)
            palabra = ''
            estado = 0
            continue
        elif estado == 3:
            tokens.append(8)
            estado = 0
            continue
        elif estado == 4:
            tokens.append(3)
            estado = 0
            continue
        elif estado == 5:
            tokens.append(4)
            estado = 0
            continue
        elif estado == 6:
            tokens.append(5)
            estado = 0
            continue
        elif estado == 7:
            tokens.append(6)
            estado = 0
            continue
        elif estado == 8:
            tokens.append(7)
            estado = 0
            continue
        elif estado == 9:
            if c.isdigit():
                estado = 9
                i = i + 1
                palabra = palabra + c
                continue
            else:
                estado = 10
                continue
        elif estado == 10:
            tokens.append(10)
            palabra = ''
            estado = 0
            continue
    return tokens
    
codigo = '''
def suma(a, b):
    c = a
    pass
'''
print(lexico(codigo))